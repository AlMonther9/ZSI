from flask import request,jsonify
from settings import app
from models import AirQuality,RealTimeCoordinates,db



@app.route('/update', methods=['POST'])
def update_sensor_values():
    json_data = request.json
    query_params = request.args.to_dict()
    data = {**json_data, **query_params}

    
    # Create AirQuality instance
    air_quality = AirQuality(
        gaz=data.get('gaz'),
        carbon_monoxide_ratio=data.get('carbon_monoxide_ratio'),
        temp=data.get('temp'),
        pressure=data.get('pressure'),
        humidity=data.get('humidity'),
        air_quality=data.get('air_quality')
    )

    db.session.add(air_quality)
    db.session.flush()
    
    # Create RealTimeCoordinates instance
    real_time_coordinates = RealTimeCoordinates(
        latitude=data.get('latitude'),
        longitude=data.get('longitude'),
        altitude=data.get('altitude'),
        google_maps=data.get('google_maps'),
        
        air_quality_id=air_quality.id
    )
    db.session.add(real_time_coordinates)

    try:
        db.session.commit()

        return jsonify(data),200
    # if there any errors undo the changes        
    except Exception as e :
        db.session.rollback()
        return f"Failed to commit data: {str(e)}", 500

