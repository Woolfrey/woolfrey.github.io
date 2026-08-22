"""
Load cause/votes data from a CSV and plot it as a column chart
using tufteplotlib's column_chart function.
"""

import pandas as pd
import matplotlib.pyplot as plt
from tufteplotlib.plots import column_chart  # adjust import path if column_chart lives elsewhere

plt.rcParams['figure.dpi'] = 150

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
CSV_PATH = "../../../assets/data/ishikawa_tally_inspections.csv"      # path to your CSV file
SORT = "desc"                 # 'alpha', 'alpha_desc', 'asc', or 'desc' (by votes)
COLOR = "#2a3244"             # set to a single color for all bars, or None for default gray

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------
df = pd.read_csv(CSV_PATH)
df.columns = [c.strip().lower() for c in df.columns]  # normalize column names

categories = df["cause"].to_list()
values = df["votes"].to_list()

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
colors = [COLOR] if COLOR else None

fig, ax = column_chart(
    categories,
    values,
    colors=colors,
    sort=SORT,
)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

plt.tight_layout()
plt.show()

# To save instead of / as well as showing:
# fig.savefig("causes_chart.png", dpi=150, bbox_inches="tight")
