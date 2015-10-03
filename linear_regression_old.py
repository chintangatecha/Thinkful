import pandas as pd
import matplotlib.pyplot as plt

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
print(loansData[0:5])
#loansData.dropna(replace= True)
#print(loansData['Amount.Requested'][0:5])

# list1 = [1,2,2,3,4,15,5,1,2,4,2,4,4,3,6]
# ##Example of lambda funciton 
# #g= filter(lambda x:x%2,list1)
# list2 = list(filter(lambda x: x % 3 == 0, list1))

# print("insert {0}".format(list2))
# for i in loansData['Interest.Rate']:
# 	print(i.replace("%", ""))
#print(loansData['Interest.Rate'].translate(None, '%'))
#loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x:x.replace("%",""))
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x:x.replace(" month",""))
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
#xy = loansData['FICO.Score'].map(lambda x: str(x))


#remove "month" at the end of loan length and convert to integer

#create a new column called Fico Score with lower limit value
loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']]
plt.figure()
p = loansData['FICO.Score'].hist()
plt.show()

#print(loansData['FICO.Range'])
#print(type(loansData['FICO.Score'][1]))
#a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')




