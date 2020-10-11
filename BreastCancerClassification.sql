-- Creating table for Breast Cancer Indicator
-- Based on SCHEMA created by Hannah

-- Create table for data set
-- Perform table merge in Python ETL
CREATE TABLE indicators1 (
	calendar_year VARCHAR(4) NOT NULL,
	age_group VARCHAR(3) NOT NULL,
	race VARCHAR NOT NULL,
	family_history VARCHAR(1) NOT NULL,
	age_menarche VARCHAR NOT NULL,
	age_first_birth VARCHAR NOT NULL,
	BIRADS_breast_density VARCHAR NOT NULL,
	current_hrt VARCHAR NOT NULL,
	menopaus VARCHAR NOT NULL,
	bmi_group VARCHAR NOT NULL,
	biophx VARCHAR NOT NULL,
	breast_cancer_history VARCHAR NOT NULL,
	covariate_count VARCHAR NOT NULL
);

CREATE TABLE indicators2 (
	calendar_year VARCHAR(4) NOT NULL,
	age_group VARCHAR(3) NOT NULL,
	race VARCHAR NOT NULL,
	family_history VARCHAR(1) NOT NULL,
	age_menarche VARCHAR NOT NULL,
	age_first_birth VARCHAR NOT NULL,
	BIRADS_breast_density VARCHAR NOT NULL,
	current_hrt VARCHAR NOT NULL,
	menopaus VARCHAR NOT NULL,
	bmi_group VARCHAR NOT NULL,
	biophx VARCHAR NOT NULL,
	breast_cancer_history VARCHAR NOT NULL,
	covariate_count VARCHAR NOT NULL
);

CREATE TABLE indicators3 (
	calendar_year VARCHAR(4) NOT NULL,
	age_group VARCHAR(3) NOT NULL,
	race VARCHAR NOT NULL,
	family_history VARCHAR(1) NOT NULL,
	age_menarche VARCHAR NOT NULL,
	age_first_birth VARCHAR NOT NULL,
	BIRADS_breast_density VARCHAR NOT NULL,
	current_hrt VARCHAR NOT NULL,
	menopaus VARCHAR NOT NULL,
	bmi_group VARCHAR NOT NULL,
	biophx VARCHAR NOT NULL,
	breast_cancer_history VARCHAR NOT NULL,
	covariate_count VARCHAR NOT NULL
);

-- CREATE TABLE for image file names from kaggle
-- File names loaded from jupyter notebook Database_Connections
CREATE TABLE Kaggle_Images (
	file_path_names VARCHAR(40) NOT NULL
);

--COPY indicators FROM '/Users/megue/Documents/Github/BreastCancerClassification/resources/bcsc_risk_factors_summarized1_092020.csv' DELIMITER ',' CSV HEADER;

/* We might want to use this later to get our isk factor data from the files on Github
wget requires linux
COPY indicators
FROM PROGRAM 'wget -q -O - "$@" "https://https://github.com/GirijaJoshi/BreastCancerClassification/blob/HannahPreston/resources/bcsc_risk_factors_summarized1_092020.csv
DELIMITER ',' CSV HEADER;
*/

SELECT * FROM indicators1;
SELECT * FROM Kaggle_Images;
