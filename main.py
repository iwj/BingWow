#!/usr/bin/env python
# -*- coding:utf-8  -*-


import bs4
import requests
import json
import urllib

def get_soup(url):
    request_result = requests.get(url)
    soup = bs4.BeautifulSoup(request_result.text, "html.parser")
    #soup = bs4.BeautifulSoup("<html>data</html>", "html.parser")

    error_img = "http://www.geekpark.net/404_bg.png"

    if soup.img:
        #若不存在，自动新建文件
        with open("one_list.txt", "w") as f:
            f.write(soup.img["src"])
        print soup.img["src"]
    else:
        print "Not fing image"
        print error_img

def run_wufazhuce():
    url_pre = "http://wufazhuce.com/one/vol."
    #TODO 计算今天与第一期前一天的差，得到今天的期数
    #article_number = 1098
    for i in range(1, 10):
        article_number = i
        url = url_pre + str(article_number)
        get_soup(url)

def run_bing():
    bing_json = "http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1444634662901&pid=hp"
    result = requests.get(bing_json).text
    result_dict = json.loads(result)
    img_url = result_dict.get("images")[0].get("url")
    file_name = img_url.split("/")[-1]
    urllib.urlretrieve(img_url, file_name)
    print img_url+"\nsuccess"

def main():
    choice = raw_input("输入选择（A:ONE一个 或者B:Bing）")
    if choice == "A":
        run_wufazhuce()
    elif choice == "B":
        run_bing()
    else:
        print "为选择有效的run，结束。"

if __name__ == "__main__":
    main()
