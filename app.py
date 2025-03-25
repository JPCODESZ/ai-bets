from flask import Flask, jsonify, request
from flask_cors import CORS
from logic import get_filtered_bets, place_bet

app = Flask(__name__)
CORS(app)

@app.route("/bets", methods=["GET"])
def bets():
    bets = get_filtered_bets()
    return jsonify(bets)

@app.route("/place-bet", methods=["POST"])
def bet():
    data = request.json
    result = place_bet(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
