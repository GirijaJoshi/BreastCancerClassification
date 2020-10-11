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


### Task Distribution & Technology Use ###

* Presentation - Ana (Readme.md) & all team members will participate in feature selection analysis and decision making process
* Data Processing and Modeling- Girija
* Database -  Mauricio
* Dashboard- Tien & Ana (HTML), Hannah (Tableau)

## Upcoming tasks ##
- [ ] Assess sensitivity and optimize model to desired level of accuracy
- [ ] Flask application for machine learning model
- [ ] Static database and scraping interactions with existing code
- [ ] Execute blueprints of dashboards in HTML and Tableau

## Presentation Link ##
[Link](https://docs.google.com/presentation/d/1gjYlYHoC6UKUpj6zE0XUGuknyy2YOyjtKmNX8WKn3Xw/edit?usp=sharing)
## Communication and More Information ##

We are currently communicating through a Slack channel (name: #finalproject); and have created a Google Drive Folder to store presentation templetes and meeting minutes.
[link](https://drive.google.com/drive/folders/1LaX9KnGGwv2Lf1l9v83TqIOjVzP_935L)
