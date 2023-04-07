from datetime import datetime, timedelta
import random

from geoalchemy2.shape import from_shape
from shapely import Point

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

def generate_posts_data(num_posts = 50):

    # Set the bounding box of the area of interest
    min_lon, max_lon = -30, 30
    min_lat, max_lat = -10, 10

    # Generate 50 random posts
    posts = []
    for i in range(num_posts):
        # Generate a random message
        message = f"Random post {i+1}"
        
        # Generate a random location within the bounding box
        lon = random.uniform(min_lon, max_lon)
        lat = random.uniform(min_lat, max_lat)
        point = Point(lon, lat)
        
        # Convert the point to a WKTElement
        wkt_element = from_shape(point, srid=4326)
        
        # Generate a random timestamp in the last 500 days
        timestamp = datetime.utcnow() - timedelta(days=random.randint(1, 500))
        
        # Create a new Post object and add it to the list of posts
        post = Post(message=message, location=wkt_element, timestamp=timestamp)
        posts.append(post)

    print(posts)
    
    # Insert the posts into the database
    db.session.bulk_save_objects(posts)
    db.session.commit()
