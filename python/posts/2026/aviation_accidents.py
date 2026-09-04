import pandas as pd
import matplotlib.pyplot as plt
from tufteplotlib.plots import line_plot

# Configuration
START_YEAR = 1940
END_YEAR = 2020

# Load data
df = pd.read_csv("../../../assets/data/aviation-accident-data-2023-05-16.csv")

# Remove records with unknown year
df = df[df["year"] != "unknown"].copy()

# keep only genuine accidents (hull-loss + repairable), drop occurrences/unknowns
df = df[df["cat"].isin(["A1", "A2"])]

# Convert year to integer
df["year"] = df["year"].astype(int)

# Filter year range
df = df[
    (df["year"] >= START_YEAR) &
    (df["year"] <= END_YEAR)
]

# Convert fatalities to numeric (missing/blank values become NaN)
df["fatalities"] = pd.to_numeric(df["fatalities"], errors="coerce")

# Count accidents per year
accidents = (
    df.groupby("year")
      .size()
      .reset_index(name="accidents")
)

# Sum fatalities per year
fatalities = (
    df.groupby("year")["fatalities"]
      .sum()
      .reset_index(name="fatalities")
)

# --- Create 2x1 subplot grid, sharing the x-axis ---
fig, (ax1, ax2) = plt.subplots(
    2, 1,
    figsize=(7, 4),
    sharex=True
)

# Top: Accidents vs. year
line_plot(
    accidents["year"],
    accidents["accidents"],
    ax=ax1,
    linewidth=1.5
)
ax1.set_xlim(START_YEAR, END_YEAR)
ax1.set_ylabel("No. of accidents")

# Remove the bottom spine on the top subplot
ax1.spines["bottom"].set_visible(False)
ax1.tick_params(axis="x", bottom=False, labelbottom=False)
ax1.set_xlabel("")

# Bottom: Fatalities vs. year
line_plot(
    fatalities["year"],
    fatalities["fatalities"],
    ax=ax2,
    linewidth=1.5
)
ax2.set_xlim(START_YEAR, END_YEAR)
ax2.set_xlabel("Year")
ax2.set_ylabel("No. of fatalities")

plt.tight_layout()

fig.savefig(
    "../../../assets/images/posts/2026/aviation_accidents.png",
    dpi=200,
    transparent=True
)
plt.show()
