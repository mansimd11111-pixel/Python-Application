#############################
# All required imports 
#############################

import pandas as pd             
import matplotlib.pyplot as plt                 
from sklearn.preprocessing import MinMaxScaler

# Load Dataset 

df = pd.read_csv("student_performance_ml.csv")

# Display the dataset
print("Original Datset: ")
print(df)

################################
# Q1 : MIN MAX SCALING 
###############################

scaler = MinMaxScaler()

# Normalize Math marks
df['Math_Normalized'] = scaler.fit_transform(df[['Math']])

print("Math scores after Min-Max Scaling:")
print(df[['Math','Math_Normalized']])

###############################
# Q2: ONE-HOT ENCODING
##############################

# Create Gender column if it does not already exist
# Example:
# df['Gender'] = ['Male', 'Female', 'Male', 'Female', ...]

# Perform one-hot encoding
df = pd.get_dummies(df, columns=['Gender'], dtype=int)

print("Dataset after One-Hot Encoding:")
print(df)

##############################
# Q3: GROUP BY GENDER
#############################

# Reload original dataset if necessary
df_original = pd.read_csv("student_performance_ml.csv")

# Calculate average marks by gender
average_marks = df_original.groupby('Gender')[['Math','English']].mean()

print("Average Marks by Gender:")
print(average_marks)

##############################
# Q4: PIE CHART FOR SAGAR
#############################

# Find Sagar's record
sagar = df_original[df_original['Name'] == 'Sagar'].iloc[0]

# Select subject marks
subjects = ['Math', 'English']
marks = [sagar['Math'], sagar['English']]

# Create pie chart
plt.figure(figsize=(6, 6))

plt.pie(
    marks,
    labels=subjects,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Subject Marks of Sagar")
plt.show()

##############################
# Q5: ADD STATUS COLUMN
#############################

# Calculate total marks
# Change/add subjects according to your dataset
df_original['Total'] = (
    df_original['Math'] +
    df_original['English']
)

# Add Status column
df_original['Status'] = df_original['Total'].apply(
    lambda x: 'Pass' if x >= 250 else 'Fail'
)

print("Dataset with Status:")
print(df_original)

df_original['Total'] = (
    df_original['Math'] +
    df_original['English'] +
    df_original['Science']
)

df_original['Status'] = df_original['Total'].apply(
    lambda x: 'Pass' if x >= 250 else 'Fail'
)

################################
# Q6: COUNT PASSED STUDENTS
################################

passed_students = (df_original['Status'] == 'Pass').sum()

print("Number of students passed:", passed_students)

###############################
# Q7: EXPORT DATAFRAME TO CSV
###############################

df_original.to_csv(
    "final_student_performance_ml.csv",
    index=False
)

print("Final DataFrame exported successfully")

#################################
# Q8: HISTOGRAM OF MATH MARKS
################################

plt.figure(figsize=(8, 5))

plt.hist(
    df_original['Math'],
    bins=5,
    edgecolor='black'
)

plt.title("Distribution of Math Marks")
plt.xlabel("Math Marks")
plt.ylabel("Number of Students")

plt.show()

################################
# Q9: RENAME COLUMN
################################

df_original.rename(
    columns={'Math': 'Mathematics'},
    inplace=True
)

print("Column renamed successfully")
print(df_original.columns)

####################################
# Q10: BOXPLOT OF ENGLISH MARKS
###################################

plt.figure(figsize=(6, 5))

plt.boxplot(
    df_original['English'],
    vert=True
)

plt.title("Boxplot of English Marks")
plt.ylabel("English Marks")

plt.show()