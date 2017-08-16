#!/usr/bin/python3
# coding=UTF-8
import requests
import bs4
from datetime import datetime, date, timedelta
import pymysql
import calendar
import  time
import string

root_url='https://toutiao.io/prev/'
index_url = root_url+'2017-03-02'
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch, br',
'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6'}


def grab_infoq() :

    grab_data = []
    response = requests.get('https://laod.cn/hosts/2017-google-hosts.html',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
    soup = bs4.BeautifulSoup(response.content.decode("utf-8"),"html.parser")

    news =  [a for a in soup.select('div.buttons a')]

    href_ = news[0].attrs.get('href')
    strip = news[0].get_text().strip()
    print(strip+" "+href_)

    real_url =href_[href_.find("url=")+4:len(href_)]

    print(real_url)
    grab_file(real_url)
    if len(strip) > 1 :
        grab_data.append((strip, href_, str(datetime.today())[0:10], 'infoq'))

    return grab_data

def grab_file(page_url) :
    # page_url="https://iiio.io/download/20170709/"
    print("page_url: "+page_url)
    grab_data = []
    response = requests.get(page_url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
    soup = bs4.BeautifulSoup(response.content.decode("utf-8"),"html.parser")

    news =  [a for a in soup.select('a')]

    for a in news:
        href_ = a.attrs.get('href')
        strip = a.get_text().strip()
        result = 'Android' in strip
        print("result: "+str(result))
        if  result :
            print(" 下载文件:" + strip)
            ip_zip = page_url+href_
            response = requests.get(ip_zip, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'},
                                    stream=True)
            print(response.headers)
            length_ = response.headers['Content-Length']
            print(length_)
            file_name = strip  #response.headers['Content-Disposition'].split(';', 1)[1].split('=', 1)[1].strip('"')
            print(file_name)
            f = open(file_name, "wb")
            total = 0;
            for chunk in response.iter_content(chunk_size=1024):
                total = total + len(chunk)
                print('%.2f%%' % (total / int(length_) * 100), end="\r")
                if chunk:
                    f.write(chunk)

            f.close()



    # href_ = news[0].attrs.get('href')
    # strip = news[0].get_text().strip()
    # print(strip+" "+href_)
    # if len(strip) > 1 :
    #     grab_data.append((strip, href_, str(datetime.today())[0:10], 'infoq'))

    return grab_data


def saveToDB(data):
    saved_data =[]
    try:
        connection = pymysql.connect(host='192.168.11.185',
                                     user='root',
                                     password='abc',
                                     db='my_dev',
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)
        for dd in data :
            with connection.cursor() as cursor:
                # Read a single record
                sql = 'SELECT count(1) cc FROM tech_article WHERE title=%s and url=%s'
                cursor.execute(sql, (dd[0],dd[1]))
                result = cursor.fetchone()
                # print('insert:' + result) #Can't convert 'dict' object to str implicitly
                # print(result['cc'])
            if result['cc'] == 0:
                with connection.cursor() as cursor:
                    # Create a new record
                    sql = "INSERT INTO `tech_article` (`title`, `url`,`date_str`,`where_come_from`) VALUES (%s, %s,%s,%s)"
                    result = cursor.execute(sql, (dd[0],dd[1], dd[2],dd[3]))
                    saved_data.append(dd)
                    print("------------------------insert")
                    # print('insert:' + result)
    finally:

        connection.close()
    return  saved_data


from datetime import datetime


data = grab_infoq() #grab_iteye_jinghua()+ grab()+grab_infoq()+grab_iteye()
# saved_data = saveToDB(data)
# for a in saved_data :
#     print(a)

import os
os.system("~/update_hosts.sh")