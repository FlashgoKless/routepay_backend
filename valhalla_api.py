from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

VALHALLA_URL = "http://localhost:8002/route"

@app.route('/route', methods=['POST'])
def get_route():
    try:
        data = request.get_json()
        
        if not data or 'locations' not in data or len(data['locations']) < 2:
            return jsonify({"error": "Необходимо указать как минимум 2 точки (start и end)"}), 400
        
        valhalla_request = {
            "locations": data['locations'],
            "costing": "auto",
            "directions_options": {
                "units": "kilometers"
            },
            "id": "valhalla_demo"
        }
        
        if 'costing_options' in data:
            valhalla_request['costing_options'] = data['costing_options']
        
        response = requests.post(VALHALLA_URL, json=valhalla_request)
        response.raise_for_status()
        valhalla_response = response.json()
        
        maneuvers_geometries = []
        if 'trip' in valhalla_response and 'legs' in valhalla_response['trip']:
            for leg in valhalla_response['trip']['legs']:
                for maneuver in leg['maneuvers']:
                    if 'geometry' in maneuver:
                        maneuvers_geometries.append(maneuver['geometry'])
        
        return jsonify({
            "status": "success",
            "maneuvers_geometries": maneuvers_geometries,
            "valhalla_full_response": valhalla_response
        })
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Ошибка при запросе к Valhalla: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Произошла ошибка: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)