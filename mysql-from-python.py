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
    # run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                        Friends(name char(20), age int, DOB datetime);""")
        # note that the above will still display a warning (not error)
        # if the table already exists
finally:
    # close the connection
    connection.close()
