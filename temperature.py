__author__ = 'gatecch'

import requests
import pandas as pd
import collections
import sqlite3
import datetime
import time

api_key = 'b10c30be44b90e18d482d7fff9e63085/'
url = 'https://api.forecast.io/forecast/' + api_key
cities = { "Atlanta": '33.762909,-84.422675',
            "Austin": '30.303936,-97.754355',
            "Boston": '42.331960,-71.020173',
            "Chicago": '41.837551,-87.681844',
            "Cleveland": '41.478462,-81.679435'
        }
URL_list = []
end_date = datetime.datetime.now()
con = sqlite3.connect('weather.db')
cur = con.cursor()
cities.keys()
with con:
    cur.execute("drop table IF EXISTS daily_temp")
    cur.execute('CREATE TABLE daily_temp ( day_of_reading INT, Atlanta REAL, Austin REAL, Boston REAL, Chicago REAL, Cleveland REAL);') #use your own city names instead of city1...

query_date = end_date - datetime.timedelta(days=30) #the current value being processed
with con:
    while query_date < end_date:
        cur.execute("INSERT INTO daily_temp(day_of_reading) VALUES (?)", (int(query_date.strftime('%s')),))
        query_date += datetime.timedelta(days=1)