##############################
#Q1 Step 1: Mean of X
############################

#X = 1+2+3+4+5/5 = 3

#Mean of X = 3

#Step 2: Mean of Y
#Y=3+4+2+4+5/5 =3.6
	

#Mean of Y = 3.6

#Step 4: Calculate Intercept (c)

#Formula:

# c = Y -mX
# c = 3.6 - (0.4)(3)
# c = 2.4

#Regression equation
# Y = 0.4(6) + 2.4
# Y = 4.8


#########
#Q2
#########
# Import required libraries
import numpy as np

# Dataset
X = np.array([1, 2, 3, 4, 5])
Y = np.array([3, 4, 2, 4, 5])

# Mean
mean_x = np.mean(X)
mean_y = np.mean(Y)

# Calculate slope
m = np.sum((X - mean_x) * (Y - mean_y)) / np.sum((X - mean_x) ** 2)

# Calculate intercept
c = mean_y - m * mean_x

# Predict Y values
Y_pred = m * X + c

# Calculate MSE
mse = np.mean((Y - Y_pred) ** 2)

# Calculate R2 score
ss_res = np.sum((Y - Y_pred) ** 2)
ss_tot = np.sum((Y - mean_y) ** 2)
r2 = 1 - (ss_res / ss_tot)

print("Mean of X:", mean_x)
print("Mean of Y:", mean_y)
print("Slope (m):", m)
print("Intercept (c):", c)
print("Predicted Y:", Y_pred)
print("MSE:", mse)
print("R2 Score:", r2)

###########
# q3
##########

# Import required libraries
import numpy as np
import matplotlib.pyplot as plt

# Dataset
experience = np.array([1, 2, 3, 4, 5])
salary = np.array([20000, 25000, 30000, 35000, 40000])

# Calculate slope and intercept
m, c = np.polyfit(experience, salary, 1)

# Predict salary for 6 years
predicted_salary = m * 6 + c

print("Slope:", m)
print("Intercept:", c)
print("Predicted Salary for 6 years:", predicted_salary)

# Regression line
salary_pred = m * experience + c

# Plot data points
plt.scatter(experience, salary, label="Data Points")

# Plot regression line
plt.plot(experience, salary_pred, label="Regression Line")

plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.title("Linear Regression: Experience vs Salary")
plt.legend()
plt.show()

######################################
#Q4. Why is KNN called a lazy learner?
######################################
#Answer:
#KNN is called a lazy learner because it does not build a model during the training phase.
#It simply stores the training data and performs calculations when a new data point needs to be predicted.

#######################################
#Q5. What happens if K is too small?
#########################################
#If K is too small, the KNN model becomes very sensitive to noise and outliers.
#It may give unstable predictions.
#It can overfit the training data.
#A K value of 1 is especially sensitive to individual data points.

####################################
#q6. What happens if K is too large?
####################################

#If K is too large, the model considers too many neighboring points.
#It becomes less sensitive to local patterns.
#Important differences between classes may be ignored.
#It can underfit the data.

##########################################################
#Q7. Why does Linear Regression minimize squared error?
#########################################################
#Linear Regression minimizes squared error because squaring the errors:

#Makes all errors positive.
#Gives greater importance to larger errors.
#Provides a smooth mathematical function that can be easily optimized.
#Helps find the best-fitting regression line.

#The objective is to minimize:
#∑(Y−Y
#pred)
#2
#This is called the Sum of Squared Errors (SSE).

################################################
#Q8. What is the difference between MSE and R²?
##############################################
#MSE	R²
#MSE stands for Mean Squared Error.	R² stands for R-squared score.
#Measures the average squared prediction error.	Measures how well the model explains the variation in the target variable.
#Lower MSE is better.	Higher R² is generally better.
#Its value depends on the scale/units of Y.	Usually ranges from 0 to 1, although it can be negative for poor models.
#Formula: Mean((Y - Ypred)²)	Formula: 1 - SSres/SStot

##########################################
# Q9 why cant R2 be greater than 1 ? 
##########################################

# R2 = 1 - SSres/SStot
# SSrres > 0
# SSres/SStot > 0
# R2 < 1
#So R² cannot be greater than 1.

#R² = 1 → Perfect prediction.
#R² = 0 → Model does not improve over simply predicting the mean.
#R² < 0 → Model performs worse than the mean baseline

##########################################
#Q10. Can KNN be used for regression?
#########################################

#Yes KNN can be used for regression.

#In KNN regression, the model finds the K nearest neighbors and calculates their average target value.

#Example:

#Suppose the salaries of the 3 nearest neighbors are:

#₹30,000
#₹35,000
#₹40,000

#Then:

#Prediction= 3
#30000+35000+40000
#=₹35,000

#KNN can be used for both classification and regression.
	

