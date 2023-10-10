#!/usr/bin/python3
"""Function that queries Reddit API"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts
    listed for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'custom'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
    else:
        posts = response.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
