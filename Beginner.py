import sqlite3 as lite
import pandas as pd
#
# conn = lite.connect('getting_started.db')
# cities = (('Las Vegas', 'NV'),
#                     ('Atlanta', 'GA'))
#
# weather = (('Las Vegas', 2013, 'July', 'December'),
#                      ('Atlanta', 2013, 'July', 'January'))
# with conn:
# 	cur = conn.cursor()
# 	cur.executemany("INSERT INTO CITIES VALUES(?,?)",cities)
# 	cur.execute("SELECT * FROM CITIES")
# 	rows = cur.fetchall()
# 	df = pd.DataFrame(rows)
# 	print(df)
# 	cols = [desc[0] for desc in cur.description]
# 	print(cols)
# 	print(cur.connection)
# 	df = pd.DataFrame(rows, columns= cols)
# 	print(df)

data = '''Region,Alcohol,Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''


data = data.splitlines()
print(data)
data = [text.split(',') for text in data]
df = pd.DataFrame(data[1::], columns=data[0])
print(df['Region'])
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

print(df['Tobacco'].mean())
print(df['Alcohol'].mean())


