from flask import Flask, render_template, send_from_directory
import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

app = Flask(__name__)

dir_path = os.path.join('.' + '/batch')

# page load
@app.route("/")
def index():
   return render_template("index.html")

# This will display files from directory
@app.route('/show_images/<path:filename>')
def download_file(filename):
    return send_from_directory(dir_path, filename)

# This loads provided image by html and converts to numpy array and then calls model for prediction
@app.route('/predict/<path:img_name>')
def prediction(img_name):
    img_name = os.path.join(dir_path + '/' + img_name)
    img_nocancer = load_img(img_name, target_size=(50, 50))
    x = img_to_array(img_nocancer)
    x = np.expand_dims(x, axis=0)

    # loading model file
    loaded_model = tf.keras.models.load_model('bca.h5')
    loaded_model.layers[0].input_shape
    images = np.vstack([x])

    # performing prediction
    classes = loaded_model.predict_classes(images, batch_size=10)
    if int(classes[0][0]) == 1:
        # prediction =  { "prediction image ": "Malignant "}
        pred = "Malignant"
        return render_template('image_prediction.html', pred=pred)
    else:
        pred = "Benign"
        return render_template('image_prediction.html', pred=pred)
        # prediction =  { "prediction image ": "Benign "}
    return prediction