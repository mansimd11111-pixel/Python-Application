# ============================================================
# FRAUDULENT TRANSACTION DETECTION
# Ensemble Learning Assignment
# ============================================================

# ------------------------------------------------------------
# 1. IMPORT LIBRARIES
# ------------------------------------------------------------

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    BaggingClassifier,
    RandomForestClassifier,
    AdaBoostClassifier,
    VotingClassifier
)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)


# ------------------------------------------------------------
# 2. LOAD DATASET
# ------------------------------------------------------------

df = pd.read_csv("fraudulent_transaction_detection.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())


# ------------------------------------------------------------
# 3. REMOVE DUPLICATE VALUES
# ------------------------------------------------------------

df = df.drop_duplicates()

print("\nShape after removing duplicates:")
print(df.shape)


# ------------------------------------------------------------
# 4. HANDLE MISSING VALUES
# ------------------------------------------------------------

# Fill numerical missing values with median
numeric_columns = df.select_dtypes(include=np.number).columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

# Fill categorical missing values with mode
categorical_columns = df.select_dtypes(include='object').columns

for col in categorical_columns:
    df[col] = df[col].fillna(df[col].mode()[0])


# ------------------------------------------------------------
# 5. ENCODE CATEGORICAL COLUMNS
# ------------------------------------------------------------

# Convert categorical columns into numerical values
label_encoders = {}

for col in df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    label_encoders[col] = le


# ------------------------------------------------------------
# 6. SEPARATE FEATURES AND TARGET
# ------------------------------------------------------------

# Target column
target = "Fraud"

X = df.drop(target, axis=1)
y = df[target]

print("\nFeatures:")
print(X.columns)

print("\nTarget:")
print(y.value_counts())


# ------------------------------------------------------------
# 7. TRAIN-TEST SPLIT
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining data:", X_train.shape)
print("Testing data:", X_test.shape)


# ------------------------------------------------------------
# 8. FEATURE SCALING
# ------------------------------------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# ------------------------------------------------------------
# 9. CREATE MODELS
# ------------------------------------------------------------

# 1. Decision Tree
decision_tree = DecisionTreeClassifier(
    random_state=42
)


# 2. Bagging Classifier
bagging = BaggingClassifier(
    estimator=DecisionTreeClassifier(random_state=42),
    n_estimators=100,
    random_state=42
)


# 3. Random Forest
random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# 4. AdaBoost
adaboost = AdaBoostClassifier(
    n_estimators=100,
    random_state=42
)


# ------------------------------------------------------------
# 10. VOTING CLASSIFIER
# ------------------------------------------------------------

voting = VotingClassifier(
    estimators=[
        ('dt', DecisionTreeClassifier(random_state=42)),
        ('rf', RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )),
        ('ada', AdaBoostClassifier(
            n_estimators=100,
            random_state=42
        ))
    ],
    voting='hard'
)


# ------------------------------------------------------------
# 11. STORE ALL MODELS
# ------------------------------------------------------------

models = {
    "Decision Tree": decision_tree,
    "Bagging": bagging,
    "Random Forest": random_forest,
    "AdaBoost": adaboost,
    "Voting": voting
}


# ------------------------------------------------------------
# 12. TRAIN AND EVALUATE MODELS
# ------------------------------------------------------------

results = []

for name, model in models.items():

    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)

    # Train model
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Metrics
    accuracy = accuracy_score(y_test, y_pred)

    precision = precision_score(
        y_test,
        y_pred,
        zero_division=0
    )

    recall = recall_score(
        y_test,
        y_pred,
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        y_pred,
        zero_division=0
    )

    # Store results
    results.append([
        name,
        accuracy,
        precision,
        recall,
        f1
    ])

    # Print results
    print("Accuracy :", accuracy)
    print("Precision:", precision)
    print("Recall   :", recall)
    print("F1 Score :", f1)

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            y_pred,
            zero_division=0
        )
    )

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)

    print("Confusion Matrix:")
    print(cm)

    # Display confusion matrix
    ConfusionMatrixDisplay(
        confusion_matrix=cm
    ).plot()

    plt.title(name + " - Confusion Matrix")
    plt.show()


# ------------------------------------------------------------
# 13. FINAL COMPARISON TABLE
# ------------------------------------------------------------

comparison = pd.DataFrame(
    results,
    columns=[
        "Algorithm",
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ]
)

print("\n")
print("=" * 80)
print("FINAL MODEL COMPARISON")
print("=" * 80)

print(comparison)


# ------------------------------------------------------------
# 14. SORT MODELS BY F1 SCORE
# ------------------------------------------------------------

comparison_sorted = comparison.sort_values(
    by="F1 Score",
    ascending=False
)

print("\nModels ranked by F1 Score:")
print(comparison_sorted)


# ------------------------------------------------------------
# 15. FIND BEST MODEL
# ------------------------------------------------------------

best_model = comparison.loc[
    comparison["F1 Score"].idxmax()
]

print("\n" + "=" * 60)
print("BEST MODEL")
print("=" * 60)

print("Algorithm :", best_model["Algorithm"])
print("Accuracy  :", best_model["Accuracy"])
print("Precision :", best_model["Precision"])
print("Recall    :", best_model["Recall"])
print("F1 Score  :", best_model["F1 Score"])