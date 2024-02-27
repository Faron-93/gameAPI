from flask import Flask, request, jsonify
from data import create_room as cr, get_rooms as gr, find_room as fr

app = Flask(__name__)

@app.route("/")
def home():
    return "elo"

@app.route("/create-room", methods=["POST"])
def create_room():
    try:
        if request.method == "POST":
            data = request.get_json()
            name = data["roomName"]
            number_of_rounds = data["numberOfRounds"]
            number_of_players = data["numberOfPlayers"]
            response = cr(name, number_of_players, number_of_rounds)
            return response, 201
    except:
        info = {
            "roomName": "string",
            "numberOfPlayers": "integer",
            "numberOfRounds": "integer"
        }
        return info

@app.route("/get-rooms", methods=["GET"])
def get_profiles():
    response = gr()
    return jsonify(response), 200

@app.route("/find-room", methods=["POST"])
def find_room():
    if request.method == "POST":
        data = request.get_json()
        name = data["roomName"]
        code = data["code"]
        response = fr(name, code)
        return response, 201

if __name__ == "__main__":
    app.run(debug=True)