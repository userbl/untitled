#!/usr/bin/python3
# coding=UTF-8
import requests
import bs4
from datetime import datetime, date, timedelta
import pymysql
import calendar
import  time
import  json

root_url='https://toutiao.io/prev/'
index_url = root_url+'2017-03-02'
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch, br',
'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6'}



def get_news():
    response = requests.get('http://get.ishadow.website/',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
    soup = bs4.BeautifulSoup(response.content.decode("utf-8"),"html.parser")
    #print(response.content.decode("utf-8"))
    # b =  [a for a in soup.select('li.gl-item div.p-price strong.J_3356012 i')]

    # b = [a for a in soup.select('div.hover-text ')]
    # for c in b :
        # print(c.i)
        # print(c.gezt_text().strip())

    nn = [a for a in soup.select('div.hover-text')]

    for c3 in nn:
        try :
            # print(c3.find("h4").find("span").get_text())  #.prettify()
            # print(c3.find("h4").find("span").string)
            # print(c3.h4.prettify())
            index =1
            data = {
                "server":"127.0.0.1",
                "server_port":8388,
                "local_port":1080,
                "password":"barfoo!",
                "method": "aes-256-cfb",
                "timeout":6000
            }



            with open('/home/cat/go/path/bin/config.json', 'wt') as f:

                for abc in c3.find_all("h4") :
                    if index ==1 :
                        host = abc.find("span").string
                        print(host)
                        # f.write('host:'+host+'\n')
                        data['server']=host
                    elif index==2 :
                        port = abc.string.split("：")[1]
                        print(port)
                        # f.write('port:'+port+'\n')
                        data['server_port'] = int(port)
                    elif index==3 :
                        pwd = abc.find("span").string
                        print(pwd)
                        # f.write('pwd:'+pwd+'\n')
                        data['password'] = pwd
                    elif index==4 :
                        md = abc.string.split(":")[1]
                        print(md)
                        # f.write('md:'+md+'\n')
                        data['method'] = md

                    index = index+1

                json_str = json.dumps(data)
                f.write(json_str)
                f.close()
                # print(abc)
            # print(c3.prettify())
            # print(c3.prettify())
            # print(c3.h4.span.string)
            # print(c3.h4.next_sibling.span.string)
            # print(c3.h4.next_element)
            # print(c3.find("h4").next_sibling.span.string)
            print("--------------")

            break
        except Exception as e:
            continue
        # print(c3.contents[1].find('strong').find('i'))
        # find_all = c3.find_all('div', class_="p-price")
        # for ccc in find_all :
        #     print(ccc.contents[1])
        # print(c3.get_text().strip())


get_news()