import numpy as np
from sklearn import cross_validation
from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()
print(iris.data.shape)
print(iris.target.shape)

## now lets divide the datasets so that we can use only the partial test and training datasets

X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(iris.data, iris.target, test_size = 0.4, random_state = 0)

print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

clf = svm.SVC(kernel='linear', C=1).fit(X_train, Y_train)
score = clf.score(X_test, Y_test)
print(score)