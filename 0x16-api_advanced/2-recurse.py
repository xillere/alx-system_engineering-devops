#!/usr/bin/python3
"""return/query a list of every hot post on a subreddit"""
import requests


def recurse(subreddit, hot_list=[], end="", inc=0):
    """returns a list of titles of every hot post on a subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": end,
        "count": inc,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    end = results.get("after")
    inc += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, end, inc)
    return hot_list
