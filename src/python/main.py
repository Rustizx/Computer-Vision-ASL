import numpy as np
import cv2
from flask import Flask, render_template, Response, request

import vision.vision as vision


app = Flask(__name__)
app.config['SECRET_KEY'] = 'np'

camera = cv2.VideoCapture(-1)
fitnessVision = vision.FitnessVision()

@app.route('/video_feed', methods=["POST", "GET"])
def video_feed():
    return Response(fitnessVision.still(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    if request.method == "POST":
        exercise = request.method['name of HTML form ele1ment'] # exercise will be an int value so element val will need to be 0,1,2
        fitnessVision.setExercise(exercise)


    return render_template('index.html')

@app.route('/output')
def output():
    testJSON = {"hello":"world"}
    return testJSON

# WHEN RUNNING FLASK SET UP IN PRODUCTION OR ELSE 2 INSTANCES ARE MADE
# This makes two camera instances which errors out because one is already used
