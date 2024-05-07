#!/usr/bin/python3
"""get the number of all subscriber in subreddit"""

import requests


def top_ten(subreddit):
    """ get number of subscriber"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
        (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    paramater = {"limit": 10}
    respons = requests.get(url=url, allow_redirects=False,
                           headers={"User-Agent": user_agent},
                           params=paramater)
    if respons.status_code == 404:
        print("None")
        return
    data = respons.json().get("data")
    [print(titles.get("data").get("title"))
     for titles in data.get("children")]
