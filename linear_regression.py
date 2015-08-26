import pandas as pd
import collections
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

##cleaning thd data
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x:x.replace(" month",""))
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']]

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
FICO = loansData['FICO.Score']
y = np.matrix(intrate).transpose()
x1 = np.matrix(FICO).transpose()
x2 = np.matrix(loanamt).transpose()
# print(x1)
# print(y)
# print(x2)
x = np.column_stack([x1,x2])
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()
print(f.summary())



