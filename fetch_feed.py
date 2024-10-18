#!/usr/bin/env python3

# This script fetches the RSS feed of each subscriber and creates a new markdown file for each entry

import feedparser
import os
import json
from tqdm import tqdm

# Path to the subscribers.json file
SUBSCRIBERS_JSON_PATH = os.path.join(os.path.dirname(__file__), 'data', 'subscribers.json')


def fetch_and_create_post(subscriber, feed_url):
    try:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            title = entry.get('title', 'No Title')
            content = entry.get('summary', 'No Content')
            date = entry.get('published', 'No Date')
            slug = entry.get('link', 'No Link').split("/")[-1]

            # Use shortname for the markdown file name
            filename = f"{subscriber}-{slug}.md"
            folder = os.path.join("content", "posts", subscriber)
            os.makedirs(folder, exist_ok=True)
            filepath = os.path.join(folder, filename)

            with open(filepath, "w") as f:
                f.write(f"---\n")
                f.write(f"title: \"{title}\"\n")
                f.write(f"date: {date}\n")
                f.write(f"author: \"{subscriber}\"\n")
                f.write(f"---\n\n")
                f.write(content)
    except Exception as e:
        print(f"Failed to process feed for {subscriber}: {e}")


if __name__ == "__main__":
    # Load the subscribers from the JSON file
    with open(SUBSCRIBERS_JSON_PATH, 'r') as f:
        subscribers = json.load(f)

    # Iterate over the subscribers and fetch posts for active ones with a progress bar
    for subscriber in tqdm(subscribers, desc="Processing subscribers"):
        if subscriber['is_active']:
            fetch_and_create_post(subscriber['shortname'], subscriber['feed'])