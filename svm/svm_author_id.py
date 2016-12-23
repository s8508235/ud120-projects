#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
clf = SVC(C=10000,kernel="rbf")
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)
print sum(pred)
print (accuracy_score(pred,labels_test))
#########################################################
#features_train2 = features_train[:len(features_train)/100]
#labels_train2 = labels_train[:len(labels_train)/100]

#clf = SVC(C=10000,kernel="rbf")
#clf.fit(features_train2, labels_train2)

#pred = clf.predict(features_test)
#print pred[10],pred[26],pred[50]
#print (accuracy_score(pred,labels_test))
