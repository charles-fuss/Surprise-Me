from http.client import NO_CONTENT
from multiprocessing.sharedctypes import Value
from flask import Flask, render_template, redirect, url_for, request
import getResults
import json
import os
import time


app = Flask(__name__)


@app.route("/")
def home():
    #clear data in case user returns to page vvvv
    if request.method == "POST":
        return redirect(url_for("questionnaire", zip=None))
    else:
        return render_template('index.html')

@app.route("/questionnaire", methods = ["POST", "GET"])
def questionnaire(zip = None):
    if request.method == "POST":
        zip = request.form['zip']
        type = request.form['type']
        checkboxInput = request.form.getlist('check')
        price = request.form.getlist('price')
        if(len(zip) == 5 or zip.isdigit == True): #registers zip as a string, fix
            return redirect(url_for("loading",checkboxInput=checkboxInput, zip=zip, price=price, type=type))
        else:
            return render_template('questionnaire.html', zip='invalid_zip')
    else:
        return render_template('questionnaire.html', zip=zip)

@app.route("/loading/<zip>/<type>/<price>/<checkboxInput>")
def loading(checkboxInput, zip, price, type):
    getResults.run(checkboxInput=checkboxInput, zip=zip, price=price, type=type)
    if(os.path.getsize(r"C:\Users\charl\Documents\Professional\Coding\flsktst\data.json") > 0):
        return redirect(url_for('results'))
    else:
        return render_template('loading.html')

@app.route("/results")
def results(data=None):
    with open(r"C:\Users\charl\Documents\Professional\Coding\flsktst\data.json", 'r') as j:
        data = json.loads(j.read())
    return render_template('results.html', data=data)

@app.route("/visualization")
def visualization(data=None):
    with open(r"C:\Users\charl\Documents\Professional\Coding\flsktst\data.json", 'r') as j:
        data = json.loads(j.read())
    return render_template('visualization.py', data=data)