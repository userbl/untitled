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


def get_news(date_str):
    # 格式化成2016-03-20 11:45:39形式
    today = date_str    # '2017-03-01'#time.strftime("%Y-%m-%d", time.localtime())
    # print(today)
    response = requests.get('https://toutiao.io/prev/'+today,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
    soup = bs4.BeautifulSoup(response.content.decode("utf-8"),"html.parser")
    #print(response.content.decode("utf-8"))
    return [a for a in soup.select('div.content h3 a')]
    #print(links)


def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


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

def queryTargetFQUser() :

    try:
        connection = pymysql.connect(host='192.168.11.185',
                                     user='root',
                                     password='abc',
                                     db='my_dev',
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            # Read a single record
            sql = 'SELECT ip,ip_man  FROM receiver  '
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    finally:

        connection.close()

def grab() :
    year = datetime.today().year
    month = datetime.today().month
    day = datetime.today().day

    grab_data = []

    for d in date_range(datetime(2013, 9, 27), datetime(year,month,day),
                        timedelta(hours=24)):

    # for d in date_range(datetime(year, month, dd), datetime(year, month, day + 5),
    #                     timedelta(hours=24)):

        d_ = str(d)[0:10]
        date_str = d_  # "2014-09-27"
        news = get_news(date_str)
        print(d_ + ' ' + str(len(news)))
        for a in news:
            # print('     ' + a.get_text())
            href_ = 'https://toutiao.io' + a.attrs.get('href')
            grab_data.append((a.get_text(), href_, d_, 'develop_first'))
            # print(grab_data)

    return grab_data

from socket import *
from datetime import datetime
import re

#
data = grab()#grab_iteye_jinghua()+ grab()+grab_infoq()+grab_iteye()
saved_data = saveToDB(data)
for a in saved_data :
    print(a)
fq_user = queryTargetFQUser()
# print(fq_user)

# aa =[{'ip_man': '白龙', 'ip': '192.168.9.64'}, {'ip_man': '于鑫', 'ip': '192.168.9.6'}]
# print(aa[0]['ip'])



#print(get_news())
