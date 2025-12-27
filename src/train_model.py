import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv("data/app_usage.csv")

# Convert day_type to numeric
data["day_type"] = data["day_type"].map({
    "weekday": 0,
    "weekend": 1
})

# Features (inputs)
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

# Target (output)
y = data["procrastinated"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
