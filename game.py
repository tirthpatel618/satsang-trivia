from flask import Flask, render_template, jsonify
import json
import random

app = Flask(__name__)

# Load mandir data
with open("mandirs.json") as f:
    mandirs = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/question")
def question():
    mandir = random.choice(mandirs)
    correct = mandir["place"]
    all_places = [m["place"] for m in mandirs]

    choices = set()
    choices.add(correct)
    while len(choices) < 4:
        choices.add(random.choice(all_places))
    choices = list(choices)
    random.shuffle(choices)

    return jsonify({
        "image_url": mandir["url"],  # relative path to /static/mandirs/...
        "choices": choices,
        "answer": correct
    })

if __name__ == "__main__":
    app.run(debug=True)
