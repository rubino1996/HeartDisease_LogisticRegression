import statsmodels.api as sm

def preprocess_data(data):
    """
    Preprocess the data by handling missing values, separating features and target.

    Args:
        data (pd.DataFrame): The raw data.

    Returns:
        dict: Processed data with 'X' (features) and 'y' (target).
    """
    data = data.dropna()
    y = data['TenYearCHD']
    estimators = [
        'male', 'age', 'currentSmoker', 'cigsPerDay', 'BPMeds',
        'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol',
        'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose'
    ]
    X = data[estimators]
    X = sm.add_constant(X)  # Add constant for statsmodels
    return {'X': X, 'y': y}
