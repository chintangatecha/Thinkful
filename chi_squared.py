from scipy import stats
import collections
import pandas as pd
import matplotlib.pyplot as plt

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace = True)
c = collections.Counter(loansData['Open.CREDIT.Lines'])

list1 = []
for k,v in c.items():
	list1.append(v)

plt.figure()
plt.bar(c.keys(), c.values(), width = 1)
plt.show() 	

#chi, p = stats.chisquare(c.values()) ## does not work
chi, p = stats.chisquare(list1)  #does work
print(chi,p)

# from scipy import stats
# import collections
# import pandas as pd

# # Load the reduced version of the Lending Club Dataset
# loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
# # Drop null rows
# loansData.dropna(inplace=True)

# freq = collections.Counter(loansData['Open.CREDIT.Lines'])