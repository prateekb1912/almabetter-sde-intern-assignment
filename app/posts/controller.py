from app import db
from .models import Post

def create_post(message, latitude, longitude):
    post = Post(message=message, latitude=latitude, longitude=longitude)
    
    db.session.add(post)
    db.session.commit()

    return post