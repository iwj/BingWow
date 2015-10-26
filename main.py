#!/usr/bin/env python
# -*- coding:utf-8  -*-


import bs4
import requests
import json
import urllib

def get_soup(url, file_str):
    request_result = requests.get(url)
    soup = bs4.BeautifulSoup(request_result.text, "html.parser")
    #soup = bs4.BeautifulSoup("<html>data</html>", "html.parser")

    error_img = "http://www.geekpark.net/404_bg.png"

    if soup.img:
        file_str = file_str + "\n" + soup.img["src"]
        print soup.img["src"]
        
    else:
        print "Not find image"
        print error_img

    return file_str

def run_wufazhuce():
    file_str = ""
    url_pre = "http://wufazhuce.com/one/vol."
    #TODO 计算今天与第一期前一天的差，得到今天的期数
    #article_number = 1098
    for i in range(1, 1099):
        article_number = i
        url = url_pre + str(article_number)
        file_str = get_soup(url, file_str)

    #若不存在，自动新建文件
    with open("one_list.txt", "w") as f:
        f.write(file_str)

def run_bing():
    bing_json = "http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1444634662901&pid=hp"
    result = requests.get(bing_json).text
    result_dict = json.loads(result)
    img_url = result_dict.get("images")[0].get("url")
    file_name = img_url.split("/")[-1]
    urllib.urlretrieve(img_url, file_name)
    img_status =  img_url+"\nsuccess"
    log_text = "* " * 10
    log_text += "\n抓取日志\n"
    log_text += " success"
    with open("bing_log.txt", "w") as f:
        f.write(log_text)

def main():
    choice = raw_input("输入选择（A:ONE一个 或者B:Bing）")
    if choice == "A":
        run_wufazhuce()
    elif choice == "B":
        run_bing()
    else:
        print "未选择有效的run，结束。"

if __name__ == "__main__":
    run_bing()
