from flask import Blueprint, jsonify
from services.weather_service import get_weather

weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/weather', methods=['GET'])
def weather():
    location = 'Lviv, Ukraine'
    weather_data = get_weather(location)
    return jsonify(weather_data), 200
