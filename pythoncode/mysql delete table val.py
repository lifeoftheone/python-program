import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='takshak1997',database='python')
mycursor=mydb.cursor()
''''sql=" DELETE FROM pychramdata WHERE version=9"
mycursor.execute(sql)
mydb.commit()'''
mycursor.execute('select * from pychramdata')
myresult=mycursor.fetchall()# it basically fetches the whole tuple
for row in myresult:
    print(row)
