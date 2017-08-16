#!/usr/bin/python3
# coding=UTF-8
import psycopg2


def t():
    connection = None
    try:
        connection = psycopg2.connect(host='192.168.122.229',
                                      user='cat',
                                      password='cat',
                                      database='my_dev' )
        cur = connection.cursor()
        # create one table

        # get result
        cur.execute('SELECT title,url,date_str from tech_article ORDER BY date_str desc ,opr_date desc limit 1000 ')
        results = cur.fetchall()
        print(results)
    finally:

        connection.close()


t()
