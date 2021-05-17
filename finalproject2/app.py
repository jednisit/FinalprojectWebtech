import config # to hide TMDB API keys
import requests # to make TMDB API calls
import locale # to format currency as USD
locale.setlocale( locale.LC_ALL, '' )

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from urllib.parse import quote
from urllib.request import urlopen
import json
import pandas as pd
import numpy as np
from flask import Flask,jsonify,make_response
from flask_restx import Resource,Api




app = Flask(__name__)
"""api = Api(app)"""

"""----------------------แก้ชื่อไฟล์ตรงนี้มา---------------------"""
f = open('genre.json')
data_music = json.load(f)
print(data_music)

v = open('genre.json')
data_vdo= json.load(v)
print(data_vdo)
"""--------------------------------------------------------"""

@app.route("/")
def home():
   return render_template("main.html",sound=data_music)



@app.route("/video")
def video():
   return render_template("video.html",vdo=data_vdo)

"""@app.route('/video/<title>')
def video(query):
    response = None
    video = None
    try:
        response = requests.request("GET", url, headers=headers, params={"query":query, "number":"1"}).json()
        video = response['videos'][0]['youTubeId']
    except:
        return render_template("video.html", video=-1)
    return render_template("video.html", video=video)"""












app.env="development"
app.run(debug=True)


