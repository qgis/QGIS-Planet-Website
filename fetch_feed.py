#!/usr/bin/env python3

# This script fetches the RSS feed of each subscriber and creates a new markdown file for each entry

import feedparser
import os
import json
from tqdm import tqdm
from urllib.parse import urlparse
import requests
import shutil
from datetime import datetime
import re

# Path to the subscribers.json file
SUBSCRIBERS_JSON_PATH = os.path.join(os.path.dirname(__file__), 'data', 'subscribers.json')


def fetch_and_create_post(subscriber_name, subscriber, feed_url):
    try:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            process_entry(entry, subscriber, subscriber_name)
    except Exception as e:
        print(f"Failed to process feed for {subscriber}: {e}")


def process_entry(entry, subscriber, subscriber_name):
    try:
        title = entry.title
        print(entry)
        # authors = entry.authors
        image_url = entry.links[-1].href
        if image_url.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp')):
            file_name = get_image_name(image_url)
            download_image(image_url, file_name, subscriber)

        file_name = os.path.basename(os.path.normpath(image_url))
        entry_date = get_entry_date(entry)
        summary = get_summary(entry)
        sanitized_subscriber = sanitize_name(subscriber)

        content = generate_markdown_content(title, file_name, entry_date, image_url, summary, sanitized_subscriber, subscriber_name)
        subscriber_folder = os.path.join("content", "community-blogs", sanitized_subscriber)
        os.makedirs(subscriber_folder, exist_ok=True)
        markdown_filename = os.path.join(subscriber_folder, f"{file_name}.md")
        write_to_file(markdown_filename, content)

    except Exception as e:
        print(f"Failed to process entry for {subscriber}: {e}")


def get_image_name(image_url):
    path = urlparse(image_url).path
    print(image_url)
    image_ext = os.path.splitext(path)[1]
    name = os.path.basename(os.path.normpath(image_url))
    image_name = f"{name}.{image_ext}".replace("..", ".")
    return image_name


def get_entry_date(entry):
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


def get_summary(entry):
    try:
        return entry.summary
    except AttributeError:
        return ""


def sanitize_name(name):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name).lower()


def generate_markdown_content(title, entry_date, image_url, summary, sanitized_subscriber, subscriber_name):
    return f"""---
source: "blog"
title: "{title}"
date: "{entry_date}"
link: "{image_url}"
draft: "true"
showcase: "planet"
folder: "{sanitized_subscriber}"
author: "{subscriber_name}"
---

{summary}
"""


def write_to_file(filename, content):
    with open(filename, "w", encoding="utf=8") as f:
        f.write(content)


def download_image(image_url, image_name, subscriber):
    response = requests.get(image_url, stream=True)
    sanitized_subscriber = sanitize_name(subscriber)
    subscriber_folder = os.path.join("content", "community-blogs", sanitized_subscriber)
    os.makedirs(subscriber_folder, exist_ok=True)
    image_filename = os.path.join(subscriber_folder, image_name)
    with open(image_filename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
        print(f"Writing: {image_filename}")


if __name__ == "__main__":
    # Load the subscribers from the JSON file
    with open(SUBSCRIBERS_JSON_PATH, 'r') as f:
        subscribers = json.load(f)
    
    subscribers = [
        {
            "feed": "https://merginmaps.com/rss/qgis",
            "name": "Mergin Maps",
            "shortname": "Mergin Maps",
            "is_active": True
        }
    ]

    # Iterate over the subscribers and fetch posts for active ones with a progress bar
    for subscriber in tqdm(subscribers, desc="Processing subscribers"):
        if subscriber['is_active']:
            fetch_and_create_post(subscriber['name'], subscriber['shortname'], subscriber['feed'])
