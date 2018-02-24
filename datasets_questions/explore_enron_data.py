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

#print len(enron_data)
print len(enron_data.keys())
print len(enron_data.values()[0])
count = 0
for person_name in enron_data.keys():
    if enron_data[person_name]["poi"]==1:
        count = count + 1
print count


enron_poi = open("../final_project/poi_names.txt","r")
lines = enron_poi.readlines()

print len(lines[2:])
enron_poi.close()
print "James value", enron_data['PRENTICE JAMES']['total_stock_value']

print "Count of emails",enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print "Total stock options",enron_data['SKILLING JEFFREY K']['exercised_stock_options']



count_salary = 0
count_email = 0
for key in enron_data.keys():
    if enron_data[key]['salary'] != 'NaN' and enron_data[key]['poi'] == True:
        count_salary+=1
    if enron_data[key]['email_address'] != 'NaN':
        count_email+=1
print count_salary
print count_email
print float(count_salary)/len(enron_data.keys())
