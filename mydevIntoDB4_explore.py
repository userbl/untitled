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



def get_news():
    # 格式化成2016-03-20 11:45:39形式
    # print(today)
    response = requests.get('https://toutiao.io/explore',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
    soup = bs4.BeautifulSoup(response.content.decode("utf-8"),"html.parser")
    #print(response.content.decode("utf-8"))
    return [a for a in soup.select('.subjects h4.media-heading a')]
    #print(links)

def get_news_page(url):

    grab_data = []
    for i in range(10000) :
        response = requests.get(url+"?page="+str(i),headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
        soup = bs4.BeautifulSoup(response.content.decode("utf-8"),"html.parser")
        #print(response.content.decode("utf-8"))
        page_detail = [a for a in soup.select('div.post h3 a')];
        print(' ---page_detail:' + str(len(page_detail)))
        if(len(page_detail) == 0) :
            break;
        grab_data=grab_data+page_detail;
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
        insert_count =0;
        for dd in data :
            with connection.cursor() as cursor:
                # Read a single record
                sql = 'SELECT count(1) cc FROM tech_article_explore WHERE title=%s and url=%s'
                cursor.execute(sql, (dd[0],dd[1]))
                result = cursor.fetchone()
                # print('insert:' + result) #Can't convert 'dict' object to str implicitly
                # print(result['cc'])
            if result['cc'] == 0:
                with connection.cursor() as cursor:
                    # Create a new record
                    sql = "INSERT INTO `tech_article_explore` (`title`, `url`,`date_str`,`where_come_from`) VALUES (%s, %s,%s,%s)"
                    result = cursor.execute(sql, (dd[0],dd[1], dd[2],dd[3]))
                    saved_data.append(dd)
                    insert_count+=1
                    # print("------------------------insert")
                    # print('insert:' + result)
        print("insert_count:"+str(insert_count))
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
        grab_data = []

        news = get_news()
        print(' ' + str(len(news)))
        detail_count =0;
        index =0;
        for a in news:
            index+=1;
            if index >10:
                print('     ' + a.get_text())
                href_ = 'https://toutiao.io' + a.attrs.get('href')
                detail = get_news_page(href_);
                detail_count+=len(detail)
                print(" detail:"+str(len(detail)))
                #grab_data = grab_data +detail;
                #grab_data.append((a.get_text(), href_, 'develop_first'))
                for b in detail:
                    grab_data.append((b.get_text(), 'https://toutiao.io' + b.attrs.get('href'), str(datetime.today())[0:10], 'develop_first'))

        print(' detail_count:' + str(detail_count));


        return grab_data

from socket import *
from datetime import datetime
import re

def sendTo_FeiQiu(saved_data,fq_user) :
    cs = socket(AF_INET, SOCK_DGRAM)
    cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)


    msg = ''
    for sd in saved_data:
        msg=msg+sd[0]+" "+sd[1]+"\n"
        pass
    # for sd in saved_data :
    for fq_u in fq_user :
        # cs.sendto(bytes("1:100:tech:tech_man:32:"+sd[0]+" "+sd[1], encoding="gb2312"), (fq_u['ip'], 2425))
        cs.sendto(bytes("1:100:tech:tech_info:32:" + msg, encoding="gbk"), (fq_u['ip'], 2425))


    cs.close()


data = grab()
saved_data = saveToDB(data)
print(' data_count:' + str(len(data)));
# for a in data :
#     print(a)


fq_user = queryTargetFQUser()

sendTo_FeiQiu(saved_data,fq_user)

# print(str(str(datetime.today())[0:10]))

# aa =[{'ip_man': '白龙', 'ip': '192.168.9.64'}, {'ip_man': '于鑫', 'ip': '192.168.9.6'}]
# print(aa[0]['ip'])



#print(get_news())
