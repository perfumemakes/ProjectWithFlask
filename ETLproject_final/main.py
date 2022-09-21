# mian.py

from flask import Flask, request, render_template
from dao import CovidDAO
import json

app = Flask(__name__)

# intro
@app.route("/")
def intro():
    return render_template("covid.html")

# 데이터 셋 전체 조회
@app.route("/show", methods=['post'])
def show():
    covidDao = CovidDAO()
    covidDao = covidDao.covidSelect()
    data = json.dumps(covidDao)

    return data

# 특정 나라의 데이터 조회
@app.route("/select", methods=['post'])
def select():
    c = request.form.get("country")
    covidDao = CovidDAO()
    result = covidDao.covidSelectOne(c)

    return render_template("result.html", data=result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)