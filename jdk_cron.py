#!/usr/bin/python3
# coding=UTF-8
import requests
import bs4
from datetime import datetime, date, timedelta
import pymysql
import calendar
import  time
import string

dir  = "/home/cat/PycharmProjects/untitled/"

def grab_infoq() :
    response = requests.get('http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html', headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'},
                            stream=False)
    # print(response.content)
    s = str(response.content, encoding="utf-8")
    # print(s)
    # for line in s :
    #     print(line)
    # Write chunks of text data
    with open(dir+'somefile.txt', 'wt') as f:
        f.write(s)

    import re
    import json
    datepat = re.compile(r'.{1,}-linux-x64.tar.gz')
    p2 = re.compile(r'jdk-.{1,5}-linux-x64.tar.gz')


    # pattern = re.compile(r'world')
    # # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
    # match = pattern.match('hello world!')
    # findall = pattern.findall('hello world!')
    # print(findall)
    # if match:
    #     # 使用Match获得分组信息
    #     print(match.group())




    with open(dir+'somefile.txt', 'rt') as f:
        for line in f:
            # print(line)
            mm =  re.match(r'.{1,}-linux-x64.tar.gz',line) #match  是从字符串开始处匹配
            if mm :
                # print(m)
                # print('find')
                # print(line)
                # print("gg:  "+mm.group())
                # mmm = re.match(r'\{.{1,}\}',line)
                # json_str = line[line.find("=")+1:(len(line)-2)]
                json_str = line[line.find("=")+1:line.find(";")]
                # print(json_str)
                data = json.loads(json_str)

                # print(json_str)
                print(data['filepath'])
                print("MD5: "+data['MD5'])
                print("SHA256: "+data['SHA256'])

                with open(dir+'jdk_md5.txt', 'wt') as f:
                    f.write(data['MD5'])
                with open(dir+'jdk_sha256.txt', 'wt') as f:
                    f.write(data['SHA256'])


                m4 = p2.findall(line)  #match  是从字符串开始处匹配
                file_name = m4[0]
                if m4 :
                    # print("000000000000>>>>>>>>>>>")
                    print(file_name)
                if  not is_file_exists(file_name) :
                    print("download file ... ")
                    grab_file(data['filepath'], file_name)

                else :
                    print("file already exists!")


                # print(line)
                # if mmm :
                #     print(mmm)
                #     print("mmm")

            # else :
            #     print("don't find")

    grab_data = []
    # response = requests.get('http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
    # soup = bs4.BeautifulSoup(response.content.decode("utf-8"),"html.parser")
    #
    # #/home/cat/dd  grep '\-linux\-x64\-demos.tar.gz' test.txt

    # print(string(soup.strings))
    # news =  [a for a in soup.select('tr td a')]
    #
    # href_ = news[0].attrs.get('href')
    # strip = news[0].get_text().strip()
    # print(strip+" "+href_)
    #
    # real_url =href_[href_.find("url=")+4:len(href_)]
    #
    # print(real_url)
    # grab_file(real_url)
    # if len(strip) > 1 :
    #     grab_data.append((strip, href_, str(datetime.today())[0:10], 'infoq'))

    return grab_data

import os

import hashlib



def is_file_exists(file_name) :

    file_name=dir+file_name

    if os.path.exists(file_name) :

        read = open(file_name, 'rb').read()

        file_md5 = hashlib.md5(read).hexdigest()
        # split_ = (os.popen("md5sum " + file_name).read().split(" ")[0])
        # file_md5 = split_
        # print("md5sum:  " + split_)

        file_sha256 = hashlib.sha256(read).hexdigest()
        md5 = ""
        sha256 = ""
        if os.path.exists(file_name) :
            with open(dir+'jdk_md5.txt', 'rt') as f:
                for line in f:
                    md5 = line
                    # print(line)
            with open(dir+'jdk_sha256.txt', 'rt') as f:
                for line in f:
                    sha256 = line
                    # print(line)

        print("md5:  "+md5)
        print("f_md5:"+file_md5)
        print("sha256:  "+sha256)
        print("f_sha256:"+sha256)

        if file_md5 == md5 and file_sha256 == sha256 :
            return True
        else:
            return False
    else :
        return False



def grab_file(file_url,file_name) :
    # page_url="https://iiio.io/download/20170709/"
    # print("url: " + file_url)


    grab_data = []

    jar = requests.cookies.RequestsCookieJar()
    jar.set('oraclelicense', 'accept-securebackup-cookie', domain='.oracle.com', path='/')
    # url = 'http://httpbin.org/cookies'
    # r = requests.get(url, cookies=jar)

    response = requests.get(file_url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'},
                            stream=True, cookies=jar)
    print(response.headers)
    length_ = response.headers['Content-Length']
    print(length_)
    # fname = response.headers['Content-Disposition'].split(';', 1)[1].split('=', 1)[1].strip('"')
    # print("--------------------->"+fname)
    print(file_name)
    f = open(dir+file_name, "wb")
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


from datetime import datetime


data = grab_infoq()

import os
os.system("~/jdk-update.sh")