import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data/app_usage.csv")

# 1. Procrastination count by hour
plt.figure()
data.groupby("hour")["procrastinated"].sum().plot(kind="bar")
plt.title("Procrastination Frequency by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Procrastination Count")
plt.show()

# 2. Average social media usage by hour
plt.figure()
data.groupby("hour")["social_minutes"].mean().plot(kind="line", marker="o")
plt.title("Average Social Media Usage by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Minutes")
plt.show()

# 3. Average study time by hour
plt.figure()
data.groupby("hour")["study_minutes"].mean().plot(kind="line", marker="o")
plt.title("Average Study Time by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Minutes")
plt.show()
