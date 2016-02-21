#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle
import math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

number_people = len(enron_data)
print("number of people = ", number_people)
number_features = len(enron_data.itervalues().next())
print("number of features per person = ", number_features)
print("---")
number_poi = sum(1 for x in enron_data.values() if x["poi"] == True)
print("number of persons of interest = ", number_poi)
print("---")
print("James Prentice = ", enron_data["PRENTICE JAMES"])
print("---")
print("Wesley Colwell = ", enron_data["COLWELL WESLEY"])
print("---")
print("Jeffrey Skilling = ", enron_data["SKILLING JEFFREY K"])
print("---")
lay_total = enron_data["LAY KENNETH L"]["total_payments"]
skilling_total = enron_data["SKILLING JEFFREY K"]["total_payments"]
fastow_total = enron_data["FASTOW ANDREW S"]["total_payments"]
print("total_payments")
print("lay ", lay_total)
print("skilling ", skilling_total)
print("fastow ", fastow_total)
print("---")
number_salary = sum(1 for x in enron_data.values() if x["salary"] != 'NaN')
print("number of quantified salaries = ", number_salary)
number_email = sum(1 for x in enron_data.values() if x["email_address"] != 'NaN')
print("number of email addresses = ", number_email)
print("---")
number_missing_payments = sum(1 for x in enron_data.values() if x["total_payments"] == 'NaN')
print("number of missing payments = ", number_missing_payments)
print("percentage of missing payments = ", float(number_missing_payments)/number_people)
print("---")
number_missing_payments_poi = sum(1 for x in enron_data.values() if x["total_payments"] == 'Nan' and x["poi"] == True)
print("percentage of missing payments of poi = ", float(number_missing_payments_poi)/number_poi)
