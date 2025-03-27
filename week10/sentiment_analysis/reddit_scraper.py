# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import time

# URL of the website to scrape
url = 'https://www.reddit.com/r/technology/'

# Add a delay of one second
time.sleep(1)

# Send a GET request to the website
response = requests.get(url)

if response.status_code == 200:

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <shreddit-post> tags
    posts = soup.select('shreddit-post')

    # Display a summary of each post
    for post in posts:
        print(f"""
        Title: {post['post-title']}
        Author: {post['author']}
        Posted: {post['created-timestamp']}
        Stats: Score = {post['score']}, Comments = {post['comment-count']}
        Permalink: {post['permalink']}
        """)

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")