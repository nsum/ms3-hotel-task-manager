import os
import datetime
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from functools import wraps
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


# Restricts access to unlogged users
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Throws and error is user not logged in. Try to fix
        # NEEDS A FIX
        if session["user"]:
            return f(*args, **kwargs)
        return redirect(url_for('login'))
    return decorated_function


# Allows admins to access certain pages
def admin_access(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session["is_admin"] == "off":
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function


# Allows management to access certain pages
def mgmt_access(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session["is_mgmt"] == "off":
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
@app.route("/home")
def home():
    tasks = mongo.db.tasks.find()
    return render_template("index.html", tasks=tasks)
    # just to test then change to index.html and hero image


# Shows shared and user's departments tasks
@app.route("/tasks")
@login_required
def tasks():
    # we need list(x) to iterate multiple times through tasks
    tasks = list(mongo.db.tasks.find())
    return render_template(
        "tasks.html", tasks=tasks)


@app.route("/all_tasks")
@login_required
def all_tasks():
    # Checks if user in session is mgmt or admin
    if session["is_admin"] or session["is_mgmt"] == "on":
        tasks = list(mongo.db.tasks.find())
        # pull list of departments
        departments = list(mongo.db.departments.find())
        return render_template(
            "all_tasks.html", tasks=tasks, departments=departments)
    else:
        return redirect(url_for('/'))


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
                session["last_name"] = logged_user["last_name"].capitalize()
                session["is_admin"] = logged_user["admin"]
                session["is_mgmt"] = logged_user["mgmt"]
                flash("Welcome, {}".format(session["first_name"]))
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
@login_required
@admin_access
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
            "first_name": request.form.get("first_name").capitalize(),
            "last_name": request.form.get("last_name").capitalize(),
            "department": request.form.get("department"),
            "super_user": "off",
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

    # pull list of departments
    departments = mongo.db.departments.find()
    return render_template("register.html", departments=departments)


@app.route("/profile/<username>", methods=["POST", "GET"])
def profile(username):
    # grab session's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    tasks = list(mongo.db.personal_tasks.find())

    if session["user"]:
        return render_template("profile.html", tasks=tasks, username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Remove session cookies
    flash("You have been logged out")
    session.clear()
    return redirect(url_for("login"))


@app.route("/add_dept_task", methods=["GET", "POST"])
def add_dept_task():
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        # Grabs and formats current date for "created on"
        current_date = datetime.date.today().strftime('%d/%b/%Y')
        # Used to insert task creator's full name in "created by"
        creator = session["first_name"] + " " + session["last_name"]

        task = {
            "department": request.form.get("department_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": creator,
            "created_on": current_date
        }

        mongo.db.tasks.insert_one(task)
        flash("Department Task Successfully Added!")
        return redirect(url_for('tasks'))

    # pull list of departments
    departments = mongo.db.departments.find()
    return render_template("add_dept_task.html", departments=departments)


# Fetch env vars
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# CHANGE DEBUG TO FALSE BEFORE SUBMISSION!!!!
