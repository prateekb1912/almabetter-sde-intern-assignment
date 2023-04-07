import requests
from flask import Blueprint, jsonify, request
from flasgger import swag_from

from app.utils.weather_utils import get_and_parse_weather_data

weather_bp = Blueprint('weather', __name__, url_prefix='/weather')

@weather_bp.route('/', methods=['GET'])
@swag_from('weather.yml')
def get_current_weather():
    try:
        lon = request.args.get('lon')
        lat = request.args.get('lat')

        if not (lat and lon):
            return jsonify({'error': 'location parameters are required'}), 400

        response_data = get_and_parse_weather_data(lon, lat)

        return jsonify({
            'data': response_data
        }), 200

    except requests.exceptions.RequestException as request_exception:
        return jsonify({'error': f'Error connecting to the weather API: {str(request_exception)}'}), 500

    except KeyError as key_error:
        return jsonify({'error': f'Required data not found in weather API response: {str(key_error)}'}), 500

    except Exception:
        return jsonify({'error': 'An unknown error occurred.'}), 500
