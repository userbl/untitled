#!/usr/bin/python3
# coding=UTF-8
import requests
import bs4
from datetime import datetime, date, timedelta
import pymysql
import calendar
import  time

root_url='https://toutiao.io/prev/'
index_url = root_url+'2017-03-02'
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch, br',
'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6'}

def grab_iteye() :

    grab_data = []
    ip_chrome = 'http://down.tech.sina.com.cn/download/d_load.php?d_id=40975&down_id=5&ip=61.138.184.186'
    ip_zip ='http://down.tech.sina.com.cn/download/d_load.php?d_id=37931&down_id=1&ip=61.138.184.186'
    response = requests.get(ip_zip, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}, stream=True)
    # print(response.content)
    print(response.headers)
    length_ = response.headers['Content-Length']
    print(length_)
    file_name = response.headers['Content-Disposition'].split(';', 1)[1].split('=', 1)[1].strip('"')
    print(file_name)
    f = open(file_name, "wb")
    total = 0;
    for chunk in response.iter_content(chunk_size=1024):
        total = total+ len(chunk)
        print('%.2f%%' % (total/int(length_)*100), end="\r")
        if chunk:
            f.write(chunk)

    f.close()
    # url ='http://119.188.72.124/tech.down.sina.com.cn/20170322/008e0e99/59.0.3047.4_chrome_installer.exe?fn=&ssig=PATkRUBXTT&Expires=1490430773&KID=sae,230kw3wk15&ip=1490351573,61.138.184.186&corp=1'
    # response = requests.head(url,
    #                          headers={
    #                              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
    # # print(response.content)
    # print(response.headers)
    return grab_data



data = grab_iteye()

