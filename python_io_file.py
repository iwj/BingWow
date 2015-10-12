# -*- coding: utf8 -*-

filename = raw_input("文件名")


with open(filename+".txt", "r") as f:
    print f.read()
