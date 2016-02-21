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
from sklearn import tree

X_train, X_test, y_train, y_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)
clf = tree.DecisionTreeClassifier()
clf.fit(X_train, y_train)
pred = clf.predict(X_test)
print "score",clf.score(X_test, y_test)
print "poi predicted in test set", sum([i for i in pred])
print "people in test set",len(X_test)
print "true positives",sum([1 for i,j in zip(pred,y_test) if i == 1 and j == 1])
from sklearn import metrics
print "precision",metrics.precision_score(y_test,pred)
print "recall",metrics.recall_score(y_test,pred)
