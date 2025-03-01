# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 17:10:30 2023

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
#CREATE
#query="create table Sumanta(id int,name varchar(100),Progm_Language varchar(60),country varchar(50)")

#INSERT
#insert_query="insert into sumanta(id,name,Progm_Language,country) values(%s,%s,%s,%s)"
#data_to_insert=(6,"Luee","Swift","Ireland")
#cursor.execute(insert_query,data_to_insert)
#connection.commit()

#UPDATE
update_query="update sumanta set name=%s,Progm_Language=%s,country=%s where id=%s"
new_values=("Copper","C#","Japan",6)
cursor.execute(update_query,new_values)
connection.commit()
select_query = "SELECT * FROM sumanta WHERE id = %s"
cursor.execute(select_query, (6,))
updated_row = cursor.fetchone()
print("Updated Row:", updated_row)

#DELETE
delete_query="delete from sumanta where id =%s"
id_to_delete=6
cursor.execute(delete_query,(id_to_delete,))
connection.commit()

query="select * from sumanta"
cursor.execute(query)


for i in cursor.fetchall():
    print(i)
    
cursor.close()
connection.close()