from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

board = [""] * 9
current_player = "X"

WIN_PATTERNS = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
]

def check_winner():
    for pattern in WIN_PATTERNS:
        a, b, c = pattern
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def move():
    global current_player

    data = request.json
    position = data["position"]

    if board[position] != "":
        return jsonify({"error": "Position already taken"})

    board[position] = current_player

    winner = check_winner()

    response = {
        "board": board,
        "winner": winner,
        "current_player": current_player
    }

    if not winner:
        current_player = "O" if current_player == "X" else "X"

    response["next_player"] = current_player

    return jsonify(response)

@app.route("/reset", methods=["POST"])
def reset():
    global board, current_player

    board = [""] * 9
    current_player = "X"

    return jsonify({"message": "reset successful"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)