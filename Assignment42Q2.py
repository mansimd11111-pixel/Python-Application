import math

# Dataset
data = [
    (1, 2, "Red"),
    (2, 3, "Red"),
    (3, 1, "Blue"),
    (6, 5, "Blue")
]

# New point
x = 2
y = 2

# Calculate distances
distances = []

for px, py, label in data:
    distance = math.sqrt((x - px) * 2 + (y - py) * 2)
    distances.append((distance, label))

# Sort distances
distances.sort()

# Function for KNN prediction

def knn_predict(k):
    neighbors = distances[:k]

    labels = [label for distance, label in neighbors]

    red_count = labels.count("Red")
    blue_count = labels.count("Blue")

    if red_count > blue_count:
        return "Red"
    elif blue_count > red_count:
        return "Blue"
    else:
        # Tie-breaking rule
        return "Blue"


print("Prediction Results\n")

for k in [1, 3, 4]:
    prediction = knn_predict(k)
    print(f"K = {k} → {prediction}")