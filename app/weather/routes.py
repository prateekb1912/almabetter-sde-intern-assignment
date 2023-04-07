from flask import Blueprint

weather_bp = Blueprint('weather', __name__, url_prefix='/weather')

