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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
'''
cnt = 0
for i in enron_data.values():
    if i['poi'] == True:
        cnt+=1
    print i
print cnt
'''
'''
poi_text = '../final_project/poi_names.txt'
poi_names = open(poi_text, 'r')
fr = poi_names.readlines()
print len(fr[2:])
poi_names.close()
'''
'''
names = ['SKILLING JEFFREY K', 'FASTOW ANDREW S', 'LAY KENNETH L']
names_payments = {name:enron_data[name]['total_payments'] for name in names}
print names_payments
'''
cnt=0
for i in enron_data.values():
    if(i['email_address']!='NaN'):
        cnt+=1
print cnt
