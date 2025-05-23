from flask import Flask, request, jsonify
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify([block.to_dict() for block in blockchain.chain]), 200

@app.route('/mine', methods=['POST'])
def mine_block():
    data = request.json.get('data')
    blockchain.add_block(data)
    return jsonify({'message': 'Block added', 'chain': [b.to_dict() for b in blockchain.chain]}), 201

if __name__ == '__main__':
    app.run(debug=True)
