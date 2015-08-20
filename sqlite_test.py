import sqlite3 as lite
import pandas as pd
cities = (('Las Vegas', 'NV'),
                    ('Atlanta', 'GA'))

weather = (('Las Vegas', 2013, 'July', 'December'),
                     ('Atlanta', 2013, 'July', 'January'))

con = lite.connect('getting_started.db')

# Inserting rows by passing tuples to `execute()`
with con:
    cur = con.cursor()
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?)", weather)
    cur.execute("select * from cities")
    rows = cur.fetchall()
    df = pd.DataFrame(rows)
    for row in rows:
    	print(row)