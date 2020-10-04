# Breast Cancer Classification Model & Risk Factor Analysis #

## Project Overview ##

Analyze Breast Cancer Risk Factor Dataset for the creation of a dashboard with graphical representation of features like age, race, familial breast cancer history, and others.

Using Deep Neural Network we will create a breast cancer screening model for Invasive Ductal Carcinoma (IDC). The classifier will  predict image histology as benign or malignant. 

## Why are we interested in this? ##

Breast cancer is the most common cancer in women worldwide; it is estimated that 276,480 new cases of invasive breast cancer will be diagnosed in women in the US. Approximately 30% of all new cancer diagnosis will be breast cancer.

Other statistics reveal that 1 in 8 women will be diagnosed with breast cancer through their lifetime.

According to the American Cancer Society, early detection (Stage 1) has a 5-year relative survival rate is 99%.  One of the ways to help early detection is by Mammogram, an x-ray that allows qualified specialists to examine breast tissue for any suspicious areas. By training computers with image interpretation machine learning, the effectiveness and rate of mammograms can increase as interpretation is aided by machine learning algorithm where its not humanly possible.  We hope this  project can contribute to the society in general.  

## Data Source ##

### Risk Factor Dataset ###

Source:
[Risk Factor Dataset](https://www.bcsc-research.org/data/rf/risk-factor-dataset-download)

The data set contains 1,522,340 records, representing 6,788,436 mammograms. Collected between 2005- 2017, and selected one exam per women per calendar year and year of age.

All features are encoded; [Data documentation](https://www.bcsc-research.org/data/rf/documentation)

### Breast Histopathology images ###

Source:
[Breast Histopathology Images](https://www.kaggle.com/paultimothymooney/breast-histopathology-images/)

The original dataset was formed of 162 whole mount slides of Breast Cancer specimen, 277534 patches of 50 x 50 images were extracted; 198,738 IDC negative and 78,786 IDC positive. The patients file name is in the format:

    uxXyYclassC.png → 10253idx5
    
X and Y are the coordinates where the patch were cropped from and C indicates class: 0 is non-IDC and 1 is IDC

## Goals/ Questions ##

* Understanding risk factors distributions to promote early detection practices; breast self exam, clinical breast exam and mammogram 
* Deep Neural Machine Learning Model to analyze mammograms and detect Breast Cancer
* What are some of the most important risk factors to the development of breast cancer?
* Can mammograms be analyzed by computers to send alert messages and request a visit with a specialist?

### Task Distribution & Technology Use ###

* Presentation - Ana (Google Slides & Readme.md)
* Initial Data Processing - Girija & Tien (Python)
* Database - Hannah & Mauricio (postgres)

## Upcoming tasks ##
- [ ] Design a dashboard layout to represent data and story tell
- [ ] Initial machine learning model
    - [ ] Assess sensitivity and optimize model to desired level of accuracy
- [ ] Store clean and complete dataset in DB for future use in the analysis and storytelling 

## Communication and More Information ##

We are currently communicating through a Slack channel (name: #finalproject); and have created a Google Drive Folder to store presentation templetes and meeting minutes.
[link](https://drive.google.com/drive/folders/1LaX9KnGGwv2Lf1l9v83TqIOjVzP_935L)
