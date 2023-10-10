#!/usr/bin/python3
"""Function that queries Reddit API"""

import requests


def recurse(subreddit, hot_list=[], after=None, counter=0):
    """ returns a list containing the titles of all hot articles
    for a given subreddit. If no results are found for
    the given subreddit, the function should return None."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    if after:
        url += f"?after={after}"
    headers = {'User-Agent': 'custom'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        return None
    else:
        data = response.json()['data']
        hot_list.extend([post['data']['title'] for post in data['children']])
        counter += 1
        print(f"Recursive call {counter}: Added {len(data['children'])} posts to the list")
        if data['after']:
            return recurse(subreddit, hot_list, data['after'], counter)
        else:
            return hot_list
