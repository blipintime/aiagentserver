from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

# In-memory data storage for demonstration
cards = []
customers = []

# GET /api/cards - Retrieve all cards
@app.route('/api/cards', methods=['GET'])
def get_cards():
    return jsonify(cards), 200

# GET /api/cards/<card_id> - Retrieve a specific card by ID
@app.route('/api/cards/<card_id>', methods=['GET'])
def get_card(card_id):
    card = next((card for card in cards if card['id'] == card_id), None)
    if card:
        return jsonify(card), 200
    return jsonify({"error": "Card not found"}), 404

# POST /api/cards - Create a new card
@app.route('/api/cards', methods=['POST'])
def create_card():
    data = request.get_json()
    if not data or 'number' not in data or 'owner' not in data:
        return jsonify({"error": "Missing required fields: number, owner"}), 400
    
    card = {
        'id': str(uuid.uuid4()),
        'number': data['number'],
        'owner': data['owner']
    }
    cards.append(card)
    return jsonify(card), 201

# GET /api/customers - Retrieve all customers
@app.route('/api/customers', methods=['GET'])
def get_customers():
    return jsonify(customers), 200

# GET /api/customers/<customer_id> - Retrieve a specific customer by ID
@app.route('/api/customers/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = next((customer for customer in customers if customer['id'] == customer_id), None)
    if customer:
        return jsonify(customer), 200
    return jsonify({"error": "Customer not found"}), 404

# POST /api/customers - Create a new customer
@app.route('/api/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Missing required fields: name, email"}), 400
    
    customer = {
        'id': str(uuid.uuid4()),
        'name': data['name'],
        'email': data['email']
    }
    customers.append(customer)
    return jsonify(customer), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    