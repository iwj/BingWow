#!/usr/bin/env python
# -*- coding:utf-8  -*-


import bs4
import requests
import json
import urllib

def bing_wow():
    bing_json = "http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1444634662901&pid=hp"
    result = requests.get(bing_json).text
    result_dict = json.loads(result)
    img_url = result_dict.get("images")[0].get("url")
    img_url = "http://cn.bing.com" + img_url
    file_name = img_url.split("/")[-1]
    print img_url
    print file_name
    urllib.urlretrieve(img_url, file_name)


if __name__ == "__main__":
    bing_wow()
