from flask import jsonify,request, Blueprint
from flasgger import swag_from

from app.posts.controller import create_post, filter_posts_by_distance, generate_posts_data
from app.utils.posts_utils import prettify_timestamp, serialize_location

posts_bp = Blueprint('posts', __name__, url_prefix='/posts')

@posts_bp.route('', methods=['POST'])
@swag_from('posts.yml')
def post_text_message():
    try:
        data = request.json

        if 'message' not in data or 'lat' not in data or 'lon' not in data:
            return jsonify({'error': 'Missing required fields.'}), 400

        message = data['message']
        latitude = float(data['lat'])
        longitude = float(data['lon'])

        create_post(message, latitude, longitude)

        return jsonify({'response': 'Post created successfully.'})

    except ValueError:
        return jsonify({'error': 'Invalid latitude or longitude.'}), 400

    except Exception:
        return jsonify({'error': 'An unknown error occurred.'}), 500

@posts_bp.route('/', methods=['GET'])
@swag_from('posts.yml')
def get_nearby_posts():
    try:
        lat = request.args.get('lat')
        lon = request.args.get('lon')

        if not (lat and lon):
            return jsonify({'error': 'location parameters are required'}), 400

        # extract page number, default = 1
        page = int(request.args.get('page', default=1))

        # Currently assuming nearby to relate to a 1km distance
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
            'page': paginated_posts.page,
            'total': paginated_posts.total
        }

        return jsonify(response_data), 200

    except ValueError:
        return jsonify({'error': 'Invalid page number.'}), 400

    except Exception:
        return jsonify({'error': 'An unknown error occurred.'}), 500


@posts_bp.route('/generate', methods=['GET'])
@swag_from('posts.yml')
def add_random_posts():
    try:
        num_posts = int(request.args.get('num', default=10))

        if num_posts <= 0:
            return jsonify({'error': 'Number of posts must be greater than zero.'}), 400

        generate_posts_data(num_posts)

        return jsonify({
            'message': 'success',
            'posts': num_posts
        })

    except ValueError:
        return jsonify({'error': 'Invalid number of posts.'}), 400

    except Exception:
        return jsonify({'error': 'An unknown error occurred.'}), 500
