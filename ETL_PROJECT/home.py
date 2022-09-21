from flask import Flask, request, render_template
from dao import covidDAO
import json

app = Flask(__name__)

@app.route("/")
def intro():
    return render_template("view.html")

@app.route("/show", methods=['post'])
def show():
    list_data = covidDAO().get()
    data = json.dumps(list_data)
    return data

@app.route("/select", methods=['post'])
def search1():
    country = request.form.get("country")
    data = covidDAO().select(country)
    return data

@app.route("/search", methods=['post'])
def search2():
    country = request.form.get("country")
    result = covidDAO().select(country)
    return render_template("result.html", data = result )

if __name__=="__main__":
    app.run(debug=True)