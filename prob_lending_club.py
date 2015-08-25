import collections
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

loadsdata = pd.read_csv("https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv")

loadsdata.dropna(inplace = True)

# loadsdata.boxplot(column='Amount.Funded.By.Investors')

# loadsdata.hist(column = 'Amount.Funded.By.Investors')

# plt.figure()
# graph = stats.probplot(loadsdata['Amount.Funded.By.Investors'], dist="norm", plot=plt)
# plt.show()

loadsdata.boxplot(column = 'Amount.Requested')
loadsdata.hist(column = 'Amount.Requested')
plt.figure()
graph = stats.probplot(loadsdata['Amount.Requested'], dist = "norm", plot = plt)
plt.show()