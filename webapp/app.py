import pickle
import os
import numpy as np
from flask import Flask, request, render_template
import requests
from waitress import serve

#instance of web app
app = Flask(__name__)

#now web app need to communicate db app
DB_SERVICE_URL="http://dbapp_container:8001/add_records"
# http: --> serving url on which dbapp is serving
# cntdbapp --> service name of dbapp (name of container of dbapp image) when you create give same name for communication
# 8001 --> port on which dbapp is serving, in app.py of db app port number should 8001 only
# /add_record --> route in dbapp which is going to add record in db, on which route you are going to serve insertion of record, so that route must be created in dbapp


# web app depends on db app
# we can create 2 components communicating on same port using docker network

# Load ML model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route("/")
def welcome():
    return render_template("index.html")

# posting to the dbapp
# rewrite rendering template we are passing context recods, Jinja templating engine is used.
@app.route("/predict", methods=["POST"])
def make_pred():
    sl = float(request.form['sl'])
    sw = float(request.form['sw'])
    pl = float(request.form['pl'])
    pw = float(request.form['pw'])

    # now creating 2D numpy array
    imp=np.array([[sl, sw, pl, pw]])
    prediction = model.predict(imp)[0]
    requests.post(url=DB_SERVICE_URL, json={"sl": sl, "sw": sw, "pl": pl, "pw": pw, "prediction": str(prediction)})
    return render_template("index.html", prediction=str(prediction))

# getting data from db app
@app.route("/show_records", methods=["GET"])
def show_records():
    records = requests.get("http://cntdbapp:8001/records")
    return render_template("records.html", records=records.json()) # we want to pass records to records.html (json to python directory)
    # jinja2 will iterate through records 

if __name__ == "__main__":
    serve(app,host='0.0.0.0', port=8000)
