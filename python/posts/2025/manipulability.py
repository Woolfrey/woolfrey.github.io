import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LinearSegmentedColormap


# Custom colours (normalized to [0, 1])
antique_white = np.array([250.0, 235.0, 215.0]) / 255.0
cendre_blue   = np.array([ 61.0, 129.0, 172.0]) / 255.0
dress_blues   = np.array([ 42.0,  50.0,  68.0]) / 255.0
super_lemon   = np.array([232.0, 193.0,  63.0]) / 255.0
white         = np.array([255.0, 255.0, 255.0]) / 255.0

colors = [dress_blues, white, antique_white]
custom_cmap = LinearSegmentedColormap.from_list("my_cmap", colors, N=256)

def plot_planar_3R_manipulability(theta1=0.0, l1=1.0, l2=1.0, l3=1.0):
    """
    Plots the manipulability of a 3R planar robot as a function of theta2 and theta3.
    
    Parameters:
    - theta1: fixed value of the first joint (in radians)
    - l1, l2, l3: link lengths
    """
    # Create a grid of theta2 and theta3
    theta2_vals = np.linspace(-np.pi, np.pi, 300)
    theta3_vals = np.linspace(-np.pi, np.pi, 300)
    Theta2, Theta3 = np.meshgrid(theta2_vals, theta3_vals)

    # Initialize manipulability array
    w = np.zeros_like(Theta2)

    # Compute manipulability for each (theta2, theta3)
    for i in range(Theta2.shape[0]):
        for j in range(Theta2.shape[1]):
            theta2 = Theta2[i, j]
            theta3 = Theta3[i, j]

            # Full 3x3 Jacobian for planar XY
            J = np.zeros((2, 3))
            # Partial derivatives of x w.r.t theta1, theta2, theta3
            J[0, 0] = -l1*np.sin(theta1) - l2*np.sin(theta1 + theta2) - l3*np.sin(theta1 + theta2 + theta3)
            J[0, 1] = -l2*np.sin(theta1 + theta2) - l3*np.sin(theta1 + theta2 + theta3)
            J[0, 2] = -l3*np.sin(theta1 + theta2 + theta3)

            # Partial derivatives of y w.r.t theta1, theta2, theta3
            J[1, 0] =  l1*np.cos(theta1) + l2*np.cos(theta1 + theta2) + l3*np.cos(theta1 + theta2 + theta3)
            J[1, 1] =  l2*np.cos(theta1 + theta2) + l3*np.cos(theta1 + theta2 + theta3)
            J[1, 2] =  l3*np.cos(theta1 + theta2 + theta3)

            # Manipulability (Yoshikawa)
            w[i, j] = np.sqrt(np.linalg.det(J @ J.T))

    # Plot manipulability as a 3D surface
    fig = plt.figure(figsize=(10,7))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(Theta2, Theta3, w, cmap=custom_cmap, edgecolor=[0.7, 0.7, 0.7], linewidth=0.1, antialiased=True, alpha = 0.75)

    # Turn off grid
    ax.grid(False)

    # Axis limits and ticks (-pi to pi)
    ax.set_xlim([-np.pi, np.pi])
    ax.set_ylim([-np.pi, np.pi])
    ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
    ax.set_yticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
    ax.set_zticks([])

    # Label ticks nicely
    ax.set_xticklabels([r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
    ax.set_yticklabels([r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])

    # Set labels
    ax.set_xlabel(r'$\theta_2$ (rad)')
    ax.set_ylabel(r'$\theta_3$ (rad)')
    ax.set_zlabel('Manipulability')

    # Remove background panes
    ax.xaxis.pane.set_facecolor((1, 1, 1, 1))  # RGBA, alpha=0 → fully transparent
    ax.yaxis.pane.set_facecolor((1, 1, 1, 1))
    ax.zaxis.pane.set_facecolor((1, 1, 1, 1))

    plt.show()

# Example usage: set theta1 = pi/4
plot_planar_3R_manipulability(theta1=np.pi/4)
