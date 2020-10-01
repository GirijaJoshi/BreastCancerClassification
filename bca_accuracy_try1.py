#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from glob import glob
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tqdm import tqdm

# getting names of all the files in IDC_regular_ps50_idx5and sub dirs
files = glob('Resources/IDC_regular_ps50_idx5/*/*/*')

# Example : Resources/IDC_regular_ps50_idx5\\10254\\0\\10254_idx5_x1001_y1001_class0.png'
# files

# checking how many are cancer files which has class1 in it
count =0 
for file in files:
   # print(f'-5:{file[-5]}')
   if file[-5] == '1':
       count+=1

print('------------------')

print(f'Number Of 1: {count}')
print(f'Number Of 0: {len(files) - count}')
# total number of files
print(f'Total: {len(files)}')

# create X and y train data

def find_data(files, lower_limit, upper_limit):
    X = []
    y = []
    
    # tqdm(patient_ids)
    for file in tqdm(files[lower_limit:upper_limit]):
        if file.endswith(".png"):
            img = tf.keras.preprocessing.image.load_img(file, target_size = (50,50))
            pixels = tf.keras.preprocessing.image.img_to_array(img)
            pixels /= 255
            X.append(pixels)
            if(file[-5] == '1'):
                y.append(1)
            elif(file[-5] == '0'):
                y.append(0)
    return np.stack(X), y

X_train,y_train = find_data(files,0, 90000)

import seaborn as sns
sns.countplot(y_train)

# get test data
X_test, y_test = find_data(files, 90000, 110000)

sns.countplot(y_test)

def balanced_data(files, size, start_index):
    half_size = int(size/2)
    count=0
    res = []
    y = []
    for file in tqdm(files[start_index:]):
        if (count!=half_size):
            if file[-5] == '1' and file.endswith(".png"):
                img = tf.keras.preprocessing.image.load_img(file, target_size = (50,50))
                pixels = tf.keras.preprocessing.image.img_to_array(img)
                pixels /= 255
                res.append(pixels)
                y.append(1)
                count += 1
                
    for file in tqdm(files[start_index:]):
        if(count!=0):
            if(file[-5] == '0'):
                img = tf.keras.preprocessing.image.load_img(file, target_size = (50,50))
                pixels = tf.keras.preprocessing.image.img_to_array(img)
                pixels /= 255
                res.append(pixels)
                y.append(0)
                count -= 1
    return np.stack(res), y

X_train2, y_train2 = balanced_data(files, 90000,0)

sns.countplot(y_train2)

x_test2, y_test2 = balanced_data(files, 20000, 100000)

sns.countplot(y_test2)

# X_train2 is 4 diemtion we need to convert in 2D
X_train2.shape

from tensorflow import keras
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Dropout, Conv2D, Activation, MaxPooling2D, Flatten, BatchNormalization

def form_model(inp_shape = (50,50,3)):
    inp = Input(inp_shape)
    m = Conv2D(32, (3,3), kernel_initializer='he_uniform', padding="same", activation='relu')(inp)
    m = MaxPooling2D(2)(m)
    # m = BatchNormalization()(m)
    
    m = Conv2D(64, (3,3), kernel_initializer='he_uniform', padding="same", activation='relu')(m)
    m = MaxPooling2D(2)(m)
    # m = BatchNormalization()(m)
    
    m = Conv2D(128, (3,3), kernel_initializer='he_uniform', padding="same", activation='relu')(m)
    m = MaxPooling2D(2)(m)
    
    m = Conv2D(128, (3,3), kernel_initializer='he_uniform', padding="same", activation='relu')(m)
    m = MaxPooling2D(2)(m)
    
    
    m = Conv2D(256, (3,3), kernel_initializer='he_uniform', padding="same", activation='relu')(m)
    m = MaxPooling2D(2)(m)
    
    # m = BatchNormalization()(m)
    
    # m = MaxPooling2D(2)(m)
    m = Flatten()(m)
    
    m = Dense(128, activation = "relu")(m)
    out = Dense(1, activation = "sigmoid")(m)
    model = Model(inp, out)
    model.compile(optimizer = keras.optimizers.SGD(1e-3, momentum=0.9), loss="binary_crossentropy", metrics = ['acc'])
    return model

model = form_model()
model.summary()

history = model.fit(X_train2, y_train2, validation_data=(x_test2, y_test2), epochs = 25, batch_size=256)

# evaluating and printing results 
score = model.evaluate(x_test2, y_test2, verbose = 0) 
print('Test loss:', score[0]) 
print('Test accuracy:', score[1]) 

# from keras.preprocessing.image import ImageDataGenerator

# datagen = ImageDataGenerator(height_shift_range=0.2,
#                             width_shift_range=0.2,
#                             zoom_range=0.2,
#                             shear_range=0.2)


# train_generator = datagen.flow(X_train2, y_train2, batch_size=256)
# val_generator = datagen.flow(x_test2, y_test2, batch_size=256)

# history2 = model2.fit(train_generator, validation_data=val_generator, epochs = 15)

# pred = model.predict(x_test2)

# res = []
# for prediction in pred:
#     if(prediction > 0.5):
#         res.append(1)
#     else:
#         res.append(0)


# from sklearn.metrics import classification_report, confusion_matrix
# print(confusion_matrix(y_test2, res))
# print(classification_report(y_test2, res))
