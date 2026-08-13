######################################################
# Step 1 : Import required libraries
######################################################

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

######################################################
# Step 2 : Get Data
######################################################

df = pd.read_csv("WinePredictor.csv")

print(df.head)
print(df.shape)
print(df.info())

######################################################
# Step 3 : Clea Prepare and Manipulate Data
######################################################

X = df.iloc[:, 1:]     # 13 features
y = df.iloc[:, 0]      # Class

print("Features:")
print(X.head())

print("Target:")
print(y.head())

# Checking missing values 
print(df.isnull().sum())

######################################################
# Step 4 : Train Test Split
######################################################

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)

######################################################
# Step 5 : Scale and Data
######################################################

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

######################################################
# Step 6 : Train the Classification Model
######################################################

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

print("Model trained successfully")

######################################################
# Step 7 : Test Data 
######################################################

y_pred = model.predict(X_test)

print("Actual values:")
print(y_test.values)

print("Predicted values:")
print(y_pred)

######################################################
# Step 8 : Calculate Accuracy
######################################################

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Accuracy Percentage:", accuracy * 100, "%")

######################################################
# Step 9 : Confusion Matrix
######################################################

cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:")
print(cm)

######################################################
# Step 10 : Classification Report
######################################################

print("Classification Report: ")
print(classification_report(y_test, y_pred))
















