from flask import Flask, jsonify, request

import bot

app = Flask(__name__)


@app.route("/tutorbot", methods=["POST"])
def response():
    print(dict(request.json))
    query = dict(request.json)['query']
    result = bot.chat(query)

    return jsonify({"response": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=3030)
