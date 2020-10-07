# Breast Cancer Classification Model & Risk Factor Analysis #

## Project Overview ##

Analyze Breast Cancer Risk Factor Dataset for the creation of a dashboard with graphical representation of features like age, race, familial breast cancer history, and others.

Using Deep Neural Network we will create a breast cancer screening model for Invasive Ductal Carcinoma (IDC). The classifier will  predict image histology as benign or malignant. 

## Why are we interested in this? ##

Breast cancer is the most common cancer in women worldwide; it is estimated that 276,480 new cases of invasive breast cancer will be diagnosed in women in the US. Approximately 30% of all new diagnosis will be breast cancer.

Other statistics reveal that 1 in 8 women will be diagnosed through their lifetime.

According to the American Cancer Society, early detection (Stage 1) has a 5-year relative survival rate is 99%. One of the ways to help early detection is by Mammogram, an x-ray that allows qualified specialists to examine breast tissue for any suspicious areas. By training computers with image interpretation machine learning, the effectiveness and rate of mammograms can increase as interpretation is aided by machine learning algorithm where its not humanly possible. We hope this project can contribute to the society in general.

## Data Source ##

### Risk Factor Dataset ###

Source:
[Risk Factor Dataset](https://www.bcsc-research.org/data/rf/risk-factor-dataset-download)

The data set contains 1,522,340 records, representing 6,788,436 mammograms. Collected between 2005- 2017, and selected one exam per women per calendar year and year of age.

All features are encoded; documentation [link:] (https://www.bcsc-research.org/data/rf/documentation)

### Breast Histopathology images ###

Source:
[Breast Histopathology Images](https://www.kaggle.com/paultimothymooney/breast-histopathology-images/)

The original dataset was formed of 162 whole mount slides of Breast Cancer specimen, 277534 patches of 50 x 50 images were extracted; 198,738 IDC negative and 78,786 IDC positive. The patients file name is in the format:

    uxXyYclassC.png → 10253idx5

X and Y are the coordinates where the patch were cropped from and C indicates class: 0 is non-IDC and 1 is IDC

## Questions ##
 
* What are some of the most important risk factors to the development of breast cancer
* Can Deep Neural Machine Learning Model analyze mammogram images to detect Breast Cancer?
* Can mammograms be analyzed by computers to send alert messages and request a visit with a specialist 

## Data Exploration ##

Data sets downloaded were mostly clean and ready for analysis 

### Breast Histopathology Images ###

Breast Histopathology Images: Extracted X, Y Patient ID and target feature from image path to create initial dataset. Cancer Diagnosis (1) group was disproportionately small (1→  78, 716 ; 2 → 198,259); to fix this we performed data augmentation by rotating images Cancer Diagnosis 40 degrees. New data has 208,984 cancer diagnosis and 198,259 no cancer diagnosis. New datasets was difficult to process; so we decided to under sample for the machine learning model.

### Risk Factor Analysis ###

Data sets were divided in three different CVS tables; we performed vertical concatenation to have one DF. There are 19,790,420 rows, 13 columns and no null values. Data has already been encoded, all data are integers, so there are no transformations needed.

## Analysis of the Project ##

Breast Histopathology images are converted to pixels and RGB is stored in an array. Array is fed to the Machine Learning Model

Risk Factor initial development of graphs and visualization to analyze data and story tell. Group may decide to develop a machine learning model to find most important features correlated with breast cancer diagnosis.

## Machine Learning Model ##

### Model Selection ###

Using the Breast Histopathology Images create a classification model using a deep neural network to predict if tumor is benign or malign.


The Deep Neural Network has three hidden layers with 32, 64 and 128 nodes respectively; totaling a number of 683,329 parameters. The initial accuracy score is 83%. All hidden layers are using relu activation functions and the output layer is using a sigmoid function.

### Feature Selection ### 

* Ana: 

Using the Keras Preprocessing Image package; images are converted to arrays that contains information about position and color. The models trained to detect patterns that are cancerous and noncancerous based off these features.

### Limitations ### 

* Memory: To run the model the server needs 10 GB of free memory
* Time: Model processing with current data takes 6 + hours to run on a personal computer 

### Task Distribution & Technology Use ###

* Presentation - Ana (Readme.md) & all team members will participate in feature selection analysis and decision making process
* Data Processing & Modeling - Girija (Python)
* Database - Mauricio (postgres)
* Dashboard:
	* HTML (Blueprint: Ana, Code: Tien & Ana)
	* Tableau (Hannah) 

## Upcoming tasks ##
-[ ] Assess sensitivity and optimize model to desired level of accuracy
-[ ] Flask application for machine learning model 
-[ ] Static database and scraping interactions with existing code 
-[ ] Execute blueprints of dashboards in HTML and Tableau

## Communication and More Information ##

We are currently communicating through a Slack channel (name: #finalproject); and have created a Google Drive Folder to store presentation templetes and meeting minutes.
[Link] (https://drive.google.com/drive/folders/1LaX9KnGGwv2Lf1l9v83TqIOjVzP_935L)