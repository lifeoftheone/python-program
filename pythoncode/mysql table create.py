import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='takshak1997',database='python')
mycursor=mydb.cursor()
''''mycursor.execute('create table pychramdata(idename varchar(20), version int(20))')'''
mycursor.execute('show tables')
for tb in mycursor:
    print(tb)