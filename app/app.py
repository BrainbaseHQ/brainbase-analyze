from flask import Flask, request, jsonify, g
from functools import wraps
from src.index import run, setup, approve
from flask_cors import CORS
from memory import create_or_update_db, get_history_from_db, update_history_in_db
from logs import update_logs_in_db, get_logs_from_db, create_or_update_logs_db
import sqlite3
import threading
import requests
import logging
import json
import os
import time

app = Flask(__name__)
CORS(app)

""" 
    Logger to log messages to the console.
"""
LOG_DATABASE = "log.db"

""" 
    Database to save chat history.
"""
DATABASE = "chat_history.db"

# Load the config.json file
with open("app/src/config.json", "r") as file:
    config_data = json.load(file)
    
print("config data", config_data)

# Extract the inputs array
inputs = config_data["inputs"]

@app.route('/')
def hello_world():
    return 'Hello, World!'

""" 
    This is the run endpoint. It is called when the user sends a message to
    your app. It is passed a message object that contains the user's input.
    You can use this to process the user's input and return a response.

    The run function should return a dictionary with the following keys:
    - success: a boolean indicating whether the run was successful
    - message: a string containing a message to display to the user
    - data: a dictionary containing any data you want to pass to the frontend
    - context: a dictionary containing any context you want to pass to the next
                run call

    The run function should raise an exception if the run was not successful.
    The exception message will be displayed to the user.
 """


@app.route('/analyze', methods=['POST'])
@refresh_token_if_expired
def handle_analyze():
    try:
        text = request.json['text']
        instruction = request.json['instruction']
        response = run(instruction=instruction, text=text)

        return jsonify(response)
    except Exception as e:
        return jsonify(str(e))

if __name__ == '__main__':
    app.teardown_appcontext(close_db)
    app.run(host="0.0.0.0", port=8080)
