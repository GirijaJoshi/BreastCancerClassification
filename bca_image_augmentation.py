#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime
from glob import glob
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tqdm import tqdm
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

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

base_path = 'Resources/IDC_regular_ps50_idx5/'
patient_ids = os.listdir(base_path)

# this to rotate by 40 degrees
datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2)

now = datetime.now()
start_time = now.strftime("%H:%M:%S.%f")
print(f'Start time before Augmentation: {start_time}')

# lets create same number of images in class0 and class1
for pid in tqdm(patient_ids):
    class_0 = os.listdir(base_path + pid + '/0')
    class_1 = os.listdir(base_path + pid + '/1')
    # print(f'PID:{pid}, Class 1 Length:{len(class_1)}, Class 0 Length:{len(class_0)}')

    curr_dir = os.path.join(base_path, pid, '1')
    # print(f'CURRENT PATH:{curr_dir}')
    
    # till class 1 < class 0 continue to augment
    i = 0
    while len(class_1) < len(class_0):
    # while i < 10:
        file_name = os.path.join(curr_dir,class_1[i])
        # print(file_name)
        img = tf.keras.preprocessing.image.load_img(file_name)
        pixels = tf.keras.preprocessing.image.img_to_array(img)
        pixels = pixels.reshape((1,) + pixels.shape)

        # print(f"File:{file_name}, Class_1:{class_1[i]}")
        f_temp = class_1[i].split('.')
        j = 0
        # this loop will run 2 times for each file and save the images in selected folder with
        # aug_ appended to the name.
        for batch in datagen.flow(pixels, 
            batch_size=1, save_to_dir=curr_dir, 
            save_prefix='aug_' + f_temp[0], save_format='png'):
            j += 1
            if j > 3:
                break

        class_0 = os.listdir(base_path + pid + '/0')
        class_1 = os.listdir(base_path + pid + '/1')
        i += 1
    
now = datetime.now()
end_time = now.strftime("%H:%M:%S.%f")
print(f'End Time After Augmentation: {end_time}')