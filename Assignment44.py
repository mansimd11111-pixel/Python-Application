import pandas as pd     
import numpy as np                 
import matplotlib.pyplot as plt              

# Create a dictionary containing student marks
data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

# Create a DataFrame using the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print("Student Data:")
print(df)
# Print the shape of the DataFrame
print("\nShape of DataFrame:")
print(df.shape)

# Print the column names
print("\nColumns:")
print(df.columns)

# Print the data types of each column
print("\nData Types:")
print(df.dtypes)

#################################################
# print descriptive statistic using .describe()
################################################
# Display descriptive statistics of numerical columns

print(df.describe())

################################
# Add a new Total column 
###############################

# Calculate the total marks of each student
# by adding Math, Science and English marks
df['Total'] = df['Math'] + df['Science'] + df['English']

# Display the updated DataFrame
print(df)

#####################################################
# Display students who scored more than 85 in Science
#####################################################

# Select students whose Science marks are greater than 85
students = df[df['Science'] > 85]

# Display the selected students
print(students)

# Replace the name 'Pooja' with 'Puja'
df['Name'] = df['Name'].replace('Pooja', 'Puja')

# Display the updated DataFrame
print(df)

#######################################################
# Sort the DataFrame according to Total marks
# ascending=False means highest marks will come first
########################################################
df_sorted = df.sort_values(by='Total', ascending=False)

# Display the sorted DataFrame
print(df_sorted)

######################
# Create a bar chart
######################
plt.bar(df['Name'], df['Total'])

# Give a label to X-axis
plt.xlabel('Student Name')

# Give a label to Y-axis
plt.ylabel('Total Marks')

# Give a title to the graph
plt.title('Student Names vs Total Marks')

# Display the graph
plt.show()

# Select the row containing Amit's marks
amit = df[df['Name'] == 'Amit']

# Store subject names in a list
subjects = ['Math', 'Science', 'English']

# Store Amit's marks in a list
marks = [
    amit['Math'].values[0],
    amit['Science'].values[0],
    amit['English'].values[0]
]

# Create a line chart
plt.plot(subjects, marks, marker='o')

# Give a label to X-axis
plt.xlabel('Subjects')

# Give a label to Y-axis
plt.ylabel('Marks')

# Give a title to the graph
plt.title("Amit's Marks Across All Subjects")

# Display the graph
plt.show()

##################################################
# Create a dictionary containing missing values
##################################################
data2 = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [np.nan, 76, 88],
    'Science': [91, np.nan, 85]
}

# Create a DataFrame
df2 = pd.DataFrame(data2)

# Display the DataFrame before filling missing values
print("Before filling missing values:")
print(df2)

# Calculate the mean of Math column
# and replace the missing value with the mean
df2['Math'] = df2['Math'].fillna(df2['Math'].mean())

# Calculate the mean of Science column
# and replace the missing value with the mean
df2['Science'] = df2['Science'].fillna(df2['Science'].mean())

# Display the DataFrame after filling missing values
print("\nAfter filling missing values:")
print(df2)

# Remove the English column from the DataFrame
df = df.drop('English', axis=1)

# Display the updated DataFrame
print(df)