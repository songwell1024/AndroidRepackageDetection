#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: CalculateWeight.py
@time: 2019/3/18 15:01
@desc: 分类方法
'''

import numpy as np
import sklearn.metrics as metrics
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from matplotlib import colors

path = r'C:\Users\Song\Desktop\Data\TrainData\train.txt'
data = np.loadtxt(path)
path = r'C:\Users\Song\Desktop\Data\TestData\test.txt'
test_data = np.loadtxt(path)

# x, y = np.split(data, (2,), axis=1)
# x = x[:, :2]
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, train_size=0.8)

x_train, y_train = np.split(data, (2,), axis=1)
x = x_train[:, :2]
y = y_train
x_test, y_test = np.split(test_data, (2,), axis=1)


# clf = LogisticRegression(penalty='l2', dual=False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver='liblinear', max_iter=100, multi_class='ovr', verbose=0, warm_start=False, n_jobs=1)
# clf = svm.SVC(C=1.0, kernel='linear', decision_function_shape='ovr')
# clf = DecisionTreeClassifier(criterion='entropy', splitter='random', max_depth=7, min_samples_leaf=70, min_samples_split=900, max_features=2, random_state=10)
# clf = RandomForestClassifier(criterion='entropy', oob_score='True', n_estimators=600, max_depth=7, min_samples_leaf=70, min_samples_split=900, max_features=2, random_state=10)
clf = GradientBoostingClassifier(learning_rate=0.01, n_estimators=600, max_depth=7, min_samples_leaf=70, min_samples_split=900, max_features=2, subsample=0.7, random_state=10)
clf.fit(x_train, y_train.ravel())
y_hat = clf.predict(x_test)
######################################
len1 = y_test.__len__()
num = 0
total = 0
for i in range(len1):
    if y_hat[i] != y_test[i] and y_hat[i] == 1:
        num = num + 1
    if y_test[i] == 0:
        total = total +1
print("FPR: ",num /total)
######################################

print('Accuracy:', metrics.accuracy_score(y_test, y_hat))
print('Precision:', metrics.precision_score(y_test, y_hat))
print('Recall:', metrics.recall_score(y_test, y_hat))
print('F-measure:', metrics.f1_score(y_test, y_hat))

mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

x1_min, x1_max = x[:, 0].min(), x[:, 0].max()+0.02
x2_min, x2_max = x[:, 1].min(), x[:, 1].max()+0.02
x1, x2 = np.mgrid[x1_min:x1_max:200j, x2_min:x2_max:200j]
grid_test = np.stack((x1.flat, x2.flat), axis=1)
grid_hat = clf.predict(grid_test)
grid_hat = grid_hat.reshape(x1.shape)

plt.xlim(x1_min, x1_max)
plt.ylim(x2_min, x2_max)
cm_light = mpl.colors.ListedColormap(['#90EE90', '#FFA0A0'])
cm_dark = mpl.colors.ListedColormap(['g', 'r'])
plt.pcolormesh(x1, x2, grid_hat, cmap=cm_light)
plt.scatter(x[:, 0], x[:, 1], c=y.ravel(), s=3, cmap=cm_dark)
plt.xlabel('Image similarity', fontsize=13)
plt.ylabel('Components and permissions similarity ', fontsize=13)
# plt.title('重打包二特征分类', fontsize=15)
plt.show()



# def getFPR(y_test, y_hat):
#     len1 = y_test.__len__()
#     num = 0
#     total = 0
#     for i in range(len1):
#         if y_hat[i] != y_test[i] and y_hat[i] == 1:
#             num = num + 1
#         if y_test[i] == 1:
#             total = total +1
#     return num /total


