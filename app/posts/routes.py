from flask import jsonify,request

from app.posts import posts_bp
from app.posts.controller import create_post


@posts_bp.route('/messages', methods=['POST'])
def post_text_message():
    # data = request.json

    # message = data['message']
    # latitude = float(data['lat'])
    # longitude = float(data['lon'])

    # post = create_post(message, latitude, longitude)

    return jsonify({'response': 'Post created successfully.'})