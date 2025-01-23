# HeartDisease_LogisticRegression
This project uses logistic regression to analyze the Framingham Heart Study dataset, a longitudinal study that tracks cardiovascular disease risk factors. 
The goal is to predict the 10-year risk of coronary heart disease (CHD) using various health and lifestyle indicators, such as age, gender, smoking habits, blood pressure, and cholesterol levels.

**The project involves:**

Data Preprocessing: Handling missing values, standardizing features, and preparing data for model training.

Model Development: Building a logistic regression model to assess the relationship between features and CHD risk.

Model Evaluation: Using confusion matrices and accuracy scores to evaluate model performance on both training and test datasets.

Visualization: Creating visual insights into the dataset, including class distributions and model results.

This analysis aims to provide insights into key predictors of CHD and demonstrates a simple yet powerful approach to binary classification problems in healthcare.

**How to Run**:
To run the program clone the repository and run main.py file. The correlations.py file and data_creation.py file are extra files that are not used in the main.py file. However, the correlations.py file was used to help identify which features from the original dataset had positive correlation with the output, in this case all of the features had positive value except education so education was not included in the evaluation for "estimators". In addition, for testing our model, a test_data was created using the file data_creation.py to test our model. As mentioned these are extra files that you don't need to run the main.py file but you do need the test_data.csv.


