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


# Home page
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


# Shows shared and user's departments tasks
@app.route("/tasks")
@login_required
def tasks():
    # We need list(x) to iterate multiple times through tasks
    tasks = list(mongo.db.tasks.find().sort("due_date", 1))
    # Compares dates to see if task due
    today = datetime.datetime.today()
    # Grab users department
    departments = list(mongo.db.departments.find())
    return render_template(
        "tasks.html", tasks=tasks, departments=departments, today=today)


# Lists all departmental tasks & has search function
@app.route("/all_tasks")
@login_required
@mgmt_access
def all_tasks():
    # Tasks sorted by due date
    tasks = list(mongo.db.tasks.find().sort("due_date", 1))
    # Pull list of departments
    departments = list(mongo.db.departments.find())
    # Used to compare due_date to current date to warn if task past due
    today = datetime.datetime.today()
    return render_template(
        "all_tasks.html", tasks=tasks,
        departments=departments, today=today)


# Shows list of tasks user assigned or edited
@app.route("/track_delegated_tasks")
@login_required
@mgmt_access
def track_delegated_tasks():
    users = list(mongo.db.users.find())
    tasks = list(mongo.db.tasks.find().sort("due_date", 1))
    # Used to compare due_date to current date to warn if task past due
    today = datetime.datetime.today()
    departments = list(mongo.db.departments.find())
    return render_template(
        "track_delegated_tasks.html",
        tasks=tasks, users=users, departments=departments, today=today)


# Log in page
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
                # Grab other sesssion user's info
                session["department"] = logged_user["department"].lower()
                session["first_name"] = logged_user["first_name"].capitalize()
                session["last_name"] = logged_user["last_name"].capitalize()
                session["is_admin"] = logged_user["admin"]
                session["is_mgmt"] = logged_user["mgmt"]
                # Grab user's department label
                department = mongo.db.departments.find_one(
                    {"department_name": session["department"]})
                session["department_label"] = department["department_label"]

                flash("Welcome, {}".format(session["first_name"]))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # Invalid password
                flash("Incorrect Username and/or Password")
        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


# Register new user
@app.route("/register", methods=["GET", "POST"])
@login_required
@mgmt_access
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
        # Check do inputs for password and repeat password match
        if request.form.get("password") == request.form.get("repeat_password"):
            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password")),
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
            return profile(session["user"])
        else:
            flash("Passwords Do Not Match")

    # Pull list of departments for dropdown list
    departments = mongo.db.departments.find()
    return render_template("register.html", departments=departments)


# User's profile page
@app.route("/profile/<username>", methods=["POST", "GET"])
@login_required
def profile(username):
    # Grab session's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # Used to compare due_date to current date to warn if task past due
    today = datetime.datetime.today()
    tasks = list(mongo.db.tasks.find().sort("due_date", 1))

    return render_template(
        "profile.html", tasks=tasks, username=username, today=today)


# Add department & shared task
@app.route("/add_dept_task", methods=["GET", "POST"])
@login_required
@mgmt_access
def add_dept_task():
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        # Grabs and formats current date for "created on"
        today = datetime.datetime.today()
        # Format due_date string to date type
        due_date_str = request.form.get("due_date")
        try:
            due_date = datetime.datetime.strptime(due_date_str, '%d/%b/%Y')
        except ValueError:
            flash("Unable to create task. Please choose correct date format")
            return redirect(request.referrer)
        # Used to insert task creator's full name in "created by"
        creator_label = session["first_name"] + " " + session["last_name"]

        task = {
            "type": "departmental",
            "assigned_to": "none",
            "department": request.form.get("department_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": due_date,
            "created_by": session["user"],
            "creator_label": creator_label,
            "created_on": today,
            "completed": False
        }

        mongo.db.tasks.insert_one(task)
        flash("Department Task Successfully Added!")
        return redirect(url_for('tasks'))

    # Pull list of departments
    departments = mongo.db.departments.find()
    return render_template("add_dept_task.html", departments=departments)


# Add personal tasks
@app.route("/add_personal_task", methods=["GET", "POST"])
@login_required
def add_personal_task():
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        # Grabs and formats current date for "created on"
        today = datetime.datetime.today()
        # Format due_date string to date type
        due_date_str = request.form.get("due_date")
        try:
            due_date = datetime.datetime.strptime(due_date_str, '%d/%b/%Y')
        except ValueError:
            flash("Unable to create task. Please choose correct date format")
            return redirect(request.referrer)
        # Used to insert task creator's full name in "created by"
        creator_label = session["first_name"] + " " + session["last_name"]
        # Non admins have name select hidden
        # So delegated will be None
        delegated = request.form.get("username")
        if delegated is None:
            assigned_to = session["user"]
        else:
            assigned_to = delegated

        task = {
            "type": "personal",
            "assigned_to": assigned_to,
            "department": "none",
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": due_date,
            "created_by": session["user"],
            "creator_label": creator_label,
            "created_on": today,
            "completed": False
        }

        mongo.db.tasks.insert_one(task)
        flash("Personal Task Successfully Added!")
        return redirect(url_for('tasks'))

    # Pull list of users
    users = mongo.db.users.find().sort("first_name", 1)
    return render_template("add_personal_task.html", users=users)


# Edit department task
@app.route("/edit_dept_task/<task_id>", methods=["GET", "POST"])
def edit_dept_task(task_id):
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        # Grabs and formats current date for "updated on"
        today = datetime.datetime.today()
        # Format due_date string to date type
        due_date_str = request.form.get("due_date")
        try:
            due_date = datetime.datetime.strptime(due_date_str, '%d/%b/%Y')
        except ValueError:
            flash("Unable to create task. Please choose correct date format")
            return redirect(request.referrer)
        # Create editor's full name label
        updator_label = session["first_name"] + " " + session["last_name"]

        mongo.db.tasks.update({"_id": ObjectId(task_id)}, {"$set": {
            "department": request.form.get("department_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": due_date,
            "updated_by": session["user"],
            "updator_label": updator_label,
            "updated_on": today
        }})

        flash("Department Task Successfully Updated!")
        return redirect(url_for('tasks'))

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    departments = mongo.db.departments.find()
    return render_template(
        "edit_dept_task.html", task=task, departments=departments)


# Edit personal task
@app.route("/edit_personal_task/<task_id>", methods=["GET", "POST"])
def edit_personal_task(task_id):
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        # Grabs and formats current date for "updated on"
        today = datetime.datetime.today()
        # Format due_date string to date type
        due_date_str = request.form.get("due_date")
        try:
            due_date = datetime.datetime.strptime(due_date_str, '%d/%b/%Y')
        except ValueError:
            flash("Unable to create task. Please choose correct date format")
            return redirect(request.referrer)
        # Create editor's full name label
        updator_label = session["first_name"] + " " + session["last_name"]
        # Non admins cant't edit other's tasks and user select is empty
        # If form.get is None it's non admin and task is assigned to user
        if request.form.get("username") is None:
            assigned_to = session["user"]
        else:
            assigned_to = request.form.get("username")

        mongo.db.tasks.update({"_id": ObjectId(task_id)}, {"$set": {
            "assigned_to": assigned_to,
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": due_date,
            "updated_by": session["user"],
            "updator_label": updator_label,
            "updated_on": today
        }})
        flash("Personal Task Successfully Updated!")
        return redirect(url_for('tasks'))

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    users = mongo.db.users.find().sort("first_name", 1)
    return render_template(
        "edit_personal_task.html", task=task, users=users)


# Delete task
@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    flash("Task Successfully Deleted")
    return redirect(request.referrer)


# Search feature
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}}))
    today = datetime.datetime.today()
    departments = list(mongo.db.departments.find())
    return render_template(
        'all_tasks.html', tasks=tasks, today=today, departments=departments)


# Complete task
@app.route("/complete_task/<task_id>", methods=["GET", "POST"])
def complete_task(task_id):
    # Grabs and formats current date for "completed on"
    today = datetime.datetime.today()
    # Puts users full name for display purposes
    completed_by_label = session["first_name"] + " " + session["last_name"]
    # Updates it to keep track on who and when completed it
    mongo.db.tasks.update({"_id": ObjectId(task_id)}, {"$set": {
            "completed": True,
            "completed_by": session["user"],
            "completed_by_label": completed_by_label,
            "completed_on": today
        }})

    flash("Task Successfully Completed")
    return redirect(request.referrer)


# User logout
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
