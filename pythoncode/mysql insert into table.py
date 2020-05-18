import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='takshak1997',database='python')
mycursor=mydb.cursor()
sqlform="insert into pychramdata (idename,version) values(%s,%s)"
pychramdataa=[("pycharm",3),('jupiter',8),('spider',9)]
mycursor.executemany(sqlform,pychramdataa)
mydb.commit()