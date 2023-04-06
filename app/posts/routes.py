from flask import jsonify,request, Blueprint

from app.posts.controller import create_post

posts_bp = Blueprint('posts', __name__, url_prefix='/posts')


@posts_bp.route('', methods=['POST'])
def post_text_message():
    data = request.json

    message = data['message']
    latitude = float(data['lat'])
    longitude = float(data['lon'])

    post = create_post(message, latitude, longitude)

    return jsonify({'response': 'Post created successfully.'})