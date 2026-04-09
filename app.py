from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chatbot import get_response

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    """Serve the main UI page."""
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    """
    Accept JSON: {"message": "user input"}
    Return JSON: {"response": "bot reply"}
    """
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"response": "Invalid request. Send JSON with a 'message' key."}), 400

    user_message = data["message"]
    bot_reply = get_response(user_message)

    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)