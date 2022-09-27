## Source of content: https://www.w3schools.com/python/python_mysql_getstarted.asp
import pymysql

# database connection
connection = pymysql.connect(host="localhost", port=3306, user="root", passwd="", database="eseaeme_fund")
cursor = connection.cursor()
# some other statements  with the help of cursor
connection.close()
