from settings import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class AirQuality(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    gaz = db.Column(db.Integer, )
    carbon_monoxide_ratio = db.Column(db.Float, )
    temp = db.Column(db.Float, )
    pressure = db.Column(db.Float, )
    humidity = db.Column(db.Float, )
    air_quality = db.Column(db.Float, )
    real_time_coordinates = db.relationship('RealTimeCoordinates', backref='air_quality')

class RealTimeCoordinates(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float,)
    longitude =db.Column(db.Float, )
    altitude = db.Column(db.Float, )
    google_maps = db.Column(db.Float)
    DataTime = db.Column(db.DateTime, default=datetime.utcnow, )
    air_quality_id = db.Column(db.Integer, db.ForeignKey("air_quality.id"))
    
    def __repr__(self):
        return f"we are in {self.latitude, self.longitude} at {self.DataTime}"