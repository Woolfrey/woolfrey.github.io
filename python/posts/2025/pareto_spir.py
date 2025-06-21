import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("~/workspace/woolfrey.github.io/assets/docs/posts/2025/pareto_spir.csv")
df.columns = df.columns.str.strip()
df = df.sort_values(by="Vote", ascending=False)

df["Cumulative"] = df["Vote"].cumsum()
df["Cumulative %"] = 100 * df["Cumulative"] / df["Vote"].sum()

fig, ax1 = plt.subplots(figsize=(10, 6))

x = range(len(df))

# Bar chart for Votes with Dress Blues color (#0A2342)
ax1.bar(x, df["Vote"], color="#2a3244")
ax1.set_ylabel("Votes", fontsize=16)
ax1.set_xlabel("Feature", fontsize=16)
ax1.set_xticks(x)
ax1.set_xticklabels(df["Feature"], rotation=45, ha='right')

# Line chart for cumulative percentage with Super Lemon color (#F5FF00)
ax2 = ax1.twinx()
ax2.plot(x, df["Cumulative %"], color="#e4bf45", marker="o", linestyle="-")
ax2.set_ylabel("Cumulative %", fontsize=14)
ax2.set_ylim(0, 110)

# Set font size
ax1.tick_params(axis='x', labelsize=14)
ax1.tick_params(axis='y', labelsize=14)
ax2.tick_params(axis='y', labelsize=14)

# Remove gridlines
ax1.grid(False)
ax2.grid(False)

# Remove the top spine
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)

plt.tight_layout()
plt.show()
