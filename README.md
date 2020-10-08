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

## Data Exploration##

### Breat Histopathology Images ###

Extracted X, Y Patient ID and target feature from image path to create initial dataset. Cancer Diagnosis (1) group was disproportionately small (1→  78, 716 ; 2 → 198,259); to fix this we performed data augmentation by rotating images Cancer Diagnosis 40 degrees. New data has 208,984 cancer diagnosis and 198,259 no cancer diagnosis. New datasets was too large to process in personal computers; so we decided to under sample for the machine learning model.

### Risk Factor Analysis ###

Original data sets were divided in three different CVS tables; we performed vertical concatenation to have one DF. There are 19,790,420 rows, 13 columns and no null values. Data has already been encoded, all data are integers, so there are no transformations needed.

## Machine Learning Model ##

### Model Selection: ###

Using the Breast Histopathology Images create a classification model using a deep neural network to predict if tumor is benign or malign.

The Deep Neural Network has three hidden layers with 32, 64 and 128 nodes respectively; totaling a number of 683,329 parameters. The initial accuracy score is 83%. All hidden layers are using relu activation functions and the output layer is using a sigmoid function.

### Feature Selection: ###

Using the Keras Preprocessing Image package; images are converted to arrays that contains information about position and color. The models trained to detect patterns that are cancerous and noncancerous based of these features.

### Limitations: ###
* Memory: To rin the model the server needs 10 GB of free memory 
* Time: Model processing with under sampled data runs for 6 + hours on a personal computer

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
