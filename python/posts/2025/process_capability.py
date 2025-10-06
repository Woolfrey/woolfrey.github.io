import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Custom colours (normalized to [0, 1])
antique_white = np.array([250.0, 235.0, 215.0]) / 255.0
cendre_blue   = np.array([ 61.0, 129.0, 172.0]) / 255.0
dress_blues   = np.array([ 42.0,  50.0,  68.0]) / 255.0
super_lemon   = np.array([232.0, 193.0,  63.0]) / 255.0
white         = np.array([255.0, 255.0, 255.0]) / 255.0

# Standard normal distribution
mu = 0
sigma = 1
x = np.linspace(-4*sigma, 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)

# Create the plot
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, color=dress_blues, lw=2)

# Fill ±3σ region
ax.fill_between(x, 0, y, where=(x >= -3*sigma) & (x <= 3*sigma), color=cendre_blue, alpha=0.3)

# Labels at sigma positions
sigma_positions = [-3, -2, -1, 0, 1, 2, 3]
sigma_labels = [r"$-3\sigma$", r"$-2\sigma$", r"$-1\sigma$", r"$\mu$", r"$+1\sigma$", r"$+2\sigma$", r"$+3\sigma$"]
ax.set_xticks(sigma_positions)
ax.set_xticklabels(sigma_labels, fontsize=12)

# Vertical lines at -3σ and +3σ
ax.axvline(-3*sigma, color=super_lemon, lw=1)
ax.axvline(3*sigma, color=super_lemon, lw=1)

# LSL and USL labels
y_max = max(y)
ax.text(-3*sigma, y_max*1.05, "LSL", ha='center', va='bottom', fontsize=12, color=super_lemon)
ax.text(3*sigma, y_max*1.05, "USL", ha='center', va='bottom', fontsize=12, color=super_lemon)

# Remove top, left, right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# Remove grid and y-axis ticks
ax.grid(False)
ax.set_yticks([])

plt.tight_layout()
plt.show()