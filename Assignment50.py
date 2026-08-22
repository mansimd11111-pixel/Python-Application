import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score
)

###################################################
# 1. LOAD DATASET
####################################################

cancer = load_breast_cancer()

df = pd.DataFrame(
    cancer.data,
    columns=cancer.feature_names
)

df["target"] = cancer.target

print("=" * 60)
print("BREAST CANCER PREDICTION")
print("=" * 60)

print("\nDataset Shape:", df.shape)
print("\nFirst 5 Records:")
print(df.head())

####################################################
# 2. DATA INFORMATION
####################################################

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

print("\nTarget Distribution:")
print(df["target"].value_counts())

# 0 = Malignant
# 1 = Benign

####################################################
# 3. EDA
####################################################

plt.figure(figsize=(6, 4))
sns.countplot(x="target", data=df)
plt.title("Distribution of Tumor Types")
plt.xlabel("Tumor Type")
plt.ylabel("Count")
plt.xticks([0, 1], ["Malignant", "Benign"])
plt.show()

plt.figure(figsize=(16, 12))
sns.heatmap(df.corr(), cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()

####################################################
# 4. FEATURES AND TARGET
####################################################

X = df.drop("target", axis=1)
y = df["target"]

####################################################
# 5. TRAIN TEST SPLIT
####################################################

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)

# ###################################################
# 6. FEATURE SCALING
# ###################################################
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ###################################################
# 7. MODEL TRAINING
# ###################################################

model = LogisticRegression(max_iter=10000)

model.fit(X_train_scaled, y_train)

print("\nModel training completed.")

#  ###################################################
# 8. PREDICTION
# ###################################################
y_pred = model.predict(X_test_scaled)

# ###################################################
# 9. EVALUATION
#  ###################################################

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\n" + "=" * 60)
print("MODEL EVALUATION")
print("=" * 60)

print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1-Score  : {f1:.4f}")

#  ###################################################
# 10. CONFUSION MATRIX
# ###################################################

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

plt.figure(figsize=(6, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Malignant", "Benign"],
    yticklabels=["Malignant", "Benign"]
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")

plt.show()

#  ###################################################
# 11. CLASSIFICATION REPORT
# ###################################################
print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=["Malignant", "Benign"]
    )
)

#  ###################################################
# 12. CONCLUSION
#  ###################################################

print("\nConclusion:")
print("The Logistic Regression model successfully")
print("classifies breast tumors as Malignant or Benign.")
print("The model achieves high accuracy and good")
print("Precision, Recall and F1-Score on the test data.")