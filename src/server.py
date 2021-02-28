from flask import Flask

from database import Database

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/database/ping')
def databasePing():
    database = Database().getDatabase()
    return database.command('ping')