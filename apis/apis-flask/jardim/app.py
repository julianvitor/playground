import random
from flask import Flask, jsonify, request, render_template
from flask_minify import Minify
from flask import send_file

app = Flask(__name__)
Minify(app=app, html=True, js=True, cssless=True)
# Simulated sensor data
def generate_sensor_data():
    return {
        "air_temp": f"{random.uniform(20, 30):.1f}°C",
        "soil_temp": f"{random.uniform(15, 25):.1f}°C",
        "ph": f"{random.uniform(5, 8):.2f}",
        "air_humidity": f"{random.uniform(40, 70):.1f}%",
        "soil_moisture": f"{random.uniform(30, 60):.1f}%",
        "electrical_consumption": f"{random.uniform(10, 20):.2f} kWh",
        "reservoir_l1": f"{random.uniform(50, 90):.1f}%",
        "reservoir_l2": f"{random.uniform(40, 80):.1f}%",
        "co2": f"{random.randint(300, 500)} ppm",
        "light": f"{random.randint(500, 1000)} Lux",
    }

@app.route('/pt')
def index():
    return render_template('dashboard.html')

@app.route('/en')
def index_en():
    return render_template('dashboard-english.html')

@app.route('/')
def index_spa():
    return render_template('dashboard-spa.html')

@app.route('/min')
def index_spa_min():
    return render_template('dashboard-spa-min.html')

@app.route('/robots.txt')
def serve_robots():
    return send_file('robots.txt')

@app.route('/sensor-data', methods=['GET'])
def get_sensor_data():
    sensor_data = generate_sensor_data()
    return jsonify(sensor_data)

@app.route('/water-plant', methods=['POST'])
def water_plant():
    response = {"message": "Regando planta com 300ml"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
