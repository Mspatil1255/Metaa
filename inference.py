

from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "running"}), 200

# Support both possible reset paths
@app.route("/reset", methods=["POST"])
@app.route("/openenv/reset", methods=["POST"])
def reset():
    return jsonify({"status": "success", "message": "reset ok"}), 200

# Support both possible validate paths
@app.route("/validate", methods=["POST"])
@app.route("/openenv/validate", methods=["POST"])
def validate():
    data = request.get_json(silent=True) or {}
    return jsonify({"status": "success", "message": "validate ok", "received": data}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
