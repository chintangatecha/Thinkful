__author__ = 'Amit'
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data/ideal_weight.csv")
#data['sex'] = data['sex'].map(lambda  x: x.replace("'",""))
print(data.columns)
data.columns = data.columns.str.replace("'","")
data['sex'] = data['sex'].str.replace("'","")

