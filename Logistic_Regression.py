import pandas as pd
import numpy as np
import collections
import matplotlib.pyplot as plt
import statsmodels.api as sm

loansdata = pd.read_csv("https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv")
loansdata['Interest.Rate'] = loansdata['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loansdata['FICO.Score'] = [int(val.split('-')[0]) for val in loansdata['FICO.Range']]
loansdata['Loan.Length'] = loansdata['Loan.Length'].map(lambda x:x.replace(" month",""))

loansdata['IR_TF'] = loansdata['Interest.Rate'].map(lambda x: 1 if x >0.12 else 0)
loansdata['intercept'] = 1.0
ind_vars = ['intercept','FICO.Score', 'Amount.Requested']
logit = sm.Logit(loansdata['IR_TF'], loansdata[ind_vars])
result = logit.fit()
coeff = result.params
print(coeff)
def logistic_function(featurelist, coef):
	xb = np.dot(featurelist, coef)
	return 1.0/(1.0 + np.exp(-xb))
logistic_function(ind_vars,coeff)


# loansdata['IR_TF'] = loansdata['Interest.Rate'] <= 0.12

# loansdata['Intercept'] = 1.0

# ind_vars = ['Intercept','FICO.Score', 'Amount.Requested']

# logit = sm.Logit(loansdata['IR_TF'], loansdata[ind_vars])

# result = logit.fit()
# coeff = result.params
# print(coeff)

# def logistic_function(feature_vector, coef):
#     xb = np.dot(feature_vector, coef)
#     return 1.0/(1.0 + np.exp(-xb))

# # Possible to obtain 10,000 dollar loan with a credit score of 700?
# print 'p=', logistic_function([1.0, 720, 10000], coeff)
# print 'Probablity is above 70% so you will most likely get the loan'

#interest_rate = −60.125 + 0.087423(FicoScore) − 0.000174(LoanAmount)
#p(x) = 1/(1 + e^(intercept + 0.087423(FicoScore) − 0.000174(LoanAmount))


#interest_rate = b + a1(FICOScore) + a2(LoanAmount)