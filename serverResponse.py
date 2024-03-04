from datahandler import DataHandler
from flask import Flask, request, jsonify

app = Flask(__name__)
datahandler = DataHandler()

@app.route('/update', methods=['POST'])
def update_sensor_values():
    data = request.json
    temp_pressure_humidity_sensor_value = data.get('gasSensorValue')
    gas_sensor_value = data.get('tempPressureHumiditySensorValue')
    reads = str(gas_sensor_value) + " " + str(temp_pressure_humidity_sensor_value)
    datahandler.store_data(reads)
    
    return 'Data received'

if __name__ == '__main__':
    app.run(host='192.168.12.166', port=3000)
