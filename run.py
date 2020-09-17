import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "to send a message use /username/message"


"""<username> in the app route decorator will now act as a variable"""


@app.route("/<username>")
def user(username):
    return "Hi " + username


@app.route("/<username>/<message>")
def send_message(username, message):
    return "{0}: {1}".format(username, message)

app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)
