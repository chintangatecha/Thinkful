__author__ = 'gatecch'

import sqlite3 as lite
import sys

con = lite.connect("weather.db")
cur = con.cursor()

with con:
    cur.EXECUTE("select")



