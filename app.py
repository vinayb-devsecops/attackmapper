from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def home():

    with open("data/techniques.json","r") as f:
        techniques = json.load(f)

    search = request.args.get("search","")

    if search:
        techniques = [
            t for t in techniques
            if search.lower() in t["technique"].lower()
            or search.lower() in t["name"].lower()
        ]

    return render_template(
        "index.html",
        techniques=techniques,
        search=search
    )

@app.route("/api/techniques")
def api_techniques():

    with open("data/techniques.json","r") as f:
        return json.load(f)



@app.route("/technique/<technique_id>")
def technique_detail(technique_id):

    with open("data/techniques.json","r") as f:
        techniques = json.load(f)

    for technique in techniques:
        if technique["technique"] == technique_id:
            return render_template(
                "technique_detail.html",
                technique=technique
            )

    return {"error":"Not Found"},404

if __name__ == "__main__":
    app.run(debug=True)
