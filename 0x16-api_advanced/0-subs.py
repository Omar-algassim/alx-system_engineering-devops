#!/usr/bin/python3
"""get the number of all subscriber in subreddit"""

import requests
import os


def number_of_subscribers(subreddit):
    """ get number of subscriber"""
    url = f"https://www.reddit.com/r/{subreddit}/about"
    respons = requests.get(url=url, allow_redirects=False)
    if respons.status_code == 404:
        return 0
    data = respons.json()
    return data.subscribers
