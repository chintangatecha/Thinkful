import collections

testlist = [1, 4, 5, 6, 9, 9, 9]

c = collections.Counter(testlist)

print(c)
print(c.values())
print(c.keys())
print(c.items())
count_sum = sum(c.values())
for k,v in c.items():
	print("the frequency of numbre" + str(k) + " is " + str(float(v)/count_sum))

import matplotlib.pyplot as plt
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
plt.boxplot(x)
plt.savefig("boxplot.png")
# calculate the number of instances in the list
# count_sum = sum(c.values())
# print(count_sum)
# count_sum1 = sum(c.keys())
# print(count_sum1)

# for k,v in c.items():
#   print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))


