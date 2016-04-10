from model import ParkingEvent, connect_to_db, db
from app import app
import csv
from datetime import datetime

def load_sessions(file):
  with open(file) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)



  # floor = db.Column(db.Integer(), nullable=False)
  # duration = db.Column(db.Integer(), nullable=False)
  # lat = db.Column(db.Integer(), nullable=False)
  # long = db.Column(db.Integer(), nullable=False)
  # time = db.Column(db.String(64), nullable=False)
    for i, row in enumerate(csvreader):
      newParkingEvent = ParkingEvent(floor=row[0],
                                duration=row[1],
                                lat=row[2],
                                long=row[3],
                                time=row[4]
                                            )
      db.session.add(newParkingEvent)
      if i % 10 == 0:
        print i

    db.session.commit()



if __name__ == '__main__':
  connect_to_db(app)
  db.create_all()

  load_sessions('./parkingData.csv');
