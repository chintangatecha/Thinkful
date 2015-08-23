import pandas as pd
import scipy as scipy

data = '''Region, Alcohol, Tobacco
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
data = [i.split(', ') for i in data]
column_names = data[0]
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)
df['Alcohol'] = df['Alcohol'].astype('float')
df['Tobacco'] = df['Tobacco'].astype('float')
df['Alcohol'].mean()
df['Alcohol'].median()
df['Alcohol']

def calculatemean(list1):
	for i in list1:
		print("Mean of {0} is {1}".format(i,df[i].mean()))
		#print("Mode of {0} is {1}".format(i,stats.mode(df[i])))
		print("median of {0} is {1}".format(i,df[i].median()))
		print("standard deviation of {0} is {1}".format(i,df[i].std()))
		print("Variance of {0} is {1}".format(i,df[i].var()))
		print("Range of {0} is {1}".format(i,max(df[i]) - min(df[i])))
list2 = ['Tobacco','Alcohol']
#print(stats.mode(df['Tobacco']) )   name 'stats' is not defined.
calculatemean(list2)
