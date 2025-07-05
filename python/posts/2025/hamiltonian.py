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

# Pendulum parameters
c = 1.0                    # Damping coefficient
g = 9.81                    # Gravitational acceleration        
I = 1.0                     # Moment of inertia
l = 1.0                     # Length of the pendulum
m = 1.0                     # Mass of the pendulum


# Hamiltonian and vector field
def H(p, q):
    return 0.5 * p**2 / I + m * g * l * (1 - np.cos(q))

def hamiltonian_vector_field(p, q):
    dq = p / I
    dp = -m * g * l * np.sin(q) - c * p
    return dq, dp

def simulate_trajectory(p0, q0, dt, steps):
    q_traj = [q0]
    p_traj = [p0]
    for _ in range(steps):
        q = q_traj[-1]
        p = p_traj[-1]
        dp = -m * g * l * np.sin(q) - c * p
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
steps = 225
q_traj, p_traj = simulate_trajectory(p0, q0, dt, steps)

# Grid for phase portrait
q_vals = np.linspace(-2 * np.pi, 2 * np.pi, 300)
p_vals = np.linspace(-10, 10, 300)
Q, P   = np.meshgrid(q_vals, p_vals)
H_vals = H(P, Q)

# Setup figure
fig, ax1 = plt.subplots(figsize=(7, 6), dpi = 200)

# --- Phase portrait ---
contour = ax1.contourf(Q, P, H_vals, levels=20, cmap=custom_cmap)
ax1.plot(q_traj, p_traj, 'r-', label='Trajectory')

# Arrow at the last step
q_last = q_traj[-1]
p_last = p_traj[-1]
dq, dp = hamiltonian_vector_field(p_last, q_last)
ax1.arrow(q_last, p_last, dq * 0.1, dp * 0.1,
          head_width=0.3, head_length=0.5, fc='r', ec='r', label='Final vector')

ax1.set_xlim(-2 * np.pi, 2 * np.pi)
ax1.set_ylim(-10, 10)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_xlabel(r'Configuration $q$', fontsize=20)
ax1.set_ylabel(r'Momentum $p$', fontsize=20)
ax1.xaxis.set_label_coords( 0.50, -0.01)
ax1.yaxis.set_label_coords(-0.01,  0.5)

# Move axes to intersect at (0,0)
ax1.spines['left'].set_position('zero')
ax1.spines['bottom'].set_position('zero')

# Hide the top and right spines
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')

# Enable ticks on bottom and left only
ax1.xaxis.set_ticks_position('top')
ax1.yaxis.set_ticks_position('right')

# (Optional) Add ticks manually if you want control over them
# ...existing code...
ax1.set_xticks([0])
ax1.set_yticks([0])

plt.tight_layout()
plt.show()