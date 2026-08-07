import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

print("Total Students:", len(df))
print("Passed Students:", (df["FinalResult"] == 1).sum())
print("Failed Students:", (df["FinalResult"] == 0).sum())