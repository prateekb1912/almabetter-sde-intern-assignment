from flask import jsonify,request, Blueprint

from app.posts.controller import create_post, filter_posts_by_distance
from app.utils.posts_utils import prettify_timestamp, serialize_location

posts_bp = Blueprint('posts', __name__, url_prefix='/posts')

@posts_bp.route('', methods=['POST'])
def post_text_message():
    data = request.json

    message = data['message']
    latitude = float(data['lat'])
    longitude = float(data['lon'])

    create_post(message, latitude, longitude)

    return jsonify({'response': 'Post created successfully.'})


@posts_bp.route('/', methods=['GET'])
def get_nearby_posts():
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    if not (lat and lon):
        return jsonify({'error': 'location parameters are required'}), 400
    
    # extract page number, default = 1
    page = int(request.args.get('page', default=1))

    paginated_posts = filter_posts_by_distance(lat, lon, page)
    posts = []

    for post in paginated_posts.items:
        timestamp = post.timestamp
        pretty_timestamp = prettify_timestamp(timestamp)

        posts.append({
            'id': post.id,
            'message': post.message,
            'location': serialize_location(post.location),
            'timestamp': pretty_timestamp            
        })
    
    response_data = {
        'posts': posts,
        'has_prev': paginated_posts.has_prev,
        'has_next': paginated_posts.has_next,
        'page': paginated_posts.page,
        'pages': paginated_posts.pages,
        'total': paginated_posts.total
    }


    return jsonify(response_data), 200
    