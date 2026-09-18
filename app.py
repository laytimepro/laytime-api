from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"status": "LIVE", "message": "Laytime Pro API Running"})

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    allowed = float(data.get('laytime_allowed', 0))
    used = float(data.get('time_used', 0))
    return jsonify({"success": True, "demurrage": max(0, used-allowed), "despatch": max(0, allowed-used)})

if __name__ == '__main__':
    app.run()
