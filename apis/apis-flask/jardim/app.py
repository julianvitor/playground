import random
from flask import Flask, jsonify, request, render_template
from flask_minify import Minify

app = Flask(__name__)
Minify(app=app, html=True, js=True, cssless=True)
# Simulated sensor data
def generate_sensor_data():
    return {
        "air_temperature": f"{random.uniform(20, 30):.1f}°C",
        "soil_temperature": f"{random.uniform(15, 25):.1f}°C",
        "soil_ph": f"{random.uniform(5, 8):.2f}",
        "air_humidity": f"{random.uniform(40, 70):.1f}%",
        "soil_moisture": f"{random.uniform(30, 60):.1f}%",
        "electrical_consumption": f"{random.uniform(10, 20):.2f} kWh",
        "reservoir_level_1": f"{random.uniform(50, 90):.1f}%",
        "reservoir_level_2": f"{random.uniform(40, 80):.1f}%",
        "co2_level": f"{random.randint(300, 500)} ppm",
        "light_level": f"{random.randint(500, 1000)} Lux",
    }

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/english')
def index_en():
    return render_template('dashboard-english.html')

@app.route('/spa')
def index_spa():
    return render_template('dashboard-spa.html')

@app.route('/spa-min')
def index_spa_min():
    return render_template('dashboard-spa-min.html')

@app.route('/sensor-data', methods=['GET'])
def get_sensor_data():
    sensor_data = generate_sensor_data()
    return jsonify(sensor_data)

@app.route('/water-plant', methods=['POST'])
def water_plant():
    # You can add logic here to simulate plant watering
    response = {"message": "Plant manually watered!"}
    return jsonify(response)

if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0 and port 8082
    app.run(host='0.0.0.0', port=5000, debug=True)
