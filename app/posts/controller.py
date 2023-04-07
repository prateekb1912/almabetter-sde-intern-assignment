from app import db
from .models import Post

def create_post(message, latitude, longitude):
    location = f'SRID=4326;POINT({longitude} {latitude})'

    post = Post(message=message, location=location)
    
    db.session.add(post)
    db.session.commit()

    return post
