from flask import Blueprint, jsonify, request

from app.utils.weather_utils import get_and_parse_weather_data

weather_bp = Blueprint('weather', __name__, url_prefix='/weather')

@weather_bp.route('/', methods=['GET'])
def get_current_weather():
    lon = request.args.get('lon')
    lat = request.args.get('lat')

    if not (lat and lon):
        return jsonify({'error': 'location parameters are required'}), 400

    response_data = get_and_parse_weather_data(lon, lat)

    return jsonify({
        'data': response_data
    }), 200