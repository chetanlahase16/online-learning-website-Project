#!C:\Users\cheta\AppData\Roaming\Python\Python310


import cgi


form=cgi.FieldStorage()


first_name=form.getvalue("first Name")
last_name=form.getvalue("last Name")
your_email=form.getvalue("your Email")
password=form.getvalue("password")


import mysql.connector

con=mysql.connector.connect(username='root', password='Chetan@16', host='localhost', database='elearning')
cur=con.cursor()

cur.execute("insert into students values(%s,%s,%s,%s)",(first_name,last_name,your_email,password))
con.commit()

cur.close()
con.close()

print("Connect")