###############################
# Import required libraries
##############################
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Step 1: Get Data
# Load dataset
df = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")

print("Dataset:")
print(df)

##############################################
# Step 2: Clean, Prepare and Manipulate Data
##############################################

# Create LabelEncoder objects
weather_encoder = LabelEncoder()
temperature_encoder = LabelEncoder()
play_encoder = LabelEncoder()

# Convert categorical data into numerical data
df["Weather"] = weather_encoder.fit_transform(df["Weather"])
df["Temperature"] = temperature_encoder.fit_transform(df["Temperature"])
df["Play"] = play_encoder.fit_transform(df["Play"])

print("\nEncoded Dataset:")
print(df)


# Separate features and target
X = df[["Weather", "Temperature"]]
Y = df["Play"]

#################################
# Step 3: Train Data
#################################

# Split data into training and testing data
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# Create KNN model
K = 3
model = KNeighborsClassifier(n_neighbors=K)

# Train the model
model.fit(X_train, Y_train)

#######################
# Step 4: Test Data
#######################

# Take input from user
print("\nEnter Weather:")
print("1. Sunny")
print("2. Overcast")
print("3. Rainy")

weather = input("Enter Weather: ")

print("\nEnter Temperature:")
print("1. Hot")
print("2. Mild")
print("3. Cool")

temperature = input("Enter Temperature: ")

# Convert user input into numerical values
weather_value = weather_encoder.transform([weather])[0]
temperature_value = temperature_encoder.transform([temperature])[0]

# Create input data
test_data = [[weather_value, temperature_value]]

# Predict
prediction = model.predict(test_data)

# Convert prediction back to Yes/No
result = play_encoder.inverse_transform(prediction)

print("\nPrediction:", result[0])

###################################
# Step 5: Calculate Accuracy
###################################

def CheckAccuracy(k):
    model = KNeighborsClassifier(n_neighbors=k)
    
    model.fit(X_train, Y_train)
    
    Y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(Y_test, Y_pred)
    
    return accuracy


print("\nAccuracy for different values of K:")

for k in range(1, 6):
    accuracy = CheckAccuracy(k)
    print("K =", k, "Accuracy =", accuracy)