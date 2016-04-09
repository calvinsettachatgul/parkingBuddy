from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ParkSession(db.Model):

  __tablename__ = "parksessions"
  parksession_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
  floor = db.Column(db.Integer(), nullable=False)
  duration = db.Column(db.Integer(), nullable=False)
  lat = db.Column(db.Integer(), nullable=False)
  long = db.Column(db.Integer(), nullable=False)
  time = db.Column(db.String(64), nullable=False)

def connect_to_db(app):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///parkingbuddy'  # weekend wanderlust map
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # Allows interactive querying in the shell

    from app import app
    connect_to_db(app)
    print "Connected to DB."