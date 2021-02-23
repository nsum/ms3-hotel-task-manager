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
    tasks = mongo.db.tasks.find()
    return render_template("index.html", tasks=tasks)
    # just to test then change to index.html and hero image


@app.route("/tasks")
def tasks():
    # we need list(x) to iterate multiple times through tasks
    tasks = list(mongo.db.tasks.find())
    # change above if renamed tasks and put all in one collection
    # add personal_tasks list here
    return render_template(
        "tasks.html", tasks=tasks)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check does username exist in db
        logged_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if logged_user:
            # make sure password matches user input
            if check_password_hash(
                    logged_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                # grab user's department
                session["department"] = logged_user["department"].lower()
                session["first_name"] = logged_user["first_name"].capitalize()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
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

        admin = "on" if request.form.get("admin") else "off"
        mgmt = "on" if request.form.get("mgmt") else "off"

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "admin": admin,
            "mgmt": mgmt
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

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove session cookies
    flash("You have been logged out")
    session.clear()
    return redirect(url_for("login"))


@app.route("/add_task")
def add_task():
    return render_template("add_task.html")


# Fetch env vars
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# CHANGE DEBUG TO FALSE BEFORE SUBMISSION!!!!
