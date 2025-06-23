import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LinearSegmentedColormap

# Custom colours (normalized to [0, 1])
antique_white = np.array([250.0, 235.0, 215.0]) / 255.0
cendre_blue   = np.array([ 61.0, 129.0, 172.0]) / 255.0
dress_blues   = np.array([ 42.0,  50.0,  68.0]) / 255.0
super_lemon   = np.array([232.0, 193.0,  63.0]) / 255.0
white         = np.array([255.0, 255.0, 255.0]) / 255.0

colors = [dress_blues, white, antique_white]
custom_cmap = LinearSegmentedColormap.from_list("my_cmap", colors, N=256)

# Pendulum parameters
m = 1.0
l = 1.0
I = 1.0
g = 9.81

# Hamiltonian and vector field
def H(p, q):
    return 0.5 * p**2 / I + m * g * l * (1 - np.cos(q))

def hamiltonian_vector_field(p, q):
    dq = p / I
    dp = -m * g * l * np.sin(q)
    return dq, dp

# Symplectic Euler integrator
def simulate_trajectory(p0, q0, dt, steps):
    q_traj = [q0]
    p_traj = [p0]
    for _ in range(steps):
        q = q_traj[-1]
        p = p_traj[-1]
        dp = -m * g * l * np.sin(q)
        p_new = p + dt * dp
        dq = p_new / I
        q_new = q + dt * dq
        p_traj.append(p_new)
        q_traj.append(q_new)
    return np.array(q_traj), np.array(p_traj)

# Initial conditions and trajectory
q0 = np.pi / 3
p0 = 2.5
dt = 0.01
steps = 1000
q_traj, p_traj = simulate_trajectory(p0, q0, dt, steps)

# Grid for phase portrait
q_vals = np.linspace(-2 * np.pi, 2 * np.pi, 300)
p_vals = np.linspace(-10, 10, 300)
Q, P   = np.meshgrid(q_vals, p_vals)
H_vals = H(P, Q)

# Setup figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# --- Phase portrait (left) ---
contour = ax1.contourf(Q, P, H_vals, levels=20, cmap=custom_cmap)
dot, = ax1.plot([], [], 'ro')
ax1.set_xlim(-2 * np.pi, 2 * np.pi)
ax1.set_ylim(-10, 10)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_title("Phase Portrait (q, p)")

# --- Pendulum animation (right) ---
pendulum_line, = ax2.plot([], [], 'o-', lw=5, color='black')
ax2.set_xlim(-1.2, 1.2)
ax2.set_ylim(-1.2, 0.2)
ax2.set_aspect('equal')
ax2.axis('off')
ax2.set_title("Pendulum Motion")

# Mutable container for the arrow
arrow_artist = [None]

def update(frame):
    q = q_traj[frame]
    p = p_traj[frame]

    dot.set_data([q], [p])

    if arrow_artist[0] is not None:
        arrow_artist[0].remove()

    dq, dp = hamiltonian_vector_field(p, q)
    arrow_artist[0] = ax1.arrow(q, p, dq * 0.3, dp * 0.3,
                                head_width=0.3, head_length=0.5, fc='r', ec='r')

    x = l * np.sin(q)
    y = -l * np.cos(q)
    pendulum_line.set_data([0, x], [0, y])

    return dot, arrow_artist[0], pendulum_line

# Create animation
ani = FuncAnimation(fig, update, frames=steps, interval=20, blit=False)
plt.tight_layout()
plt.show()