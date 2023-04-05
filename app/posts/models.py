from app import db

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    @property
    def location(self):
        return f'({self.latitude},{self.longitude})'

    @location.setter
    def location(self, point):
        point = point.strip('()').split(',')
        self.latitude = float(point[0])
        self.longitude = float(point[1])