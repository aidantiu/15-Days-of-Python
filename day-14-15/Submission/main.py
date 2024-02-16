from flask import Flask, jsonify, request

app = Flask(__name__)

aws_services = [
    {
        "id": 1,
        "service": "Lambda"
    },
    {
        "id": 2,
        "service": "Simple Storage Service(S3)"
    }
]

# base url
@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'Welcome to AWS Services API'})

# Route to get all AWS services
@app.route('/aws_services/get_all', methods=['GET'])
def get_all():
    return jsonify({'aws_services': aws_services})

# Route to get a specific AWS service by ID
@app.route('/aws_services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    service = next((s for s in aws_services if s['id'] == service_id), None)
    if service:
        return jsonify(service)
    return jsonify({'error': 'Service not found'}), 404

# Route to add a new AWS service
@app.route('/aws_services/add_service', methods=['POST'])
def add_service():
    data = request.json
    if 'service' in data:
        new_service = {
            'id': len(aws_services) + 1,
            'service': data['service']
        }
        aws_services.append(new_service)
        return jsonify({'message': 'Service added successfully', 'service': new_service}), 201
    return jsonify({'error': 'Service name is required'}), 400

# Route to delete an AWS service by ID
@app.route('/aws_services/delete_service/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    global aws_services
    initial_length = len(aws_services)
    aws_services = [s for s in aws_services if s['id'] != service_id]
    if len(aws_services) < initial_length:
        return jsonify({'message': 'Service deleted successfully'}), 200
    return jsonify({'error': 'Service not found'}), 404

# Route to update an AWS service by ID
@app.route('/aws_services/update_service/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    data = request.json
    service = next((s for s in aws_services if s['id'] == service_id), None)
    if service:
        service['service'] = data.get('service', service['service'])
        return jsonify({'message': 'Service updated successfully', 'service': service}), 200
    return jsonify({'error': 'Service not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
