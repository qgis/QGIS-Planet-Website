#!/usr/bin/env python3

import feedparser
import os
import json
from tqdm import tqdm
from urllib.parse import urlparse
import requests
import shutil
from datetime import datetime
from scripts.resize_image import resize_image
from dateutil.parser import parse as date_parse

# Path to the subscribers.json file
SUBSCRIBERS_JSON_PATH = os.path.join(os.path.dirname(__file__), 'data', 'subscribers.json')
ALL_POSTS_FOLDER = os.path.join("content", "posts")

class FeedProcessor:
    def __init__(self, subscriber_name, shortname, feed_url):
        """
        Initializes a new instance of the class.

        Args:
            subscriber_name (str): The name of the subscriber.
            shortname (str): A short name or identifier for the subscriber.
            feed_url (str): The URL of the feed to be fetched.

        Description:
            This class is responsible for initializing the subscriber's details 
            including their name, a short identifier, and the URL of the feed 
            they are subscribed to.
        """
        self.subscriber_name = subscriber_name
        self.shortname = shortname
        self.feed_url = feed_url

    def fetch_and_create_post(self):
        try:
            feed = feedparser.parse(self.feed_url)
            for entry in feed.entries:
                self.process_entry(entry)
        except Exception as e:
            print(f"Failed to process feed for {self.subscriber_name}: {e}")

    def process_entry(self, entry):
        try:
            title = entry.title
            image_url = entry.links[-1].href
            if image_url.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp')):
                file_name = self.get_image_name(image_url)
                self.download_image(image_url, file_name)

            file_name = os.path.basename(os.path.normpath(image_url))
            entry_date = self.get_entry_date(entry)
            content = self.get_content(entry)
            if not content:
                content = self.get_summary(entry)
            tags = self.get_tags(entry)

            content = self.generate_markdown_content(title, entry_date, image_url, content, tags)
            
            # Copy the markdown file to the all-posts folder
            os.makedirs(ALL_POSTS_FOLDER, exist_ok=True)
            markdown_filename = os.path.join(ALL_POSTS_FOLDER, f"{file_name}.md")
            self.write_to_file(markdown_filename, content)

        except Exception as e:
            print(f"Failed to process entry for {self.subscriber_name}: {e}")

    def get_image_name(self, image_url):
        path = urlparse(image_url).path
        image_ext = os.path.splitext(path)[1]
        name = os.path.basename(os.path.normpath(image_url))
        image_name = f"{name}.{image_ext}".replace("..", ".")
        return image_name

    def get_entry_date(self, entry):
        date_formats = [
            "%a, %d %b %Y %H:%M:%S %z",  # Example: Wed, 14 Dec 2022 00:00:00 +0000
            "%a, %d %b %Y %H:%M:%S %Z",  # Example: Wed, 14 Dec 2022 00:00:00 GMT
            "%Y-%m-%dT%H:%M:%SZ",        # Example: 2024-09-04T04:52:11Z
            "%Y-%m-%dT%H:%M:%S%z"        # Example: 2017-09-01T12:09:27+02:00
        ]
        
        date_to_parse = entry.get('updated', entry.get('published', None))
        if date_to_parse:
            for date_format in date_formats:
                try:
                    parsed_date = datetime.strptime(date_to_parse, date_format)
                    return parsed_date.strftime("%Y-%m-%dT%H:%M:%S%z")
                except (AttributeError, ValueError):
                    continue
        
        print("Date format error: Unable to parse date")
        with open("unprocessed_dates.txt", "a") as f:
            f.write(f"Failed to parse date for entry: {entry.get('updated', entry.get('published', None))} \n\n")
        return ""

    def get_summary(self, entry):
        try:
            return entry.summary
        except AttributeError:
            return ""
        
    def get_content(self, entry):
        try:
            return entry.content[0].value
        except AttributeError:
            return None

    def get_tags(self, entry):
        try:
            return [tag.term.lower() for tag in entry.tags]
        except AttributeError:
            return []

    def generate_markdown_content(self, title, entry_date, image_url, summary, tags):
        tags_str = ", ".join([f'"{tag}"' for tag in tags])
        return f"""---
source: "blog"
title: "{title}"
date: "{entry_date}"
link: "{image_url}"
draft: "false"
showcase: "planet"
subscribers: ["{self.shortname}"]
author: "{self.subscriber_name}"
tags: [{tags_str}]
---

{summary}
"""

    def write_to_file(self, filename, content):
        with open(filename, "w", encoding="utf=8") as f:
            f.write(content)

    def download_image(self, image_url, image_name):
        response = requests.get(image_url, stream=True)
        os.makedirs(ALL_POSTS_FOLDER, exist_ok=True)
        image_filename = os.path.join(ALL_POSTS_FOLDER, image_name)
        with open(image_filename, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
            print(f"Writing: {image_filename}")

class FunderProcessor:
    """
    A class to process and fetch funder information from a remote JSON feed.

    This class provides methods to fetch funder data from a specified URL, process each funder entry,
    and generate corresponding markdown files and images for each funder.

    Methods:
        fetch_funders(): Fetches the funder data from the remote JSON feed.
        process_funder(item): Processes a single funder entry and generates the markdown file and image.
    """

    @staticmethod
    def fetch_funders():
        response = requests.get("https://changelog.qgis.org/en/qgis/members/json/")
        data = json.loads(response.text)
        items = data["rss"]["channel"]["item"]
        for item in items:
            FunderProcessor.process_funder(item)

    @staticmethod
    def process_funder(item):
        link = item["member_url"]
        image_url = item["image_url"]
        title = item["title"]
        level = item["member_level"]
        country = item["member_country"]
        start_date = item["start_date"]
        end_date = item["end_date"]

        start_date = date_parse(start_date, fuzzy_with_tokens=True)[0]
        start_date = start_date.strftime("%Y-%m-%d")
        end_date = date_parse(end_date, fuzzy_with_tokens=True)[0]
        end_date = end_date.strftime("%Y-%m-%d")

        path = urlparse(image_url).path
        image_ext = os.path.splitext(path)[1]
        name = os.path.basename(os.path.normpath(link))
        image_name = "%s.%s" % (name, image_ext)
        image_name = image_name.replace("..",".")

        content = f"""---
level: "{level}"
title: "{title}"
logo: "{image_name}"
startDate: "{start_date}"
endDate: "{end_date}"
link: "{link}"
country: "{country}"
---
"""
        markdown_filename = f"content/funders/{name}.md"
        with open(markdown_filename , "w", encoding="utf=8") as f:
            f.write(content)
            print(f"Writing: {markdown_filename}")

        response = requests.get(image_url, stream=True)
        image_filename = f"content/funders/{image_name}"
        with open(image_filename, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
            print(f"Writing: {image_filename}")
        del response
        try:
            if level.lower() in ["flagship", "large"]:
                resize_image(image_filename, max_height=150)
            else:
                resize_image(image_filename)
        except Exception as e:
            print(f"Error resizing image: {e}")

if __name__ == "__main__":
    # Load the subscribers from the JSON file
    with open(SUBSCRIBERS_JSON_PATH, 'r') as f:
        subscribers = json.load(f)

    # Iterate over the subscribers and fetch posts for active ones with a progress bar
    for subscriber in tqdm(subscribers, desc="Processing subscribers"):
        if subscriber['is_active']:
            processor = FeedProcessor(subscriber['name'], subscriber['shortname'], subscriber['feed'])
            processor.fetch_and_create_post()
    
    FunderProcessor.fetch_funders()
