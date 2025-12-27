import pandas as pd

# Load dataset
data = pd.read_csv("data/app_usage.csv")

print("Original data:")
print(data.head())

# Convert categorical column 'day_type' to numbers
# weekday -> 0, weekend -> 1
data["day_type"] = data["day_type"].map({
    "weekday": 0,
    "weekend": 1
})

print("\nAfter converting day_type:")
print(data.head())

# Select features (inputs)
X = data[
    [
        "hour",
        "day_type",
        "social_minutes",
        "study_minutes",
        "app_switches",
        "idle_minutes",
        "is_night"
    ]
]

# Target variable (output)
y = data["procrastinated"]

print("\nInput features (X):")
print(X.head())

print("\nTarget variable (y):")
print(y.head())
