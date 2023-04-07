from geoalchemy2 import Geometry
from app import db

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255), nullable=False)
    location = db.Column(Geometry(geometry_type='POINT', srid=4326))
    timestamp = db.Column(db.DateTime(timezone=True), default = db.func.now())

    def __str__(self) -> str:
        return f'{self.message} at {self.timestamp} and {self.location}'