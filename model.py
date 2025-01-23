import statsmodels.api as sm
import numpy as np

def train_model(X, y):
    """
    Train a logistic regression model.

    Args:
        X (pd.DataFrame): Features.
        y (pd.Series): Target variable.

    Returns:
        tuple: Trained model, confusion matrix, and accuracy.
    """
    reg_logit = sm.Logit(y, X)
    results_logit = reg_logit.fit(disp=0)  

    cm, acc = confusion_matrix(X, y, results_logit)
    return results_logit, cm, acc

def evaluate_model(model, X, y):
    """
    Evaluate the logistic regression model.

    Args:
        model: Trained logistic regression model.
        X (pd.DataFrame): Features.
        y (pd.Series): Target variable.

    Returns:
        tuple: Confusion matrix and accuracy.
    """
    cm, acc = confusion_matrix(X, y, model)
    return cm, acc

def confusion_matrix(data, actual_values, model):
    """
    Compute the confusion matrix and accuracy.

    Args:
        data (pd.DataFrame): Features.
        actual_values (pd.Series): True values.
        model: Logistic regression model.

    Returns:
        tuple: Confusion matrix and accuracy.
    """
    pred_values = model.predict(data)
    bins = np.array([0, 0.5, 1])
    cm = np.histogram2d(actual_values, pred_values, bins=bins)[0]
    acc = (cm[0, 0] + cm[1, 1]) / cm.sum()
    return cm, acc
