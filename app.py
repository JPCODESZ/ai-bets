from flask import Flask, jsonify, request
from logic import get_filtered_bets, place_bet
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "ok", "message": "AI Bets API is running"}), 200

@app.route("/bets")
def bets():
    # Get the filtered bets (up to 20)
    bets = get_filtered_bets(limit=20)
    print(f"📦 Returning {len(bets)} bets")
    return jsonify(bets)

@app.route("/place-bet", methods=["POST"])
def bet():
    data = request.json
    if not data or "team" not in data or "odds" not in data:
        return jsonify({"error": "Invalid request"}), 400
    result = place_bet(data)
    return jsonify(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"✅ Starting server on port {port}")
    app.run(host="0.0.0.0", port=port)
