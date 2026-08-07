import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

counts = df["FinalResult"].value_counts()
percentage = df["FinalResult"].value_counts(normalize=True) * 100

print("Counts:")
print(counts)

print("\nPercentage:")
print(percentage)

if abs(percentage[1] - percentage[0]) < 10:
    print("\nDataset is Balanced.")
else:
    print("\nDataset is Imbalanced.")