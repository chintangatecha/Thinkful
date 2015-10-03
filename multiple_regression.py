import pandas as pd
import numpy as np
import statsmodels.api as sm

df_adv = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)
X = df_adv[['TV', 'Radio']]
y = df_adv['Sales']
print(df_adv.head())
X = sm.add_constant(X)

import statsmodels.formula.api as smf

# formula: response ~ predictor + predictor
est = smf.ols(formula='Sales ~ TV + Radio', data=df_adv).fit()
estimation = smf.ols(formula = 'Sales ~TV + Radio', data = df_adv).fit()


print(est.summary())