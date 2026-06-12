from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():

    with open("data/techniques.json","r") as f:
        techniques = json.load(f)

    return render_template(
        "index.html",
        techniques=techniques
    )

@app.route("/api/techniques")
def api_techniques():

    with open("data/techniques.json","r") as f:
        return json.load(f)

if __name__ == "__main__":
    app.run(debug=True)
