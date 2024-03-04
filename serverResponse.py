from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update_sensor_values():
    data = request.json
    gas_sensor_value = data.get('gasSensorValue')
    temp_pressure_humidity_sensor_value = data.get('tempPressureHumiditySensorValue')
    print(f"Gas Sensor value: {gas_sensor_value}")
    print(f"Temp/Pressure/Humidity Sensor value: {temp_pressure_humidity_sensor_value}")
    return 'Data received'

if __name__ == '__main__':
    app.run(host='192.168.12.166', port=3000)
