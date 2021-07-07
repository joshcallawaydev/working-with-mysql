import os
import datetime
import pymysql

username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'bob';")
        connection.commit()
finally:
    connection.close()
