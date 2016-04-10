from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from model import connect_to_db, ParkingEvent
app = Flask(__name__)
db = SQLAlchemy(app)


@app.route("/")
def index():
  return render_template("homepage.html")

if __name__ == "__main__":
  app.debug = False
  connect_to_db(app)
  app.run()