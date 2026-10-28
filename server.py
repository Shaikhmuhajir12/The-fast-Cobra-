
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "app": "The Fast Cobra Downloader",
        "status": "online",
        "message": "Backend is running"
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok"
    }), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

