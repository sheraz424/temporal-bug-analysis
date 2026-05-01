import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/results.csv")

# -------------------------
# REPO COMPARISON (NONE)
# -------------------------
df["None_Improve"] = df["Early_None"] - df["Late_None"]

plt.figure(figsize=(10,5))
plt.bar(df["Repo"], df["None_Improve"])
plt.xticks(rotation=45)
plt.title("None Bug Improvement per Repository")
plt.ylabel("Improvement (Early - Late)")
plt.tight_layout()
plt.savefig("../none_repo_comparison.png")


# -------------------------
# REPO COMPARISON (EXCEPTION)
# -------------------------
df["Exc_Improve"] = df["Early_Exception"] - df["Late_Exception"]

plt.figure(figsize=(10,5))
plt.bar(df["Repo"], df["Exc_Improve"])
plt.xticks(rotation=45)
plt.title("Exception Bug Improvement per Repository")
plt.ylabel("Improvement (Early - Late)")
plt.tight_layout()
plt.savefig("../exception_repo_comparison.png")