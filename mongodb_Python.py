# -*- coding: utf-8 -*-
"""
Created on Fri May 12 00:28:05 2023

@author: KIIT
"""

import pymongo
client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb=client['About_College']
information=mydb.collegeinformation
record=[{
        
        'Kiit':'Patia',
        'Soa':'khandagir',
        'Silicon':'infocity'
        
        },{'Outr': "Kalinga Nagar",
           'Utkal ': 'VaniVihar',
           'Xim':'Fortune Tower'
           },
           {
               'Revenshaw':'Cuttack',
               'Igit':'Dhenkanal',
               'Giet':'Patrapada'
               
               }]

information.insert_many(record)

