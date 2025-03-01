# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 20:25:50 2023

@author: KIIT
"""

import pymongo
client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb=client['About_College']
information=mydb.collegeinformation
all_documents=information.find()

for item in all_documents:
    print(item)
    

client.close()