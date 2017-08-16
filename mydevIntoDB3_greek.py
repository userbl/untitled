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



def get_news_greek():
    # 格式化成2016-03-20 11:45:39形式
    # today = date_str    # '2017-03-01'#time.strftime("%Y-%m-%d", time.localtime())
    # print(today)
    response = requests.get('http://geek.csdn.net/service/news/get_news_list?jsonpcallback=jQuery203017309250190335468_1489126260747&username=userbl&from=-&size=20&type=HackCount&_=148912626074',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
    soup = bs4.BeautifulSoup(response.content.decode("utf-8"),"html.parser")
    #print(response.content.decode("utf-8"))
    # soup = bs4.BeautifulSoup(response["content_html"])
    # print(str(soup)[42:len(str(soup))-1])

    import json

    newDictionary = json.loads(str(soup)[42:len(str(soup))-1])
    print(newDictionary)
    return [a for a in soup.select('div.geek_list span.tracking-ad a')]
    #print(links)






def grab_greek() :
    year = datetime.today().year
    month = datetime.today().month
    day = datetime.today().day

    grab_data = []

    news = get_news_greek()
    for a in news:
        # print('     ' + a.get_text())
        # href_ = 'http://www.infoq.com' + a.attrs.get('href')
        grab_data.append((a.get_text().strip(), a.attrs.get('href'), str(datetime.today())[0:10], 'infoq'))
        # print(grab_data)

    return grab_data


#
data = grab_greek()
print(data)
for a in data :
    print(a[0])
# saved_data = saveToDB(data)
# fq_user = queryTargetFQUser()
# print(fq_user)
# sendTo_FeiQiu(saved_data,fq_user)

# aa =[{'ip_man': '白龙', 'ip': '192.168.9.64'}, {'ip_man': '于鑫', 'ip': '192.168.9.6'}]
# print(aa[0]['ip'])



#print(get_news())
