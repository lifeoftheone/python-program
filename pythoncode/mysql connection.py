import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='takshak1997')
print(mydb)
if (mydb):
    print("connected")
else:
    print("not connected")