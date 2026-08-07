from pyexpat import model
from re import X

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

###################################
# Display feature Importance
###################################

print("Feature Importances:")
importance = model.feature_importances_

for feature, value in zip(X.columns, importance):
    print(feature, ":", value)

##################################################
# Remove sleephours column and compare accuracy
##################################################

X_new = df.drop(["SleepHours", "FinalResult"], axis=1) # type: ignore
y = df["FinalResult"] # type: ignore

x_train, x_test, y_train, y_test = train_test_split(
    X_new, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy after removing SleepHours:", accuracy*100)    

#Train model using only Studyhours and attendance
X = df[["StudyHours", "Attendance"]] # type: ignore
y = df["FinalResult"] # type: ignore

x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy*100)

#######################################
# Predict result for 5 new students
#######################################

new_students = pd.DataFrame({
    "StudyHours":[8,5,2,6,9],
    "Attendance":[95,80,60,85,98],
    "PreviousScore":[88,70,45,75,92],
    "AssignmentsCompleted":[10,8,5,9,10],
    "SleepHours":[7,6,8,7,6]
})

prediction = model.predict(new_students)

print(new_students)
print("Predicted Result:", prediction)

#################################
# calculate accuracy manually 
#################################

correct = (y_test == y_pred).sum()

total = len(y_test)

manual_accuracy = (correct/total)*100

print("Manual Accuracy:", manual_accuracy)

####################################
# Identify misclassified students 
####################################
wrong = y_test != y_pred

print(df.loc[y_test.index[wrong]]) # type: ignore

print("Misclassified Students =", wrong.sum())

###########################################
#Compare different random_state values
###########################################
for state in [0,10,42]:
    model = DecisionTreeClassifier(random_state=state)
    model.fit(x_train,y_train)

    pred = model.predict(x_test)

    acc = accuracy_score(y_test,pred)

    print("Random State:",state)
    print("Accuracy:",acc*100)
 
################################    
# Decision Tree Visualization
################################
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(15,8))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=["Fail","Pass"],
    filled=True
)

plt.show()

###################################
#Create performanceindex column
####################################

df["PerformanceIndex"] = (df["StudyHours"]*2) + df["Attendance"] # type: ignore

X = df.drop("FinalResult",axis=1) # type: ignore
y = df["FinalResult"] # type: ignore

x_train,x_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(x_train,y_train)

pred = model.predict(x_test)

acc = accuracy_score(y_test,pred)

print("Accuracy:",acc*100)

####################################
#train model with max_depth=None
####################################

model = DecisionTreeClassifier(max_depth=None,random_state=42)

model.fit(x_train,y_train)

train_acc = model.score(x_train,y_train)

test_acc = model.score(x_test,y_test)

print("Training Accuracy:",train_acc*100)

print("Testing Accuracy:",test_acc*100)    

