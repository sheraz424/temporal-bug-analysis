import pandas as pd

df = pd.read_csv("results/results.csv")

# Average trends
print("\nAVERAGE TRENDS")

print("None Early:", df["Early_None"].mean())
print("None Late:", df["Late_None"].mean())

print("Exception Early:", df["Early_Exception"].mean())
print("Exception Late:", df["Late_Exception"].mean())


# Improvement score (Early - Late)
df["none_improve"] = df["Early_None"] - df["Late_None"]
df["exc_improve"] = df["Early_Exception"] - df["Late_Exception"]

print("\nBEST IMPROVEMENT (None bugs)")
print(df.sort_values("none_improve", ascending=False)[["Repo", "none_improve"]])

print("\nBEST IMPROVEMENT (Exception bugs)")
print(df.sort_values("exc_improve", ascending=False)[["Repo", "exc_improve"]])