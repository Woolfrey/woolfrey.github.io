import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Custom colours (normalized to [0, 1])
antique_white = np.array([250.0, 235.0, 215.0]) / 255.0
cendre_blue   = np.array([ 61.0, 129.0, 172.0]) / 255.0
dress_blues   = np.array([ 42.0,  50.0,  68.0]) / 255.0
super_lemon   = np.array([232.0, 193.0,  63.0]) / 255.0
white         = np.array([255.0, 255.0, 255.0]) / 255.0

colors = [dress_blues, white, antique_white]
custom_cmap = LinearSegmentedColormap.from_list("my_cmap", colors, N=256)

# Mass-spring-damper parameters
m = 1.0   # mass
k = 1.0   # spring constant
x0 = 0.0  # equilibrium position

# Energy function: E(x, v) = 0.5*m*v^2 + 0.5*k*(x-x0)^2
def energy(x, v):
    return 0.5 * m * v**2 + 0.5 * k * (x - x0)**2

# Create grid
x = np.linspace(-3, 3, 200)
v = np.linspace(-3, 3, 200)
X, V = np.meshgrid(x, v)
E = energy(X, V)

# Plot 3D surface
fig = plt.figure(figsize=(8, 6), dpi=200)
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, V, E, cmap=custom_cmap, edgecolor='none', antialiased=True, alpha=1.0)

ax.set_xlabel('Position $x$', fontsize=14, labelpad=10)
ax.set_ylabel('Velocity $\dot{x}$', fontsize=14, labelpad=10)
ax.set_zlabel('Energy $E$', fontsize=14, labelpad=10)

# Remove grid lines
ax.grid(False)
ax.xaxis._axinfo['grid'].update(color = (1,1,1,0))
ax.yaxis._axinfo['grid'].update(color = (1,1,1,0))
ax.zaxis._axinfo['grid'].update(color = (1,1,1,0))

# Set ticks to only show 0 on each axis
ax.set_xticks([0])
ax.set_yticks([0])
ax.set_zticks([0])

# Remove the grey background panels (panes)
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

# Remove grid lines
ax.grid(False)
ax.xaxis._axinfo['grid'].update(color = (1,1,1,0))
ax.yaxis._axinfo['grid'].update(color = (1,1,1,0))
ax.zaxis._axinfo['grid'].update(color = (1,1,1,0))

plt.tight_layout()
plt.show()