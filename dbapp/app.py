# database to store feature vector and the prediction for that vector. 
# create additional rpute to store the content of this table. 
# python application talk to the database. 
# --> write down sql in python format
# --> ORM create model classes which maps to tables in db.

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from waitress import serve
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'predictions.db')
db_path = db_path.replace("\\", "/")

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + db_path
# dialect + driver : //username: password @ host:port/database

# every dialect has a default driver. 
# /// --> relative path in sqllite 
# //// --> absolute path in sqllite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# avoid signaling whenever there is modification in the object.

db = SQLAlchemy(app)
# we are integrating flask web app instance with db instance. 
# 1 ORM model class per table

# ORM Model
# only inheriting db.model known as model class, 1 model class mapped to 1 database table.
class Prediction(db.Model):
    # default __tablename__==prediction
    id = db.Column(db.Integer, primary_key=True)
    sl = db.Column(db.Float)
    sw = db.Column(db.Float)
    pl = db.Column(db.Float)
    pw = db.Column(db.Float)
    prediction = db.Column(db.String(50))

@app.route("/add_records", methods=["POST"])
def add_record():
    record=request.get_json()
    record=Prediction(**record) #unfloading the data of 5 columns instance of prediction with this data.
    db.session.add(record)
    db.session.commit() 

    return jsonify({"message": "record added"})
    #jsonify convert python dictionary to json format


@app.route("/records",methods=["GET"])
def show_records():
    records = Prediction.query.all()
    records = [{"id": record.id, "sepal_length": record.sl, "sepal_width": record.sw, "petal_length": record.pl, "petal_width": record.pw, "prediction": record.prediction} for record in records]
    return jsonify(records)

    

# if do not exist table then it will create the table.
# if table associated with model class already exist then it will not do anything.
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    serve(app, host='0.0.0.0', port=8001)


# db.create_all() will create the db and go through all the ORM classes and map them to the table. 
# request context - to send HTTP requests application context