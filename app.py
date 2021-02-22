import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


# Create instance of flask
app = Flask(__name__)

# Grab db name
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# Configure connection string
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# Grab secret key
app.secret_key = os.environ.get("SECRET_KEY")

# Create instance of pymongo
mongo = PyMongo(app)


@app.route("/")
def home():
    tasks = mongo.db.department_tasks.find()
    return render_template("index.html", tasks=tasks)
    # just to test then change to index.html and hero image


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check does username exist in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # make sure password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("home"))
            else:
                # invalid password
                flash("Incorrect Username and/or Password")

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    # change to profile or tasks when created
    return render_template("login.html")


@app.route("/control")
def control():
    return render_template("control_panel.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check is username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username Already Exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # flash username and password
        flash(
            "User '{}' Successfully Created!".format(
                request.form.get("username")))
        flash(
            "Please Provide User With The Password: '{}'".format(
                request.form.get("password")))
        return redirect(url_for("control"))

    return render_template("register.html")


@app.route("/profile/<username>", methods=["POST", "GET"])
def profile(username):
    # grab session's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


# Fetch env vars
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# CHANGE DEBUG TO FALSE BEFORE SUBMISSION!!!!
