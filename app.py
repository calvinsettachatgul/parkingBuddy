from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from model import connect_to_db, ParkingEvent
app = Flask(__name__)
db = SQLAlchemy(app)

import psycopg2

# try:
#     conn = psycopg2.connect("dbname='parkingbuddy' user='dbuser' host='localhost' password='dbpass'")
# except:
#     print "I am unable to connect to the database"


@app.route("/")
def index():
  # print db
  # events = db.execute('select duration from parkingevents')
  # print events
  # garages = db.execute('select * from garages')
  # eventList = events.fetchAll()
  # garageList = garages.fetchAll()
  parkingevents = ParkingEvent.query.all()
  # garagesList = Garage.query.all()
  # print parkingevents[0]
  return render_template("homepage.html", events=parkingevents)

if __name__ == "__main__":
  app.debug = False
  connect_to_db(app)
  app.run()