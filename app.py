from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from bucin.generative_text_bucin.chat import get_response
import os

app = Flask(__name__, static_folder='static')
CORS(app)

# Serve assets directory
@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory(os.path.join('bucin', 'assets'), filename)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').strip()
    
    if not user_message:
        return jsonify({'error': 'Message field is required'}), 400

    response = get_response(user_message)

    if 'error' in response:
        return jsonify({'error': response['error']}), 500

    return jsonify({'response': response['response']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
