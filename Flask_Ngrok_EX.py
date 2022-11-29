import pandas as pd
from flask_ngrok import run_with_ngrok
from flask import request, jsonify, Flask
import random as rk

app = Flask(__name__)
run_with_ngrok(app)

planilha_json = {
    "1": {
        "name": "Mahesh",
        "Age": 25,
        "City": "Bangalore",
        "Country": "India"
    },
    "2": {
        "name": "Alex",
        "Age": 26,
        "City": "London",
        "Country": "UK"
    },
    "3": {
        "name": "David",
        "Age": 27,
        "City": "San Francisco",
        "Country": "USA"
    },
    "4": {
        "name": "John",
        "Age": 28,
        "City": "Toronto",
        "Country": "Canada"
    },
    "5": {
        "name": "Chris",
        "Age": 29,
        "City": "Paris",
        "Country": "France"
    }
}

@app.route("/")  

def home():
    return "<marquee><h3> Para ver a planilha em JSON, adicione /index ao final da URL.</h3></marquee>"


@app.route("/index")

def index():
    return jsonify(planilha_json)  


app.run()
