# Breast Cancer Classification Model & Risk Factor Analysis #

## Project Overview ##

Analyze Breast Cancer Risk Factor Dataset for the creation of a dashboard with graphical representation of features like age, race, familial breast cancer history, and others.

Using Deep Neural Network we will create a breast cancer screening model for Invasive Ductal Carcinoma (IDC). The classifier will  predict image histology as benign or malignant. 

## Why are we interested in this? ##

Breast cancer is the most common cancer in women worldwide; it is estimated that 276,480 new cases of invasive breast cancer will be diagnosed in women in the US. Approximately 30% of all new cancer diagnosis will be breast cancer.

Other statistics reveal that 1 in 8 women will be diagnosed with breast cancer through their lifetime.

According to the American Cancer Society, the 5-year relative survival rate is 99%. A Mammogram is an x-ray that allows qualified specialists to examine breast tissue for any suspicious areas. By training computers with high sensitivity, the cost of mammograms can decrease as the model will advice you to go to the doctor if there is suspicious of a malignant mass.

## Data Source ##

### Risk Factor Dataset ###

Source:
[Risk Factor Dataset](https://www.bcsc-research.org/data/rf/risk-factor-dataset-download)

The data set contains 1,522,340 records, representing information from 6,788,436 mammograms. Collected between 2005- 2017, and selected one exam per women per calendar year and year of age.

All data features are encoded; [Data documentation](https://www.bcsc-research.org/data/rf/documentation)

Citation: Data collection and sharing was supported by the National Cancer Institute (P01CA154292; U54CA163303), the Patient-Centered Outcomes Research Institute (PCS-1504-30370), and the Agency for Health Research and Quality (R01 HS018366-01A1). We thank the participating women, mammography facilities, and radiologists for the data they have provided for this study. You can learn more about the BCSC at: http://www.bcsc-research.org/.

### Breast Histopathology images ###

Source:
[Breast Histopathology Images](https://www.kaggle.com/paultimothymooney/breast-histopathology-images/)

The original dataset was formed of 162 whole mount slides of Breast Cancer specimen, 277534 patches of 50 x 50 images were extracted; 198,738 IDC negative and 78,786 IDC positive. All files are images, with the file name in following format:

    e.g. uxXyYclassC.png → 8975_idx5_x51_y1101_class0.png
    
starting with patient id (8975_idx5), then X and Y are the coordinates where the patch were cropped from, and C indicates class: 0 is non-IDC and 1 is IDC

## Goals / Questions ##

* Create an interactive dashboard to promote understanding of risk factors and its distributions.  
* Promote breast cancer awareness, and early detection practices; traditional examination techinques and modern computer aided techniques.
* Leverage Deep Neural Network (DNN/CNN) Machine Learning Models to aid analysis and detection of Breast Cancer via Mammogram image analysis.
* What are some of the most important risk factors to the development of breast cancer?
* Can mammograms be analyzed by computers to aid in breast cancer detection?

### Task Distribution & Technology Use ###

Primary roles: 
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
