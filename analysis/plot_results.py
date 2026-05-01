import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("results.csv")

# -----------------------------
# GRAPH 1: Average None Density
# -----------------------------
avg_early = df["Early_None"].mean()
avg_middle = df["Middle_None"].mean()
avg_late = df["Late_None"].mean()

phases = ["Early", "Middle", "Late"]
values = [avg_early, avg_middle, avg_late]

plt.figure(figsize=(8,5))
plt.plot(phases, values, marker="o", linewidth=2)
plt.title("Average None-Issue Density Over Time")
plt.ylabel("Issues per KLOC")
plt.grid(True)
plt.savefig("none_trend.png")
plt.show()

# -----------------------------
# GRAPH 2: Average Exception Density
# -----------------------------
avg_early = df["Early_Exception"].mean()
avg_middle = df["Middle_Exception"].mean()
avg_late = df["Late_Exception"].mean()

values = [avg_early, avg_middle, avg_late]

plt.figure(figsize=(8,5))
plt.plot(phases, values, marker="o", linewidth=2)
plt.title("Average Exception-Issue Density Over Time")
plt.ylabel("Issues per KLOC")
plt.grid(True)
plt.savefig("exception_trend.png")
plt.show()