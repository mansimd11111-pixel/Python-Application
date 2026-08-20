#Machine Learning Assignment
# Advertising Dataset - Linear Regression

#################################
# Step 1: Import Libraries
#################################

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


##################################
# Step 2: Get Data
##################################

df = pd.read_csv("MarvellousAdvertising.csv")

print("Dataset:")
print(df)


##################################
# Step 3: Prepare Data
##################################

# Input features
X = df[['TV', 'radio', 'newspaper']]

# Output feature
Y = df['sales']


##################################
# Step 4: Train Data
##################################

# Divide data into 50% training and 50% testing

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y,
    test_size=0.5,
    random_state=42
)

print("\nTraining Data:")
print(X_train)

print("\nTesting Data:")
print(X_test)


##################################
# Step 5: Create Linear Regression
##################################

model = LinearRegression()


# Train the model

model.fit(X_train, Y_train)

print("\nModel Training Completed")


##################################
# Step 6: Test Data
##################################

Y_pred = model.predict(X_test)


##################################
# Step 7: Display Expected
# and Predicted Values
##################################

result = pd.DataFrame({
    'Expected Sales': Y_test.values,
    'Predicted Sales': Y_pred
})

print("\nExpected vs Predicted Sales:")
print(result)


##################################
# Step 8: Model Evaluation
##################################

mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)

print("\nMean Squared Error:", mse)
print("R2 Score:", r2)