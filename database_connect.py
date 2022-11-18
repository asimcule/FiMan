import os
import mysql.connector
from mysql.connector import errorcode

#establishing connection to the finance.db database and accessing the cursor for the database
db_username = os.environ.get("db_username")
db_password = os.environ.get("db_password")
try:
    database = mysql.connector.connect(
        user = db_username,
        password = db_password,
        host = '127.0.0.1',
        database =' final_project'
    )

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your credentials!")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist!")
    
    else:
        print(err)

db = database.cursor()