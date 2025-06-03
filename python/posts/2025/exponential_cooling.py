#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 26 16:21:30 2025

@author: woolfrey
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.patches import FancyArrowPatch

###############################################################################
#                             Parameters & functions                          #
###############################################################################

# Parameters
image_res = 200
k         = -0.6                                                                # Time constant
phi       = 1.618                                                               # Golden ratio; for scaling figures                             
tau_amb   = 20                                                                  # Ambient temperature
tau0      = 60                                                                  # Initial temperature
t_span    = (0, 10)                                                             # Time span
t_eval    = np.linspace(*t_span, 300)                                           # Generate array

# Define ordinary differential equation
def cooling_ode(t, tau):
    return -k * (tau_amb - tau)

solution = solve_ivp(cooling_ode, t_span, [tau0], t_eval=t_eval)                # Solve ODE for temperature
tau      = solution.y[0]                                                        # Initial value
epsilon  = tau_amb - tau                                                        # Difference

# This is for drawing nice arrows at the end of spines
def add_axis_arrow(ax, direction='x', size=8):
    """Adds a triangle at the end of the axis."""
    if direction == 'x':
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        ax.add_patch(FancyArrowPatch((xlim[1], ylim[0]), (xlim[1]+0.1, ylim[0]),
                                     arrowstyle='-|>', mutation_scale=size, color='black',
                                     linewidth=0.8, clip_on=False))
    elif direction == 'y':
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        ax.add_patch(FancyArrowPatch((xlim[0], ylim[1]), (xlim[0], ylim[1]+0.5),
                                     arrowstyle='-|>', mutation_scale=size, color='black',
                                     linewidth=0.8, clip_on=False))

###############################################################################
#                                Plot Temperature                             #
###############################################################################
fig1, ax1 = plt.subplots(figsize=(3*phi, 3), dpi=200)

ax1.axhline(tau_amb, color='gray', linewidth=1)                                 # Reference line

ax1.plot(solution.t, tau, color='black', linewidth=2)                           # Plot the solution

# Draw an arrow at the end of the curve
ax1.annotate('', 
    xy=(solution.t[-1], tau[-1]),                                               # end point of curve
    xytext=(solution.t[-2], tau[-2]),                                           # a point just before end, to get arrow direction
    arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

# Labeling on spines
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.tick_params(left=True, bottom=False, labelleft=True, labelbottom=False)
ax1.set_yticks([tau0, tau_amb])
ax1.set_yticklabels([r'$\tau_0$', r'$\tau_{\mathrm{amb}}.$'], fontsize=12)  # set corresponding labels

# Axis limits
xlim = ax1.get_xlim()
ylim = ax1.get_ylim()

# Add arrows at ends of spines
add_axis_arrow(ax1, 'x')
add_axis_arrow(ax1, 'y')

# Labels
ax1.set_xlabel('Time $(s)$', labelpad=10)
ax1.set_ylabel(r'Temperature ($^{\circ}$C)', labelpad=10)


plt.tight_layout()
plt.show()

###############################################################################
#                                 Plot Difference                             #
###############################################################################
fig2, ax2 = plt.subplots(figsize=(3*phi, 3), dpi=200)

ax2.axhline(0, color='gray', linewidth=1)

ax2.plot(solution.t, epsilon, color='black', linewidth=2)

ax2.annotate('', 
    xy=(solution.t[-1], epsilon[-1]),
    xytext=(solution.t[-2], epsilon[-2]),
    arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

ax2.tick_params(left=True, bottom=False, labelleft=True, labelbottom=False)
ax2.set_yticks([tau_amb-tau0, 0])
ax2.set_yticklabels([r'$\epsilon_0$', r'$0$'], fontsize=12)

xlim = ax2.get_xlim()
ylim = ax2.get_ylim()

add_axis_arrow(ax2, 'x')
add_axis_arrow(ax2, 'y')

ax2.set_xlabel('Time $(s)$', labelpad=10)
ax2.set_ylabel(r'Difference ($^{\circ}$C)', labelpad=10)

plt.tight_layout()
plt.show()