# from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
# from sqlalchemy.orm import declarative_base, relationship
# from sqlalchemy.sql import func

# Base = declarative_base()
# class RealTimeCoordinates(Base):
#     __tablename__ = 'real_time_coordinates'

#     id = Column(Integer, primary_key=True)
#     latitude = Column(Float)
#     longitude = Column(Float)
#     altitude = Column(Float)
#     DataTime = Column(DateTime(timezone=True), server_default=func.now())

#     air_quality_id = Column(Integer, ForeignKey('air_quality.id'), unique=True)
#     air_quality = relationship('AirQuality', back_populates='real_time_coordinates')

#     def __repr__(self):
#         return f"we are in {self.latitude, self.longitude} at {self.DataTime}"

from settings import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class AirQuality(db.Model):

    id =       db.Column(db.Integer, primary_key=True)
    gaz =      db.Column(db.Float)
    pressure = db.Column(db.Float)
    real_time_coordinates = db.relationship('RealTimeCoordinates', backref='air_quality')

class RealTimeCoordinates(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude =db.Column(db.Float)
    altitude = db.Column(db.Float)
    DataTime = db.Column(db.DateTime, default=datetime.utcnow)
    air_quality_id = db.Column(db.Integer, db.ForeignKey("air_quality.id"))
    def __repr__(self):
        return f"we are in {self.latitude, self.longitude} at {self.DataTime}"