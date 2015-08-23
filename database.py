import pandas as pd
import sqlite3 as lite

connection = lite.connect('getting_started.db')
weather  = (  
  ('New York City'   ,2013,    'July'        ,'January'     ,62),
  ('Boston'        ,2013,    'July'        ,'January'     ,59),
  ('Chicago'       ,2013,    'July'        ,'January'     ,59),
  ('Miami'        ,2013,    'August'      ,'January'     ,84),
  ('Dallas'         ,2013,    'July'        ,'January'     ,77),
  ('Seattle'        ,2013,    'July'        ,'January'     ,61),
  ('Portland'      ,2013,    'July'        ,'December'    ,63),
  ('San Francisco'   ,2013,    'September'   ,'December'    ,64),
  ('Los Angeles'    ,2013,    'September'   ,'December'    ,75))

cities = (('New York City', 'NY'),
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA'))

with connection:
	cursor = connection.cursor()
	cursor.execute("DROP table IF EXISTS cities")
	cursor.execute("DROP table IF EXISTS weather")
	cursor.execute("CREATE table cities(name text,state text)")
	cursor.execute("CREATE table weather(city text, year integer, warm_month text, cold_month text, average_high integer)")
	cursor.executemany("INSERT into cities values(?,?)",cities)
	cursor.executemany("INSERT into weather values(?,?,?,?,?)",weather)
	cursor.execute("SELECT name, state, warm_month, AVG(average_high) FROM cities inner join weather on name = city GROUP BY warm_month,name,city order by AVG(average_high) desc ;")
	data = cursor.fetchall()
	df = pd.DataFrame(data)
	cols = [desc[0] for desc in cursor.description]
	df = pd.DataFrame(data, columns = cols)
	print(df['name'][0])
	for row in range(len(df)):
		print("the cities that are the warmest in {0} are {1} of {2}".format(df['warm_month'][row],df['name'][row],df['state'][row]))
	#print("the cities that are the warmest in {0} are {1}".format(df['warm_month'][0],df['name'][0]))