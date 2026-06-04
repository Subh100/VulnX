from scipy.io import arff
import pandas as pd

data, meta = arff.loadarff("E:/Data/PhishGuard/dataset/phishing_dataset.arff")

df = pd.DataFrame(data)

print("dData Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())

X = df.drop("Result", axis=1)
y = df["Result"]

print("Unique labels:", set(y))
print(df["Result"].value_counts())

print("\nFeatures Shape:")
print(X.shape)

print("\nTarget Shape:")
print(y.shape)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

X = X.astype(int)
y = y.astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size = 0.2,
    random_state = 42
)

model = RandomForestClassifier(
    n_estimators = 100,
    random_state = 42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy:")
print(accuracy * 100)

import joblib

joblib.dump(model, r"E:\Data\PhishGuard\backend\model\phishguard_model.pkl")

print("Model Saved Successfully!")