# HeartDisease_LogisticRegression
This project uses logistic regression to analyze the Framingham Heart Study dataset, a longitudinal study that tracks cardiovascular disease risk factors. The dataset was obtained from Kaggle (https://www.kaggle.com/datasets/dileep070/heart-disease-prediction-using-logistic-regression)
The goal is to predict the 10-year risk of coronary heart disease (CHD) using various health and lifestyle indicators, such as age, gender, smoking habits, blood pressure, and cholesterol levels.

**The project involves:**

Data Preprocessing: Handling missing values, standardizing features, and preparing data for model training.

Model Development: Building a logistic regression model to assess the relationship between features and CHD risk.

Model Evaluation: Using confusion matrices and accuracy scores to evaluate model performance on both training and test datasets.

Visualization: Creating visual insights into the dataset, including class distributions and model results.

This analysis evaluates the predictors of coronary heart disease (CHD) and demonstrates the effectiveness of logistic regression for binary classification in healthcare. The model achieved 85.5% accuracy on the training set and 83.7% accuracy on the test set, as evidenced by the confusion matrices. While the model performs well, its accuracy can be further improved with additional training data, feature engineering, or advanced modeling techniques such as regularization or ensemble methods. These enhancements can refine predictions and provide even greater insights for risk assessment in real-world healthcare applications.

**How to Run**:

To run the program clone the repository (https://github.com/rubino1996/HeartDisease_LogisticRegression.git) and run main.py file. The repository includes two additional files, correlations.py and data_creation.py, which are not directly used within the main.py file but serve supporting purposes:

correlations.py: This script was used to identify features from the original dataset with a positive correlation to the output. All features except education showed positive correlation with the target variable (TenYearCHD). As a result, education was excluded from the list of estimators during the training process.

data_creation.py: This script was used to generate a synthetic dataset (test_data.csv) for testing the logistic regression model.

While you don't need to execute correlations.py or data_creation.py to run the program, you will need the test_data.csv file to evaluate the model on test data. 

