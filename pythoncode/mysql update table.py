import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='takshak1997',database='python')
mycursor=mydb.cursor()
sql="UPDATE pychramdata SET version=7 WHERE idename='pycharm'"
mycursor.execute(sql)
mydb.commit()