################
# Q1
###############

import numpy as np

data = np.array([6, 7, 8, 9, 10, 11, 12])

mean = np.mean(data)

print("Mean =", mean)

##########################
# Q2
##########################
import numpy as np

data = np.array([6, 7, 8, 9, 10, 11, 12])

variance = np.var(data)
standard_deviation = np.std(data)

print("Variance =", variance)
print("Standard Deviation =", standard_deviation)

#######################
# Q3
######################
import numpy as np
from sklearn.preprocessing import StandardScaler

data = np.array([
    [25, 20000],
    [30, 40000],
    [35, 80000]
])

scaler = StandardScaler()

scaled_data = scaler.fit_transform(data)

print("Scaled Dataset:")
print(scaled_data)

##################
# Q4 
#####################
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import euclidean

# Two points
p1 = np.array([25, 20000])
p2 = np.array([30, 40000])

# Distance before scaling
distance_before = euclidean(p1, p2)

# Apply feature scaling
data = np.array([
    [25, 20000],
    [30, 40000],
    [35, 80000]
])

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Distance after scaling
distance_after = euclidean(scaled_data[0], scaled_data[1])

print("Euclidean Distance Before Scaling:", distance_before)
print("Euclidean Distance After Scaling:", distance_after)

#################################
# Q5. Classification Report
##################################

#A classification report is a performance summary used to evaluate a classification machine learning model.
#It generally contains:

#.Precision
#.Recall
#.F1-score
#.Support
#.Accuracy

#Why is it used?
#It helps us understand how well the model predicts each class instead of looking only at overall accuracy.

#########################################
# Q6 Metrics in a Classification Report
########################################
#1.Precision
#Precision tells us how many of the predicted positive values are actually positive.
#Formula:
#Precision = TP / (TP + FP)
#High precision means there are fewer false positive predictions.

#2.Recall = TP / (TP + FN)

#3.F1 Score = 2 × (Precision × Recall) / (Precision + Recall)

#4.Class 0 → Support = 4

#Class 1 → Support = 4

#5.Accuracy = (TP + TN) / Total Samples

###############################
# Q7 calculate TP, TN, FP, FN
################################
#True Positive (TP) = 3
#True Negative (TN) = 3
#False Positive (FP) = 1
#False Negative (FN) = 1


#########################################
# Q8 prg to calculate TP, TN, FP, AND FN
##########################################
from sklearn.metrics import confusion_matrix

actual = [1, 1, 1, 1, 0, 0, 0, 0]
predicted = [1, 1, 0, 1, 0, 1, 0, 0]

cm = confusion_matrix(actual, predicted)

tn, fp, fn, tp = cm.ravel()

print("True Positive (TP) =", tp)
print("True Negative (TN) =", tn)
print("False Positive (FP) =", fp)
print("False Negative (FN) =", fn)

###########################################
# q9 Generate classification report using 
###########################################

from sklearn.metrics import classification_report

actual = [1, 1, 1, 1, 0, 0, 0, 0]

predicted = [1, 1, 0, 1, 0, 1, 0, 0]

report = classification_report(actual, predicted)

print("Classification Report:")
print(report)