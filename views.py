from flask import request
from settings import app



@app.route('/update', methods=['POST'])
def update_sensor_values():
    data = request.json
    temp_pressure_humidity_sensor_value = data.get('gasSensorValue')
    gas_sensor_value = data.get('tempPressureHumiditySensorValue')
    reads = str(gas_sensor_value) + " " + str(temp_pressure_humidity_sensor_value)
    # datahandler.store_data(reads)
    
    return 'Data received'

