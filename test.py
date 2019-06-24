#!/usr/bin/python

import sys
import mysql.connector

def printTableContents():
	getSql = "select * from books"
	cursor.execute(getSql)

	result = cursor.fetchall();

	for x in result:
		print(x)

args = sys.argv

db = mysql.connector.connect(host="10.101.0.2", user="turnip", passwd="P@ssw0rd", database="root_library")

cursor = db.cursor()

printTableContents()

sql = "insert into books (bookname, aid) values (%s, %s)"
val = (args[1], args[2])

cursor.execute(sql,val)

db.commit()

printTableContents()