import sys
import os
from loguru import logger

from flask import Flask, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from markupsafe import escape
from flask import render_template, request, redirect
from flask_session import Session

from helper import *
from database_connect import database, db

# setting logger to log meassages to stdout
logger.remove()
formatted_messasge = "<white>{time:YYYY-MM-DD HH:mm:ss}</white> | <level>{level: <8}</level> | MODULE:<cyan>{module}</cyan> FUNCTION:<cyan>{function}</cyan> LINE:<cyan>{line}</cyan> --- <level>{message}</level>"
logger.add(sys.stdout, level="DEBUG", format=formatted_messasge)

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# everything related to routing goes here
@app.route('/')
@login_required
def index():
    return render_template('homepage.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    session.clear()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        sql = "SELECT * FROM registered_users WHERE username=%s"
        db.execute(sql, (username,))
        logger.info("Username function runs ok!")
        query_result = db.fetchone()
        print(query_result)
        
        # if the username is valid
        if query_result:
            # if the username and the password is valid
            if check_password_hash(query_result[2], password):
                logger.debug("Successfully validated password")
                session["user_id"] = query_result[0]
                print(session["user_id"])
                return redirect('/')
            # if the username is valid but the password is not valid!
            else:
                logger.error("password validation unsuccessful!")
                return render_template("login.html")

        # if the user is not registered at all
        else:
            logger.error("credential validation unsuccessful!")
            return render_template("login.html")
        
    else:
        return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"] 
            confirmation = request.form["confirmation"]

            if validate_username(username) == True and password == confirmation:
                query = "INSERT INTO registered_users (username, password) VALUES(%s, %s)"
                logger.info("Fails when inserting into the databse!")
                val = (username, generate_password_hash(password),)
                db.execute(query, val)
                database.commit()
                return redirect('/login')
            
            else:
                return render_template('register.html', error = True)

    else:
        return render_template('register.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

