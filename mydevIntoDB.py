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


def saveToDB():
    pass



connection = pymysql.connect(host='192.168.11.185',
                                 user='root',
                                 password='abc',
                                 db='my_dev',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)






# try:
year =datetime.today().year
month = datetime.today().month
day = datetime.today().day

for d in date_range(datetime(2014, 9, 27), datetime(year,month,day),
                    timedelta(hours=24)):
# for d in date_range(datetime(year, month, day-1), datetime(year,month,day+1),
#                     timedelta(hours=24)):
    # print(d)
    d_ = str(d)[0:10]
    # print(d_)
    date_str = d_#"2014-09-27"
    news = get_news(date_str)
    print(d_+' '+str(len(news)))
    for a in news:
        # print('https://toutiao.io'+a.get_text())
        # print(a.get_text() + '  ' + 'https://toutiao.io' + a.attrs.get('href'))
        print('     ' + a.get_text())
        try:
            href_ = root_url + a.attrs.get('href')
            with connection.cursor() as cursor:
                # Read a single record
                sql = 'SELECT count(1) cc FROM tech_article WHERE title=%s and url=%s and date_str=%s '
                cursor.execute(sql, (a.get_text(), href_, d_))
                result = cursor.fetchone()
                # print('insert:' + result) #Can't convert 'dict' object to str implicitly
                # print(result['cc'])
            if result['cc'] == 0 :
                with connection.cursor() as cursor:
                    # Create a new record
                    sql = "INSERT INTO `tech_article` (`title`, `url`,`date_str`,`where_come_from`) VALUES (%s, %s,%s,%s)"
                    result = cursor.execute(sql, (a.get_text(), href_, d_, 'develop_first'))
                    print("------------------------insert")
                    # print('insert:' + result)
        finally:
            pass
            #connection.close()
connection.close()

# except Exception as e:
#     print(e)





#print(get_news())
