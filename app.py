import os
import datetime
from datetime import timedelta
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


# Logout user after specified time of Inactivity
@app.before_request
def set_session_timeout():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=15)


# Restricts access to unlogged users
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Throws and error is user not logged in. Try to fix
        # NEEDS A FIX
        is_logged = session.get("user")
        if is_logged is None:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
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
    # Just to test then change to index.html and hero image


# Shows shared and user's departments tasks
@app.route("/tasks")
@login_required
def tasks():
    # We need list(x) to iterate multiple times through tasks
    tasks = list(mongo.db.tasks.find())
    # Grab users department
    departments = list(mongo.db.departments.find())
    return render_template(
        "tasks.html", tasks=tasks, departments=departments)


@app.route("/all_tasks")
@login_required
@mgmt_access
def all_tasks():
    tasks = list(mongo.db.tasks.find())
    # Pull list of departments
    departments = list(mongo.db.departments.find())
    return render_template(
        "all_tasks.html", tasks=tasks, departments=departments)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check does username exist in db
        logged_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if logged_user:
            # Make sure password matches user input
            if check_password_hash(
                    logged_user["password"], request.form.get("password")):
                # Grab session username
                session["user"] = request.form.get("username").lower()
                session["department"] = logged_user["department"].lower()
                # Grab other sesssion user's info
                session["first_name"] = logged_user["first_name"].capitalize()
                session["last_name"] = logged_user["last_name"].capitalize()
                session["is_admin"] = logged_user["admin"]
                session["is_mgmt"] = logged_user["mgmt"]

                flash("Welcome, {}".format(session["first_name"]))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # Invalid password
                flash("Incorrect Username and/or Password")
        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    # Change to profile or tasks when created
    return render_template("login.html")


# Admin & mgmt control panel
@app.route("/control")
@login_required
@mgmt_access
def control():
    return render_template("control_panel.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check is username exists
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

        # Flash username and password
        flash(
            "User '{}' Successfully Created!".format(
                request.form.get("username")))
        flash(
            "Please Provide User With The Password: '{}'".format(
                request.form.get("password")))
        return redirect(url_for("control"))

    # Pull list of departments for dropdown list
    departments = mongo.db.departments.find()
    return render_template("register.html", departments=departments)


@app.route("/profile/<username>", methods=["POST", "GET"])
@login_required
def profile(username):
    # Grab session's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    tasks = list(mongo.db.tasks.find())

    if session["user"]:
        return render_template("profile.html", tasks=tasks, username=username)

    return redirect(url_for("login"))


# Add department and shared tasks
@app.route("/add_dept_task", methods=["GET", "POST"])
@login_required
@mgmt_access
def add_dept_task():
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        # Grabs and formats current date for "created on"
        current_date = datetime.date.today().strftime('%d/%b/%Y')
        # Used to insert task creator's full name in "created by"
        creator_label = session["first_name"] + " " + session["last_name"]

        task = {
            "type": "departmental",
            "assigned_to": "none",
            "department": request.form.get("department_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"],
            "creator_label": creator_label,
            "created_on": current_date
        }

        mongo.db.tasks.insert_one(task)
        flash("Department Task Successfully Added!")
        return redirect(url_for('tasks'))

    # Pull list of departments
    departments = mongo.db.departments.find()
    return render_template("add_dept_task.html", departments=departments)


@app.route("/edit_dept_task/<task_id>", methods=["GET", "POST"])
@mgmt_access
def edit_dept_task(task_id):
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        # Grabs and formats current date for "created on"
        current_date = datetime.date.today().strftime('%d/%b/%Y')
        # Used to insert task creator's full name in "created by"
        creator_label = session["first_name"] + " " + session["last_name"]

        submit_edit = {
            "type": "departmental",
            "assigned_to": "none",
            "department": request.form.get("department_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"],
            "creator_label": creator_label,
            "created_on": current_date
        }

        mongo.db.tasks.update({"_id": ObjectId(task_id)}, submit_edit)
        flash("Department Task Successfully Updated!")
        return redirect(url_for('tasks'))

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    departments = mongo.db.departments.find()
    return render_template(
        "edit_dept_task.html", task=task, departments=departments)


@app.route("/logout")
def logout():
    # Remove session cookies
    flash("You have been logged out")
    session.clear()
    return redirect(url_for("login"))


# Fetch env vars
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# CHANGE DEBUG TO FALSE BEFORE SUBMISSION!!!!
