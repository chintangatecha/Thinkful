import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import collections
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

c = collections.Counter(x)
sumvalues = sum(c.values())

for k,v in c.items():
	print("frequency of {0} is {1}".format(k, float(v) / sumvalues))

plt.boxplot(x)
plt.savefig("boxplot.png")
plt1.hist(x, histtype='bar')
plt1.savefig("Histogram.png")
graph1 = stats.probplot(x, dist="norm", plot=plt)
plt.savefig("qqplot.png")
# plt.boxplot(x)

# plt.savefig("boxplot.png")