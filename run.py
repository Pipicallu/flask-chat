import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []


def add_messages(username, message):
    """ Add messages to the messages list """
    messages.append("{}: {}".format(username, message))


def get_all_messages():
    """ get all of the messages and separate them using a 'br' tag """
    return "<br>".join(messages)


@app.route("/")
def index():
    return "to send a message use /username/message"


"""<username> in the app route decorator will now act as a variable"""


@app.route("/<username>")
def user(username):
    """ display chat messages """
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())


@app.route("/<username>/<message>")
def send_message(username, message):
    """create a new message and re-direct to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)


app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)
