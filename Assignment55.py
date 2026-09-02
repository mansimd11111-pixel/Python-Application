# ============================================================
# CUSTOMER LOAN APPROVAL USING VOTING CLASSIFICATION
# ============================================================

# 1. Import Libraries

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# 2. Load Dataset
# ============================================================

df = pd.read_csv("Customer_Loan_Approval.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)


# ============================================================
# 3. Check Missing Values
# ============================================================

print("\nMissing Values:")
print(df.isnull().sum())


# ============================================================
# 4. Handle Missing Values
# ============================================================

features = [
    'Age',
    'Income',
    'CreditScore',
    'ExistingLoan',
    'EmploymentExperience',
    'LoanAmount'
]

for column in features:
    df[column] = df[column].fillna(df[column].median())


print("\nMissing Values After Handling:")
print(df.isnull().sum())


# ============================================================
# 5. Separate Input and Output
# ============================================================

X = df[features]

y = df['LoanApproved']


# ============================================================
# 6. Split Dataset
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# ============================================================
# 7. Logistic Regression
# ============================================================

lr_model = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression(random_state=42))
])

lr_model.fit(X_train, y_train)

y_pred_lr = lr_model.predict(X_test)

lr_accuracy = accuracy_score(y_test, y_pred_lr)

print("\nLogistic Regression Accuracy:",
      round(lr_accuracy * 100, 2), "%")


# ============================================================
# 8. Decision Tree
# ============================================================

dt_model = DecisionTreeClassifier(
    random_state=42
)

dt_model.fit(X_train, y_train)

y_pred_dt = dt_model.predict(X_test)

dt_accuracy = accuracy_score(y_test, y_pred_dt)

print("Decision Tree Accuracy:",
      round(dt_accuracy * 100, 2), "%")


# ============================================================
# 9. KNN
# ============================================================

knn_model = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', KNeighborsClassifier(n_neighbors=5))
])

knn_model.fit(X_train, y_train)

y_pred_knn = knn_model.predict(X_test)

knn_accuracy = accuracy_score(y_test, y_pred_knn)

print("KNN Accuracy:",
      round(knn_accuracy * 100, 2), "%")


# ============================================================
# 10. Hard Voting Classifier
# ============================================================

hard_voting = VotingClassifier(
    estimators=[
        ('lr', lr_model),
        ('dt', dt_model),
        ('knn', knn_model)
    ],
    voting='hard'
)

hard_voting.fit(X_train, y_train)

y_pred_hard = hard_voting.predict(X_test)

hard_accuracy = accuracy_score(y_test, y_pred_hard)

print("Hard Voting Accuracy:",
      round(hard_accuracy * 100, 2), "%")


# ============================================================
# 11. Soft Voting Classifier
# ============================================================

soft_voting = VotingClassifier(
    estimators=[
        ('lr', lr_model),
        ('dt', dt_model),
        ('knn', knn_model)
    ],
    voting='soft'
)

soft_voting.fit(X_train, y_train)

y_pred_soft = soft_voting.predict(X_test)

soft_accuracy = accuracy_score(y_test, y_pred_soft)

print("Soft Voting Accuracy:",
      round(soft_accuracy * 100, 2), "%")


# ============================================================
# 12. Comparison
# ============================================================

results = pd.DataFrame({
    'Model': [
        'Logistic Regression',
        'Decision Tree',
        'KNN',
        'Hard Voting',
        'Soft Voting'
    ],

    'Accuracy (%)': [
        lr_accuracy * 100,
        dt_accuracy * 100,
        knn_accuracy * 100,
        hard_accuracy * 100,
        soft_accuracy * 100
    ]
})

results['Accuracy (%)'] = results['Accuracy (%)'].round(2)

print("\n======================================")
print("MODEL ACCURACY COMPARISON")
print("======================================")

print(results)


# ============================================================
# 13. Best Model
# ============================================================

best_model = results.loc[
    results['Accuracy (%)'].idxmax()
]

print("\nBest Model:", best_model['Model'])
print("Best Accuracy:", best_model['Accuracy (%)'], "%")


# ============================================================
# 14. Confusion Matrix
# ============================================================

cm = confusion_matrix(y_test, y_pred_hard)

plt.figure(figsize=(6, 4))

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=['Rejected', 'Approved'],
    yticklabels=['Rejected', 'Approved']
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Hard Voting Confusion Matrix")

plt.show()


# ============================================================
# 15. Classification Report
# ============================================================

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred_hard,
        target_names=[
            'Loan Rejected',
            'Loan Approved'
        ]
    )
)