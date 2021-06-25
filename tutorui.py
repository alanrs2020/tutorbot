from flask import Flask, jsonify, request
import time
import main as bot

app = Flask(__name__)


@app.route("/tutorbot", method=["POST"])
def response():
    query = dict(request.form)["query"]
    result = bot.getMessage(query)
    return jsonify({"response": result+" "+time.ctime()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", )
