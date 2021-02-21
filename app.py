import os
from flask import Flask
if os.path.exists("env.py"):
    import env


# Create instance of flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "hello!"


# Fetch env vars
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# CHANGE DEBUG TO FALSE BEFORE SUBMISSION!!!!
