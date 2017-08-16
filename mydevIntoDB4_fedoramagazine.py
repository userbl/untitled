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



def get_news_page(url):

    grab_data = []

    response = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
    soup = bs4.BeautifulSoup(response.content.decode("utf-8"), "html.parser")
    page_detail = [a for a in soup.select('div.post-container div.post-header>h2>a')]

    grab_data = grab_data + page_detail

    for i in range(10000) :
        response = requests.get(url+"page/"+str(i)+"/",headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
        soup = bs4.BeautifulSoup(response.content.decode("utf-8"),"html.parser")
        #print(response.content.decode("utf-8"))
        page_detail = [a for a in soup.select('div.post-container div.post-header h2 a')]
        print(' ---page_detail:' + str(len(page_detail)))
        if(len(page_detail) == 0) :
            break
        grab_data=grab_data+page_detail
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
                sql = 'SELECT count(1) cc FROM tech_article_fedora WHERE title=%s and url=%s'
                cursor.execute(sql, (dd[0],dd[1]))
                result = cursor.fetchone()
                # print('insert:' + result) #Can't convert 'dict' object to str implicitly
                # print(result['cc'])
            if result['cc'] == 0:
                with connection.cursor() as cursor:
                    # Create a new record
                    sql = "INSERT INTO `tech_article_fedora` (`title`, `url`,`date_str`,`where_come_from`) VALUES (%s, %s,%s,%s)"
                    result = cursor.execute(sql, (dd[0],dd[1], dd[2],dd[3]))
                    saved_data.append(dd)
                    print("------------------------insert")
                    # print('insert:' + result)
    finally:

        connection.close()
    return  saved_data


def grab() :
    year = datetime.today().year
    month = datetime.today().month
    day = datetime.today().day

    detail_count = 0;
    grab_data = []

    # grab_data = get_news_page("https://fedoramagazine.org/")

    detail = get_news_page("https://fedoramagazine.org/");
    detail_count += len(detail)
    print(" detail:" + str(len(detail)))
    for b in detail:
        grab_data.append(
            (b.get_text(), b.attrs.get('href'), str(datetime.today())[0:10], 'fedora_magazine'))


    print(' detail_count:' + str(detail_count));
    return grab_data


from socket import *
from datetime import datetime

#
data = grab()
print(len(data))
saved_data = saveToDB(data)
for a in saved_data :
    print(a)


