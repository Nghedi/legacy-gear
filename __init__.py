from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/base_layout.html")
def base_layout():
        return render_template("base_layout.html")

@app.route("/items")
def GetData():
        f = open('data/gear/resto-shaman.json', 'r')
        daten = json.load(f)
        columns = ["Stam", "Agi"]
        return render_template("items.html", records=daten, colnames=columns, website="https://tbc.cavernoftime.com")


@app.route('/')
def index():
    return 'Hello World!'

if __name__ == "__main__":
    app.run(debug=True)
