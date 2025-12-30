import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

st.set_page_config(page_title="Procrastination Intervention", layout="centered")

st.title("🧠 Procrastination Intervention System")
st.write(
    "This app predicts **procrastination risk before it happens** "
    "and provides timely intervention messages."
)

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

st.header("📱 Simulate Current Phone Usage")

hour = st.slider("Hour of the day", 0, 23, 21)
day_type = st.selectbox("Day type", ["weekday", "weekend"])
social_minutes = st.slider("Social media minutes (this hour)", 0, 60, 40)
study_minutes = st.slider("Study minutes (this hour)", 0, 60, 5)
app_switches = st.slider("App switches", 0, 30, 16)
idle_minutes = st.slider("Idle minutes", 0, 60, 0)

is_night = 1 if hour >= 20 or hour <= 5 else 0
day_type_val = 0 if day_type == "weekday" else 1

current_behavior = pd.DataFrame([{
    "hour": hour,
    "day_type": day_type_val,
    "social_minutes": social_minutes,
    "study_minutes": study_minutes,
    "app_switches": app_switches,
    "idle_minutes": idle_minutes,
    "is_night": is_night
}])

if st.button("🔮 Predict Procrastination Risk"):
    risk = model.predict_proba(current_behavior)[0][1]

    st.subheader("⚠️ Risk Assessment")
    st.write(f"**Procrastination Risk Probability:** {risk:.2f}")

    if risk < 0.4:
        st.success("Low risk. This is a good time to focus.")
    elif risk < 0.7:
        st.warning(
            "Moderate risk of distraction.\n\n"
            "Try putting the phone aside for the next 10 minutes."
        )
    else:
        st.error(
            "🚨 HIGH RISK of procrastination!\n\n"
            "Based on your past behavior, this often leads to long scrolling.\n"
            "Put the phone down and start with just 5 minutes of study."
        )
