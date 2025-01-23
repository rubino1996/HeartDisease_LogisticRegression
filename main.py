import pandas as pd
from preprocess import preprocess_data
from model import train_model, evaluate_model
from visualize import plot_distribution

# Load and preprocess the data
raw_data = pd.read_csv('framingham.csv')
data = preprocess_data(raw_data)

# Train the logistic regression model
X_train = data['X']
y_train = data['y']
model, train_cm, train_acc = train_model(X_train, y_train)

# Visualize the original training class distribution
plot_distribution(y_train, title='Original Training Class Distribution')

# Load the test data and preprocess it
raw_test_data = pd.read_csv('test_data.csv')
test_data = preprocess_data(raw_test_data)

X_test = test_data['X']
y_test = test_data['y']

# Evaluate the model on the test set
test_cm, test_acc = evaluate_model(model, X_test, y_test)

# Visualize the test data distribution
plot_distribution(y_test, title='Test Data Class Distribution')

# Print confusion matrices and accuracies
print("Training Confusion Matrix:", train_cm)
print("Training Accuracy:", train_acc)
print("Test Confusion Matrix:", test_cm)
print("Test Accuracy:", test_acc)
