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
        rows = cursor.executemany("DELETE FROM Friends WHERE name = %s;",
                                  ['bob', 'jim'])
        connection.commit()
finally:
    connection.close()
