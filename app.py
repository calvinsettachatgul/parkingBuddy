from flask import Flask, render_template,jsonify,redirect
from flask_sqlalchemy import SQLAlchemy
from model import connect_to_db, ParkingEvent, Garage
import os
import requests

app = Flask(__name__)
db = SQLAlchemy(app)

import psycopg2

# try:
#     conn = psycopg2.connect("dbname='parkingbuddy' user='dbuser' host='localhost' password='dbpass'")
# except:
#     print "I am unable to connect to the database"



@app.route("/")
def index():
  parkingevents = ParkingEvent.query.all()
  # garagesList = Garage.query.all()
  return render_template("homepage.html", events=parkingevents)

@app.route("/garages")
def get_garages():
  print "hello"
  garageList = Garage.query.all()
  print garageList
  return jsonify({"garages": garageList})

@app.route('/automatic_api')
def get_automatic_json():
  access_client_id = os.environ['AUTOMATIC_CLIENT_ID']
  access_secret = os.environ['AUTOMATIC_SECRET']
  print access_client_id
  print access_secret

  return jsonify({"lat":"hello you got the data"})


if __name__ == "__main__":
  app.debug = False
  connect_to_db(app)
  app.run()