import pandas as pd
from sklearn.linear_model import LogisticRegression

# Load dataset
data = pd.read_csv("data/app_usage.csv")

# Encode day_type
data["day_type"] = data["day_type"].map({
    "weekday": 0,
    "weekend": 1
})

# Features and target
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
y = data["procrastinated"]

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# -------- SIMULATE CURRENT USER BEHAVIOR --------
current_behavior = pd.DataFrame([{
    "hour": 21,
    "day_type": 0,
    "social_minutes": 40,
    "study_minutes": 5,
    "app_switches": 16,
    "idle_minutes": 0,
    "is_night": 1
}])

# Predict procrastination probability
risk_probability = model.predict_proba(current_behavior)[0][1]

print("Procrastination Risk Probability:", round(risk_probability, 2))

# -------- INTERVENTION LOGIC --------
if risk_probability < 0.4:
    message = "Low risk. Good time to focus."
elif risk_probability < 0.7:
    message = (
        "⚠️ Moderate risk of distraction.\n"
        "Try to limit phone usage for the next 10 minutes."
    )
else:
    message = (
        "🚨 HIGH RISK of procrastination!\n"
        "Based on your past behavior, opening the phone now usually leads to long scrolling.\n"
        "Put the phone down and start with just 5 minutes of study."
    )

print("\nIntervention Message:")
print(message)
