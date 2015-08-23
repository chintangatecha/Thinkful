import sqlite3 as lite
import pandas as pd

cities = (('Las Vegas', 'NV'),
                    ('Atlanta', 'GA'))

weather = (('Las Vegas', 2013, 'July', 'December'),
                     ('Atlanta', 2013, 'July', 'January'))

con = lite.connect('getting_started.db')

with con:
	cursor = con.cursor()
	cursor.executemany("INSERT into cities values(?,?)",cities)
	cursor.execute("select * from cities")
	data = cursor.fetchall()
	df = pd.DataFrame(data)
	print (df)
	print(df.head())
	print(cursor.description)
	cols = [desc[0] for desc in cursor.description]
	df = pd.DataFrame(data, columns = cols)
	print(df)