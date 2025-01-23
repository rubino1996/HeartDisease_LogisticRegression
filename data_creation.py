import numpy as np
import pandas as pd

np.random.seed(42)
n_samples = 1000

synthetic_data = pd.DataFrame({
    'male': np.random.choice([0, 1], size=n_samples, p=[0.57, 0.43]),  # Match mean 0.429
    'age': np.random.randint(32, 71, size=n_samples),  # Age range 32-70
    'education': np.random.choice([1, 2, 3, 4], size=n_samples, p=[0.25, 0.5, 0.2, 0.05]),
    'currentSmoker': np.random.choice([0, 1], size=n_samples, p=[0.51, 0.49]),
    'cigsPerDay': np.random.choice([0, 10, 20, 30], size=n_samples, p=[0.5, 0.2, 0.2, 0.1]),
    'BPMeds': np.random.choice([0, 1], size=n_samples, p=[0.97, 0.03]),
    'prevalentStroke': np.random.choice([0, 1], size=n_samples, p=[0.99, 0.01]),
    'prevalentHyp': np.random.choice([0, 1], size=n_samples, p=[0.69, 0.31]),
    'diabetes': np.random.choice([0, 1], size=n_samples, p=[0.97, 0.03]),
    'totChol': np.random.normal(236, 44, n_samples).clip(107, 300),  # Cholesterol level
    'sysBP': np.random.normal(132, 22, n_samples).clip(90, 200),  # Systolic BP
    'diaBP': np.random.normal(83, 12, n_samples).clip(50, 120),  # Diastolic BP
    'BMI': np.random.normal(25.8, 4.1, n_samples).clip(15, 40),  # BMI
    'heartRate': np.random.randint(60, 120, size=n_samples),  # Heart rate
    'glucose': np.random.normal(82, 24, n_samples).clip(50, 200),  # Glucose level
    'TenYearCHD': np.random.choice([0, 1], size=n_samples, p=[0.85, 0.15])  # Match class distribution
})


synthetic_data.to_csv('test_data.csv', index=False)



