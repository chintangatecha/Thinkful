import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import pandas as pd


df = pd.read_csv('http://statweb.stanford.edu/~tibs/ElemStatLearn/datasets/SAheart.data', index_col=0)

# copy data and separate predictors and response
X = df.copy()
y = X.pop('chd')

df.head()
print(y.head())

print(df['chd'].groupby(X.famhist).mean())
print(df.famhist.head())
print(pd.Categorical(df.famhist).labels)
# plt.scatter(df.logincome, df.mdvis, alpha=0.3)
# plt.xlabel('Log income')
# plt.ylabel('Number of visits')

# income_linspace = np.linspace(df.logincome.min(), df.logincome.max(), 100)

# est = smf.ols(formula='mdvis ~ logincome + hlthp', data=df).fit()

# plt.plot(income_linspace, est.params[0] + est.params[1] * income_linspace + est.params[2] * 0, 'r')
# plt.plot(income_linspace, est.params[0] + est.params[1] * income_linspace + est.params[2] * 1, 'g')
# short_summary(est)