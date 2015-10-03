__author__ = 'gatecch'

import requests
import pandas as pd
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import sqlite3
import time
import collections
from dateutil.parser import parse

r = requests.get("http://www.citibikenyc.com/stations/json")
uniquekeys = []
for stations in r.json()['stationBeanList']:
    for stationkey in stations.keys():
        if stationkey not in uniquekeys:
            uniquekeys.append(stationkey)

con = sqlite3.connect('citi_bike.db')
cur = con.cursor()
with con:
    cur.execute("drop table IF EXISTS citibike")
    cur.execute("CREATE TABLE citibike (id INT PRIMARY KEY, totalDocks INT, city TEXT, altitude INT, stAddress2 TEXT, longitude NUMERIC, postalCode TEXT, testStation TEXT, stAddress1 TEXT, stationName TEXT, landMark TEXT, latitude NUMERIC, location TEXT )")

sql = "INSERT INTO citibike (id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"

with con:
    for station in r.json()['stationBeanList']:
        cur.execute(sql,(station['id'],station['totalDocks'],station['city'],station['altitude'],station['stAddress2'],station['longitude'],station['postalCode'],station['testStation'],station['stAddress1'],station['stationName'],station['landMark'],station['latitude'],station['location']))

station_ids = []
for a in station['id']:
    station_ids.append(a)


station_ids = ['_' + str(x) + ' INT' for x in station_ids]
with con:
    cur.execute("CREATE TABLE available_bikes ( execution_time INT, " +  ", ".join(station_ids) + ");")


exec_time = parse(r.json()['executionTime'])
with con:
    cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%s'),))

id_bikes = collections.defaultdict(int) #defaultdict to store available bikes by station


for station in r.json()['stationBeanList']:
    id_bikes[station['id']] = station['availableBikes']


with con:
    for k, v in id_bikes.iteritems():
        cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + exec_time.strftime('%s') + ";")