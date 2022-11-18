
from flask import session, redirect, render_template
from database_connect import database, db

def validate_username(username):
    db.execute('SELECT * FROM registered_users WHERE username=%s', (username,))
    print(db.fetchall())
    if len(db.fetchall()) == 0:
        return True
    else:
        return False

def login_required(func):
    def check_session(*args, **kwargs):
        if session.get('user_id') is None:
            return redirect ("/login")
        return func(*args, **kwargs)
    return check_session

        
