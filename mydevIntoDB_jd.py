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
    response = requests.get('https://search.jd.com/search?keyword=%E7%A1%AC%E7%9B%98&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E7%A1%AC%E7%9B%98&cid3=683#J_searchWrap',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
    soup = bs4.BeautifulSoup(response.content.decode("utf-8"),"html.parser")
    #print(response.content.decode("utf-8"))
    # b =  [a for a in soup.select('li.gl-item div.p-price strong.J_3356012 i')]
    b = [a for a in soup.select('li[data-sku="3356012"] ')]

    nn = [a for a in soup.select('div[id=J_goodsList] li')]
    # for c in b :
        # print(c.i)
        # print(c.gezt_text().strip())
    for c3 in nn:
        try :
            print(c3.contents[1].contents[1].find("a").attrs['title']+'   '+(c3.contents[1].find('strong').find('i')).string)  #.prettify()
        except Exception as e:
            continue
        # print(c3.contents[1].find('strong').find('i'))
        # find_all = c3.find_all('div', class_="p-price")
        # for ccc in find_all :
        #     print(ccc.contents[1])
        # print(c3.get_text().strip())


get_news()