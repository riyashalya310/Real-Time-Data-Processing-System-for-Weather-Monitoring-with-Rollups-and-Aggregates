# backend/app.py
from flask import Flask, jsonify, request
from weather_data import process_weather_data, summarize_weather, check_thresholds
from models import DailyWeatherSummary
from database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
db.init_app(app)

@app.route('/weather', methods=['POST'])
def receive_weather_data():
    weather_data = request.json
    process_weather_data(weather_data)
    return jsonify({"status": "success"})

@app.route('/summary', methods=['GET'])
def get_daily_summary():
    summaries = summarize_weather()
    return jsonify(summaries)

@app.route('/alerts', methods=['GET'])
def check_alerts():
    alerts = check_thresholds()
    return jsonify(alerts)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
