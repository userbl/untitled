#!/usr/bin/python3
# coding=UTF-8
import psycopg2


def test():

    try:
        connection = psycopg2.connect(host='192.168.122.229',
                                      user='cat',
                                      password='cat',
                                      database='my_dev' )
        cur = connection.cursor()
        # create one table

        # get result
        cur.execute('SELECT version()')
        results = cur.fetchall()
        print(results)
    finally:

        connection.close()


test()
