import sqlite3 as lite
cities = (('Las Vegas', 'NV'),
                    ('Atlanta', 'GA'))

weather = (('Las Vegas', 2013, 'July', 'December'),
                     ('Atlanta', 2013, 'July', 'January'))

conn = lite.connect('getting_started.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO CITIES VALUES(?,?)",cities)
    cur.execute("INSERT INTO WEATHER VALUES(?,?,?,?)",weather)

