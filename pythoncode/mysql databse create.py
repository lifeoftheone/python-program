import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='takshak1997')
mycursor=mydb.cursor()
''''mycursor.execute('create database python')'''
mycursor.execute('show databases')
for db in mycursor:
    print(db)
