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


#
data = grab_iteye()
print(data)
for a in data :

    print(a)
# saved_data = saveToDB(data)
# fq_user = queryTargetFQUser()
# print(fq_user)
# sendTo_FeiQiu(saved_data,fq_user)

# aa =[{'ip_man': '白龙', 'ip': '192.168.9.64'}, {'ip_man': '于鑫', 'ip': '192.168.9.6'}]
# print(aa[0]['ip'])



#print(get_news())
