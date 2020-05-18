import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='takshak1997',database='python')
mycursor=mydb.cursor()
mycursor.execute('select * from pychramdata')
''''myresult=mycursor.fetchone()'''''# fetchchone fetch only single value from the tuple
myresult=mycursor.fetchall()# it basically fetches the whole tuple
for row in myresult:
    print(row)