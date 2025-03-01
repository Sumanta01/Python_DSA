# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 20:10:02 2023

@author: KIIT
"""
import mysql.connector

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="kiit",
    database="my_db" 
    )

cursor=connection.cursor()
query="select * from sumanta"
cursor.execute(query)
for i in cursor.fetchall():
    print(i)
    
cursor.close()
connection.close()
 

    