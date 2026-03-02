from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/dashboard', methods=['GET'])
def get_dashboard():
    return jsonify({'message': 'Dashboard data'}), 200

@app.route('/api/monitoring', methods=['GET'])
def get_monitoring():
    return jsonify({'message': 'Monitoring data'}), 200

@app.route('/api/control', methods=['POST'])
def control_device():
    data = request.get_json()
    return jsonify({'message': 'Control command received', 'data': data}), 200

if __name__ == '__main__':
    app.run(debug=True)