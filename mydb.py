#install mysql on you computer
#https
#pip install mysql 
#pip install mysql-connector
#pip install mysql-connector-python 


import mysql.connector


dataBase = mysql.connector.connect(
	host= 'localhost',
	user= 'root',
	password= 'JusT4limbo',
	auth_plugin='mysql_native_password'

	)

print("hello")
#prepare a cursor object 
cursorObject =dataBase.cursor()

#create a data base
cursorObject.execute("CREATE DATABASE base")

print("all done")