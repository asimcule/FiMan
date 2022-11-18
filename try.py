import os

db_username = os.environ.get("db_username")
db_password = os.environ.get("db_password")
print(db_username, db_password)