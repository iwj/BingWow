#!/usr/bin/env python
# -*- coding:utf-8  -*-


import bs4
import requests
import json
import urllib

def bing_wow():
    #error_img_url
    #error_img = "http://www.geekpark.net/404_bg.png"
    bing_json = "http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1444634662901&pid=hp"
    result = requests.get(bing_json).text
    result_dict = json.loads(result)
    img_url = result_dict.get("images")[0].get("url")
    file_name = img_url.split("/")[-1]
    urllib.urlretrieve(img_url, file_name)
    img_status =  img_url+"\nsuccess"
    log_text = "抓取日志"
    log_text += "\n success"
    with open("bing_log.txt", "w") as f:
        f.write(log_text)


if __name__ == "__main__":
    bing_wow()
