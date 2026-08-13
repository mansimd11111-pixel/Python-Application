import math

# Dataset
data = [
    (1, 2, "Red"),
    (2, 3, "Red"),
    (3, 1, "Blue"),
    (6, 5, "Blue")
     ]

# Accept new point
x = float(input("Enter X coordinate: "))
y = float(input("Enter Y coordinate: "))

# Calculate Euclidean distances
distances = []

for px, py, label in data:
    distance = math.sqrt((x - px) * 2 + (y - py) * 2)
    distances.append((distance, label))

# Sort distances
distances.sort()

# Select K = 3 nearest neighbors
k = 3
neighbors = distances[:k]

# Display nearest neighbors
print("\nNearest Neighbors:")
for distance, label in neighbors:
    print(f"{label} - Distance: {distance:.2f}")

# Majority voting
labels = [label for distance, label in neighbors]

red_count = labels.count("Red")
blue_count = labels.count("Blue")

if red_count > blue_count:
    prediction = "Red"
else:
    prediction = "Blue"

print("\nPredicted Class:", prediction)