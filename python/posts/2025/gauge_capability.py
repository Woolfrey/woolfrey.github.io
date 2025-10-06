import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Custom colours (normalized to [0, 1])
antique_white = np.array([250.0, 235.0, 215.0]) / 255.0
cendre_blue   = np.array([ 61.0, 129.0, 172.0]) / 255.0
dress_blues   = np.array([ 42.0,  50.0,  68.0]) / 255.0
super_lemon   = np.array([232.0, 193.0,  63.0]) / 255.0
white         = np.array([255.0, 255.0, 255.0]) / 255.0

# Figure
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6), sharex=True)

# Common x-range
sigma_small = 1
sigma_large = 6
x_min = -18
x_max = 18
x_common = np.linspace(x_min, x_max, 1000)

# ------------------------
# Top subplot: standard normal
# ------------------------
mu1 = 0
sigma1 = sigma_small
y1 = norm.pdf(x_common, mu1, sigma1)
ax1.plot(x_common, y1, color=dress_blues, lw=2)
ax1.fill_between(x_common, 0, y1,
                 where=(x_common >= mu1 - 3*sigma1) & (x_common <= mu1 + 3*sigma1),
                 color=cendre_blue, alpha=0.2)
ax1.axis('off')
ax1.set_xlim(x_min, x_max)

# ------------------------
# Bottom subplot: σ = 6
# ------------------------
mu2 = 0
sigma2 = sigma_large
y2 = norm.pdf(x_common, mu2, sigma2)
ax2.plot(x_common, y2, color=dress_blues, lw=2)
ax2.fill_between(x_common, 0, y2,
                 where=(x_common >= mu2 - 3*sigma2) & (x_common <= mu2 + 3*sigma2),
                 color=cendre_blue, alpha=0.2)

# Remove all spines and y-axis ticks
for spine in ax2.spines.values():
    spine.set_visible(False)
ax2.set_yticks([])

# Ticks every 3 units, labeled as multiples of σ
tick_positions = np.arange(-18, 19, 3)
tick_labels = []
for pos in tick_positions:
    if pos == 0:
        tick_labels.append(r"$\mu$")
    elif pos > 0:
        tick_labels.append(r"$+" + f"{pos}" + r"\sigma$")
    else:
        tick_labels.append(r"$" + f"{pos}" + r"\sigma$")
ax2.set_xticks(tick_positions)
ax2.set_xticklabels(tick_labels, fontsize=12)
ax2.tick_params(axis='x', direction='out', length=5)

ax1.set_title("Gauge R&R:", loc='left')
ax2.set_title("Part-to-Part Variation:", loc='left')

plt.tight_layout()
plt.show()