#application.py

from flask import Flask

app=Flask(__name__)

@app.route("/")
def display():
  return "My roll no. is 2349!"
