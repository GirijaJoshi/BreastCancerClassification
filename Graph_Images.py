#!/usr/bin/env python
# coding: utf-8

import os
from pprint import pprint
from tqdm import tqdm
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from IPython.display import display
from sklearn.model_selection import train_test_split


# create a Resources/temp/original in current directory
files = os.listdir("Resources/IDC_regular_ps50_idx5")
# print('Patient IDs')
# print(files)


base_path = 'Resources/IDC_regular_ps50_idx5/'
patient_ids = os.listdir(base_path)
# print(f'PIDS: {patient_ids}')


class_0_total = 0
class_1_total = 0


now = datetime.now()
start_filename = now.strftime("%H:%M:%S.%f")
print(f'Start Reading All File Names: {start_filename}')

# reading all file names with all the folders and sub folders
for patient_id in patient_ids:
    class_0_files = os.listdir(base_path + patient_id + '/0')
    class_1_files = os.listdir(base_path + patient_id + '/1')

    class_0_total += len(class_0_files)
    class_1_total += len(class_1_files) 

total_images = class_0_total + class_1_total
    
print(f'Number of patches in Class 0: {class_0_total}')
print(f'Number of patches in Class 1: {class_1_total}')
print(f'Total number of patches: {total_images}')

now = datetime.now()
end_filename = now.strftime("%H:%M:%S.%f")
print(f'End Reading All File Names: {end_filename}')


columns = ["patient_id",'x_cordinate','y_cordinate',"target","path"]
data_rows = []
i = 0
iss = 0
isss = 0


# getting path name of all the images
for patient_id in tqdm(patient_ids):
    for c in [0,1]:
        
        class_path = base_path + patient_id + '/' + str(c) + '/'
        # print(class_path)

        # get all image file names
        imgs = os.listdir(class_path)
        # print(f'Images:{imgs}')
        
        # Extracting Image Paths
        img_paths = [class_path + img + '/' for img in imgs]
        # print(f'Image Path: {img_paths} ')

        

        # Get image cordinates
        img_coords = [img.split('_',4)[2:4] for img in imgs]
        x_coords = [int(coords[0][1:]) for coords in img_coords]
        y_coords = [int(coords[1][1:]) for coords in img_coords]

        for (path,x,y) in zip(img_paths,x_coords,y_coords):
            values = [patient_id,x,y,c,path]
            data_rows.append({k:v for (k,v) in zip(columns,values)})


data = pd.DataFrame(data_rows)
print(data)

print(f'Shape: {data.shape}')

def get_classes_split(series):
    ratio = np.round(series.value_counts()/series.count()*100,decimals = 1)
    return ratio


import random
# shuffling the data
def suffle_patient_ids(data_frame):
    patient_groups = [df for _, df in data_frame.groupby('patient_id')]
    random.shuffle(patient_groups)
    shuffled_df = pd.concat(patient_groups).reset_index(drop=True)
    return shuffled_df


from sklearn.model_selection import train_test_split
for i in range(3):
    data = suffle_patient_ids(data)
    display(data.head())

print(f"PERCENT of Split: \n{get_classes_split(data['target'])}")

# Create test and train data
X = data.drop(drop(columns=["EIN","NAME"]))
print(X)

# # check the visual difference between cancerous cells
# positive_cells = np.random.choice(data[data.target == 1].index.values, size = 100, replace=False)
# negative_cells = np.random.choice(data[data.target == 0].index.values, size = 100, replace=False)

# num_rows = 10
# num_cols = 10


# # plot patches
# fig,ax = plt.subplots(num_rows,num_cols,figsize = (30,30))

# for row in tqdm(range(num_rows)):
#     for col in range(num_cols):
#         idx = positive_cells[col + num_cols*row]
#         img = io.imread(data.loc[idx, "path"])
#         ax[row,col].imshow(img[:,:,:])
#         ax[row,col].grid(False)

# fig,ax = plt.subplots(num_rows,num_cols,figsize = (30,30))

# for row in tqdm(range(num_rows)):
#     for col in range(num_cols):
#         idx = negative_cells[col + num_cols*row]
#         img = io.imread(data.loc[idx, "path"])
#         ax[row,col].imshow(img[:,:,:])
#         ax[row,col].grid(False)
