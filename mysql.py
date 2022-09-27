# Connecting to a db (XAMPP)
""" Sources of content: 
1. https://www.w3schools.com/python/python_mysql_getstarted.asp
2. https://www.tutorialslides.com/how-to-connect-and-create-database-on-mysql-phpmyadmin-using-python/
"""
import pymysql
import pymysql.cursors

connection = pymysql.connect(host="localhost", port=3306, user="root", passwd="", database="eseaeme_fund")
cursor = connection.cursor()

# Creating a table

"""Query for creating table"""
ArtistTableSql = """CREATE TABLE Artists(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
NAME  CHAR(20) NOT NULL,
TRACK CHAR(10))"""

cursor.execute(ArtistTableSql)
connection.close()

# Insert

insert1 = "INSERT INTO Artists(NAME, TRACK) VALUES('Towang', 'Jazz' );"# queries for inserting values
insert2 = "INSERT INTO Artists(NAME, TRACK) VALUES('Sadduz', 'Rock' );"
"""executing the quires"""
cursor.execute(insert1)
cursor.execute(insert2)

connection.commit() #commiting the connection then closing it.
connection.close()

# Select
retrive = "Select * from Artists;"# queries for retrievint all rows

cursor.execute(retrive)#executing the quires
rows = cursor.fetchall()
for row in rows:
   print(row)

connection.commit() #commiting the connection then closing it.
connection.close()

# Update
updateSql = "UPDATE  Artists SET NAME= 'Tauwang'  WHERE ID = '1' ;"
cursor.execute(updateSql)

# Delete
deleteSql = "DELETE FROM Artists WHERE ID = '1'; "
cursor.execute(deleteSql )

# Drop table
dropSql = "DROP TABLE IF EXISTS Artists;"
cursor.execute(dropSql)