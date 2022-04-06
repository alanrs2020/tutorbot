from flask import Flask, jsonify, request
import time
import bot as bot

app = Flask(__name__)


@app.route("/tutorbot", methods=["POST"])
def response():
    print(dict(request.json))
    query = dict(request.json)['query']
    result = bot.chat(query)

    return jsonify({"response": result+" "+time.ctime()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", )
