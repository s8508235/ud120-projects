#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

### your code goes here
from sklearn import cross_validation
features_train,features_test,labels_train,labels_test = cross_validation.train_test_split(features,labels,random_state=42,test_size=0.3)
from sklearn import tree
'''
clf = tree.DecisionTreeClassifier()
clf.fit(features,labels)
print clf.score(features,labels)
'''

clf = tree.DecisionTreeClassifier()
clf.fit(features_train,labels_train)
print clf.score(features_test,labels_test)
testset = clf.predict(features_test)
print labels_test
print testset
from sklearn.metrics import *
print precision_score(labels_test,testset)
print recall_score(labels_test,testset)
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
print len(predictions)
print precision_score(true_labels,predictions)
print recall_score(true_labels,predictions)
