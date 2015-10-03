__author__ = 'gatecch'

import collections
from _collections import defaultdict

number_list = [1,1,2,2,2,2,3,3,4,4,5,5,5,5,5,5,6,7,8,8,8,8,9,9,9,9]
dic = collections.defaultdict(int)
for i in number_list:
    dic[i] +=1


print(dic)
