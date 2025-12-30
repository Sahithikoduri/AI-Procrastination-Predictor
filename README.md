# AI-Procrastination-Predictor 🧠

An AI-driven system that **predicts procrastination risk before it happens** using behavioral app-usage patterns and provides **timely intervention messages** to help users avoid long distraction cycles.

---

## 🚀 Overview

Most productivity apps only show screen time *after* time is already wasted.  
This project takes a **proactive approach**.

It analyzes app-usage behavior to:
- Predict when a user is **likely to procrastinate**
- Identify **low-distraction focus windows**
- Trigger **adaptive intervention messages** to help users act early

The system is designed as a **proof-of-concept** for intelligent digital wellbeing tools.

---

## ❓ Problem Statement

Procrastination is not caused by lack of motivation alone, but by **repeated behavioral patterns** such as late-night phone usage, frequent app switching, and social media overuse.

Existing timer-based apps:
- React after distraction happens
- Use fixed reminders
- Do not adapt to personal behavior

This project aims to **predict and intervene** before prolonged distraction begins.

---

## 🧠 How the System Works

1. **Behavior Data Collection (Simulated)**
   - Hourly app-usage behavior
   - Social media time
   - Study time (self-reported)
   - App switching frequency
   - Time-of-day indicators

2. **Data Preprocessing**
   - Encoding categorical variables
   - Feature selection
   - Preparing data for ML models

3. **Machine Learning Model**
   - Logistic Regression
   - Predicts probability of procrastination (0–1)

4. **Risk Estimation**
   - Low risk → no interruption
   - Medium risk → gentle warning
   - High risk → strong motivational intervention

5. **Intervention Logic**
   - Messages adapt based on predicted risk
   - Focuses on guidanc
