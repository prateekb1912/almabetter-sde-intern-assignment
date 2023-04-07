from app import db
from .models import Post

def create_post(message, latitude, longitude):
    location = f'SRID=4326;POINT({longitude} {latitude})'

    post = Post(message=message, location=location)
    
    db.session.add(post)
    db.session.commit()

    return post

def filter_posts_by_distance(lat, lon, page=1, per_page=10):
    target_location = f'SRID=4326;POINT({lon} {lat})'

    nearby_posts = Post.query.filter(
        Post.location.ST_Distance(target_location) <= 1000
    ).order_by(Post.timestamp.desc()).paginate(page=page, per_page=per_page)

    return nearby_posts
