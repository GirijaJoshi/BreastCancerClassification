# Breast Cancer Classification Model & Risk Factor Analysis #

## Project Overview ##

Analyze Breast Cancer Risk Factor Dataset for the creation of a dashboard with graphical representation of features like age, race, familial breast cancer history, and others.

Using Deep Neural Network we will create a breast cancer screening model for Invasive Ductal Carcinoma (IDC). The classifier will  predict image histology as benign or malignant. 

## Why are we interested in this? ##

Breast cancer is the most common cancer in women worldwide; it is estimated that 276,480 new cases of invasive breast cancer will be diagnosed in women in the US. Approximately 30% of all new cancer diagnosis will be breast cancer.

Other statistics reveal that 1 in 8 women will be diagnosed with breast cancer through their lifetime.

According to the American Cancer Society, early detection (Stage 1) has a 5-year relative survival rate is 99%.  One of the ways to help early detection is by Mammogram, an x-ray that allows qualified specialists to examine breast tissue for any suspicious areas. By training computers with image interpretation machine learning, the effectiveness and rate of mammograms can increase as interpretation is aided by machine learning algorithm where its not humanly possible.  We hope this  project can contribute to the society in general.  

## Data Source ##

### Breast Cancer Wisconsin (Diagnostic) ###

Source:
[data.csv](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29)

The data set contains 569 instances; features come from a digitalized image of a fine needle aspiration (FNA) of breast mass. They provide a description of the characteristic of the cell nuclei present in the image. There are 14 feature including ID number and mass diagnosis (malignant or bening).This data set will help us better understand IDC mammogram images.

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
    
Starting with patient id (8975_idx5), then X and Y are the coordinates where the patch were cropped from, and C indicates class: 0 is non-IDC and 1 is IDC

## Goals / Questions ##

* Create an interactive dashboard to promote understanding of risk factors and its distributions.  
* Promote breast cancer awareness, and early detection practices; traditional examination techinques and modern computer aided techniques.
* Leverage Deep Neural Network (DNN/CNN) Machine Learning Models to aid analysis and detection of Breast Cancer via Mammogram image analysis.
* What are some of the most important risk factors to the development of breast cancer?
* Can mammograms be analyzed by computers to aid in breast cancer detection?

## Data Exploration ##

### Breat Histopathology Images ###

Extracted X, Y Patient ID and target feature from image path to create initial dataset. Cancer Diagnosis (1) group was disproportionately small (1→  78, 716 ; 2 → 198,259).
![Data before Augmentation](https://github.com/GirijaJoshi/BreastCancerClassification/blob/master/Images/num_img_before_downsampling.PNG)
To fix this we performed data augmentation by rotating images Cancer Diagnosis 40 degrees. New data has 208,984 cancer diagnosis and 198,259 no cancer diagnosis.

### Risk Factor Analysis ###

Original data sets were divided in three different CVS tables; we performed vertical concatenation to have one DF. There are 19,790,420 rows, 13 columns and no null values. Data has already been encoded, all data are integers, so there are no transformations needed.

## Machine Learning Model ##

### Model Selection: ###

Using the Breast Histopathology Images create a classification model using a Deep Neural Network to predict if tumor is benign or malign. A Convolutional Neural Network, is the most effective tool found fo the task of image recognition; the model can efficiently process, correlate and understand the large amount of data in high-resolution images.

## Our Model ## 

After image augmentation data set had too many images and could not be processed; the group decided to downsample. Used 109,404 images for training and 27,352 images for testing with similar numbers of cancerous and non-cancerous images.

![Image count after Downsampling](https://github.com/GirijaJoshi/BreastCancerClassification/blob/master/Images/num_img_after_downsampling.PNG)

To increase accuracy; model architecture is designed in a bottle neck; the Convolutional Neural Network will stablish a predictive model that classify the features of the image and can improve accuracy scores and F-scores.
The Deep Neural Network has three hidden layers with 32, 64 and 128 nodes respectively; totaling a number of 683,329 parameters. The initial precision score is 86% and accuracy (F-Score) 83%. All hidden layers are using relu activation functions and the output layer is using a sigmoid function.

### Feature Selection: ###

Using the Keras Preprocessing Image package; images are converted to arrays that contains information about position and color. The models trained to detect patterns that are cancerous and noncancerous based of these features.

* Image Size: Used original image size 50 x 50 pixels. The data was clean and with consistent format.

* Image Type: Mammograms png are used to train the model in the 50 x 50 format. Same image format is needed to make predictions. 

* Number of images: 136,756 images; there was an initial imbalance between cancerous and noncancerous images. We maximize the number of images by undersampling the non cancerous group to match number of images of the cancerous group.

* Color: 3 color channels RGB (Red, Blue, Green).

![Cancerous Images](https://github.com/GirijaJoshi/BreastCancerClassification/blob/master/Images/Cancer_images.png)
![Non Cancerous Images](https://github.com/GirijaJoshi/BreastCancerClassification/blob/master/Images/non_cancer_images.png)

### Limitations: ###
* Memory: To rin the model the server needs 10 GB of free memory 
* Time: Model processing with under sampled data runs for 6 + hours on a personal computer

## Dashboard Blueprint ## 

The team will create a story board using Tableu to create a narrative on Breast Cancer Risk factorr and demographics. User can interact by clicking and to check which are the features that they want to observe and the division between cancerous and noncancerous. In the Tableus dashboard we will enbed an HTML file to run the ML model and do predictions of mammograms in real time. 

Blueprint can be found in Google Slide Presentation

## Technologies, Languages, Tools and Algorithms ##

The technologies used for the project are Heroku, Tableau, and Github. Heroku is being used to host the Machine Learning model and make life predictions on real mammograms. Tableau is used to create a story and dashboards showing graphs on all our datasets. Finally Github has been central for the group project nad will be used to host final webpage. 

The code uses of python, HTML, Javascript and SQL. Different langiuages are used for different tasks; machine learning model and Initial data exploration is coded in python; SQL was used to code database; and, Javascript and HTML for the webpage application. 

Algorithms were used for the machine learning models which uses depp learning neural network, CNN and a Random Forest Classifier.

## Results of the analysis ##
### Risk Factor Analysis ###
Risk factor visualizations and simple machine learning model show that major risk factors are related to natural femenine hormonal changes and menstrual cycles. Some other important contributors for the development of breast cancer are related to familial disease history; and, age. 

### Breast Histopathology Images ###
Convolutional Neural Network and Image processing of 136,756 mammogram images we achieved an accuracy score of 83% with balanced accuracy for positive and negative predictions. Other studies using the same data have only achieved 76% accuracy. We have attached the summary statistics of machine learning model.


## Presentation Link ##
[Google Slides Storyboard Link](https://docs.google.com/presentation/d/1gjYlYHoC6UKUpj6zE0XUGuknyy2YOyjtKmNX8WKn3Xw/edit?usp=sharing)

## Dashboards ##

### Tableau ### 
[Presentation Dashboard](https://public.tableau.com/profile/hannah1209#!/vizhome/BreastCancerClassification_Tableau/TitleSlide?publish=yes)

### HTML ###

[Beat Breast Cancer](https://github.com/GirijaJoshi/BreastCancerClassification/tree/Tien-HTML1)

## Recommendation for future analysis ## 

* Risk Factor Dataset can be changed for a more general dataset that includes women and men. It would be ideal to conduct an analysis of a longitudinal data set to closely observe the transformation of some of the features and how they may lead to cancer diagnosis. 

* CNN Machine Learning Model should have a greater positive predictive accuracy score. Because this has a medical application, we should aspite to have above 98% 99% accuracy for TRUE POTIVES. Model optimization can be done through better feature selection, increasing training and testing images, and/or adding more hidden layers to the model architecture. We plan to keep improving the model. 

* Web app can be used as a screening tool at medical center to direct patients to specialist. We need to adapt the code to allow users to upload mammograms.

## Communication and More Information ##

We are currently communicating through a Slack channel (name: #finalproject); and have created a Google Drive Folder to store presentation templetes and meeting minutes.
[link](https://drive.google.com/drive/folders/1LaX9KnGGwv2Lf1l9v83TqIOjVzP_935L)
