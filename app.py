from flask import Flask, render_template,jsonify,redirect
from flask_sqlalchemy import SQLAlchemy
from model import connect_to_db, ParkingEvent, Garage
import os
import requests
from requests_oauthlib import OAuth1

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

  url = 'https://api.automatic.com/trip/'
  auth = OAuth1(access_client_id, access_secret)


  headers = {"Authorization": "Bearer: e5cdd2a2f2c52ac2ff9825f53ac566f45c513991"}

  # response = requests.get('https://www.example.com').content
  response = requests.get(url, headers=headers)

  print response

  return jsonify({"lat":37.8033345, "long":-122.2695569})


if __name__ == "__main__":
  app.debug = True
  connect_to_db(app)
  app.run()