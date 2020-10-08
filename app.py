from flask import Flask, render_template, send_from_directory
import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

app = Flask(__name__)

# img1 = os.path.join('C:\BootCamp\BreastCancerClassification' + '/batch/8863_idx5_x51_y1251_class0.png' )
# img1 = os.path.join('C:\BootCamp\BreastCancerClassification' + '/batch/16570_idx5_x1451_y951_class1.png' )
dir_path = os.path.join('C:\BootCamp\BreastCancerClassification' + '/batch')

@app.route("/")
def index():
   return render_template("index.html")

@app.route('/show_images/<path:filename>')
def download_file(filename):
    # filename = os.path.join(dir_path + '/' + filename)
    # return send_from_directory(dir_path, filename=img_name)
    # prediction =  { "image ": "show "}
    # return prediction
    return send_from_directory(dir_path, filename)

@app.route('/predict/<path:img_name>')
def prediction(img_name):
    img_name = os.path.join(dir_path + '/' + img_name)
    img_nocancer = load_img(img_name, target_size=(50, 50))
    x = img_to_array(img_nocancer)
    x = np.expand_dims(x, axis=0)

    # loaded_model = tf.keras.models.load_model('bca_orig.h5')
    loaded_model = tf.keras.models.load_model('bca_1.h5')
    loaded_model.layers[0].input_shape

    images = np.vstack([x])
    classes = loaded_model.predict_classes(images, batch_size=10)
    # prediction =  { "prediction image 1": int(classes[0][0]), "prediction image 2": int(classes[1][0]) }
    if int(classes[0][0]) == 1:
        prediction =  { "prediction image ": "Malignant "}
    else:
        prediction =  { "prediction image ": "Benign "}
    return prediction

@app.route('/guess')
def guessing():
    img1 = os.path.join('C:\BootCamp\BreastCancerClassification' + '/batch/9382_idx5_x901_y1501_class1.png' )

    img_nocancer = load_img(img1, target_size=(50, 50))
    x = img_to_array(img_nocancer)
    # print(x)
    x = np.expand_dims(x, axis=0)
    # print(type(x))
    # print(x)

    loaded_model = tf.keras.models.load_model('bca_orig.h5')
    loaded_model.layers[0].input_shape

    images = np.vstack([x])
    # print(images)
    classes = loaded_model.predict_classes(images, batch_size=5)
    print(classes)
    print(img1)
    pred =  { "prediction New ": int(classes[0][0]) }
    # # prediction =  { "prediction image 1": int(classes[0][0]), "prediction image 2": int(classes[1][0]) }
    # if int(classes[0][0]) == 1:
    #     prediction =  { "prediction image ": "Malignant "}
    # else:
    #     prediction =  { "prediction image ": "Benign "}
    return pred


