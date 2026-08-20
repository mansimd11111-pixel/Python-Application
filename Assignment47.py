##########################################
#Q1 What is a coefficient in regression?
###########################################

#A coefficient represents how much the dependent variable (Y) changes when an independent variable (X) increases by 1 unit,
# while other factors remain constant.
#For example:
#Salary = 5000 × Experience + 20000
#Here, 5000 is the coefficient. It means that for every 1-year increase in experience, the predicted salary increases by ₹5,000

######################
#2. Regression model
########################
#Given:

#Y = 8X + 15

#Coefficient = 8
#Intercept = 15

#Meaning of coefficient:
#The coefficient 8 means that when X increases by 1 unit, Y increases by 8 units.

#Meaning of intercept:
#When X = 0 the predicted value of Y is 15.

################################
#Q3.Marks prediction model
################################

#Marks = 6 × StudyHours + 40

#Coefficient = 6

#It means that for every additional 1 hour of study predicted marks increase by 6 marks.

#Intercept = 40

#It means that when study hours are 0 the predicted marks are 40.

#If study hours increase by 2 hours:
#Increase in marks = 6 × 2
#= 12 marks

#So the predicted marks will increase by 12 marks.

#########################
#Q4 Salary prediction
########################
#Given:

#Salary = 12 × Experience + 25

#For Experience = 2 years:

#Salary = 12 × 2 + 25
#= 24 + 25
#= 49

#For Experience = 5 years:

#Salary = 12 × 5 + 25
#= 60 + 25
#= 85

#For Experience = 7 years:

#Salary = 12 × 7 + 25
#= 84 + 25
#= 109

#####################################
#Q5 Regression equation
####################################
#Given:

#Y = -3X + 20

#1. What does the negative coefficient indicate?

#The coefficient is -3.

#It indicates a negative relationship between X and Y. When X increases Y decreases.

#2. What happens to Y when X increases by 1?

#Y decreases by 3 units.

#3. Calculate Y when X = 4

#Y = -3(4) + 20
#= -12 + 20
#= 8

#Therefore, Y = 8.

###################################
#Q6 House price prediction
####################################
#Given:

#Price = 3000 × Size + 40000 × Bedrooms + 150000

#Meaning of Size coefficient = 3000

#For every 1-unit increase in house size the predicted house price increases by 3000 units, assuming the number of bedrooms remains constant.

#Meaning of Bedrooms coefficient = 40000

#For every additional bedroom the predicted house price increases by 40,000, assuming the size remains constant.

#Which feature has a larger impact?
#Size coefficient = 3000
#Bedrooms coefficient = 40000

#Therefore, according to the given equation, Bedrooms has the larger coefficient and greater impact per one-unit increase.

#####
#Q7
####
# Import required libraries
import numpy as np
from sklearn.linear_model import LinearRegression

# Input data
study_hours = np.array([[1], [2], [3], [4], [5]])
marks = np.array([50, 55, 60, 65, 70])

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(study_hours, marks)

# Print coefficient
print("Coefficient:", model.coef_[0])

# Print intercept
print("Intercept:", model.intercept_)

###########################################
#Q8 Predict marks for 6 study hours
#######################################

#Using the model from Question 7:

#Marks = 5 × StudyHours + 45

#For 6 study hours:

#Marks = 5 × 6 + 45
#= 30 + 45
#= 75

# Import required libraries
import numpy as np
from sklearn.linear_model import LinearRegression

# Training data
study_hours = np.array([[1], [2], [3], [4], [5]])
marks = np.array([50, 55, 60, 65, 70])

# Create and train the model
model = LinearRegression()
model.fit(study_hours, marks)

# Predict marks for 6 study hours
predicted_marks = model.predict([[6]])

# Display result
print("Predicted marks for 6 study hours:", predicted_marks[0])

########
#Q9
###########
# Import required libraries
import numpy as np
from sklearn.linear_model import LinearRegression

# Input features
X = np.array([
    [1, 7],
    [2, 6],
    [3, 7],
    [4, 6],
    [5, 8]
])

# Target variable
y = np.array([50, 55, 60, 65, 70])

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Print coefficients
print("Coefficient for StudyHours:", model.coef_[0])
print("Coefficient for SleepHours:", model.coef_[1])

# Print intercept
print("Intercept:", model.intercept_)

###########################################################
##Q10 Importance of coefficients in regression models
#############################################################

#Coefficients are important because they show how strongly each input feature affects the predicted output.

#For example:

#Marks = 5 × StudyHours + 2 × SleepHours + 30

#StudyHours coefficient = 5
#SleepHours coefficient = 2

#This means:

#Increasing study hours by 1 increases predicted marks by 5, keeping sleep hours constant.
#Increasing sleep hours by 1 increases predicted marks by 2, keeping study hours constant.

#Coefficients help us understand the direction and impact of input features on predictions.

#Positive coefficient: increases the predicted value.
#Negative coefficient: decreases the predicted value.
#Coefficient near 0: has little or no linear effect on the prediction.