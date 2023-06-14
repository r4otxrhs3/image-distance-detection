from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField,validators
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
import cv2
import requests
import json
app= Flask(__name__)
# Load the pre-trained YOLO model and class labels

with open('coco.names', 'r') as f:
    classes = f.read().splitlines()

# Function to calculate distance between two points


def calculate_distance(x1, y1, x2, y2, width):
    # Assuming a known object width and focal length of the camera
    known_width = 0.15  # meters
    focal_length = 500  # pixels

    # Calculate distance
    distance = (known_width * focal_length) / width

    return distance

# Function to perform object detection and measure distance


def detect_and_measure_distance(image_path):
    image = cv2.imread(image_path)
    blob = cv2.dnn.blobFromImage(
        image, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward(net.getUnconnectedOutLayersNames())

    # Rest of the object detection and measurement code...

# Flask route for the home page


# Flask route to handle file uploads


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file_path = 'uploads/' + file.filename
    file.save(file_path)

    detect_and_measure_distance(file_path)

    return 'Object detection and distance measurement completed.'

app.config['SECRET_KEY']= 'supersecretkey'
app.config['UPLOAD_FOLDER']= 'static/files'

class UploadFileForm(FlaskForm):
    file= FileField("File", validators=[InputRequired()])
    submit= SubmitField("Upload File")
@app.route("/", methods=['GET', "POST"])
@app.route('/home', methods=['GET', "POST"])
def home():
    form= UploadFileForm()
    if form.validate_on_submit():
        file= form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        return "File has been uploaded"
    return render_template("imagedetection.html", form=form)



if __name__== '__main__':
    app.run(debug=True)