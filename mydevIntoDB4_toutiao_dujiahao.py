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





def grab_item() :

    grab_data = []
    response = requests.get('http://www.iteye.com/news', headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
    soup = bs4.BeautifulSoup(response.content.decode("utf-8"), "html.parser")

    news = [a for a in soup.select('div.content h3 a')]

    for a in news:
        href_ = 'http://www.iteye.com' + a.attrs.get('href')
        text = a.get_text()
        strip = text.strip()
        if '[' in strip :
            pass
        else:
            grab_data.append((strip, href_, str(datetime.today())[0:10], 'iteye'))

    return grab_data


def grab_toutiao_dujihao() :

    grab_data = []
    response = requests.get('https://toutiao.io/explore',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
    soup = bs4.BeautifulSoup(response.content.decode("utf-8"),"html.parser")

    news =  [a for a in soup.select('ul.subjects li div.media-body h4.media-heading a')]+[a for a in soup.select('div.full_width h3 a')]+[a for a in soup.select('div.news h3 a')]
    for a in news:
        href_ = 'http://www.infoq.com' + a.attrs.get('href')
        strip = a.get_text().strip()
        if len(strip) > 1 :
            grab_data.append((strip, href_, str(datetime.today())[0:10], 'infoq'))
            print(strip+"  "+a.attrs.get('href'))

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




from socket import *
from datetime import datetime
import re



#
data = grab_toutiao_dujihao() #grab_iteye_jinghua()+ grab()+grab_infoq()+grab_iteye()
# saved_data = saveToDB(data)
# for a in saved_data :
    # print(a)


