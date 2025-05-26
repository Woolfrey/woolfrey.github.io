#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 26 16:21:30 2025

@author: woolfrey
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters
k = -0.6                                            # Cooling constant
tau_amb = 20                                        # Ambient temperature in degrees Celsius
tau0 = 60                                           # Initial temperature
t_span = (0, 10)                                    # Time span in seconds
t_eval = np.linspace(*t_span, 300)                  # Time points for evaluation

# Differential equation: dτ/dt = -k (τ_amb - τ)
def cooling_ode(t, tau):
    return -k * (tau_amb - tau)

# Solve the ODE
sol = solve_ivp(cooling_ode, t_span, [tau0], t_eval=t_eval)
tau = sol.y[0]
epsilon = tau_amb - tau  # Error

phi = 1.618  # Golden ratio for figure sizing

# === Plot 1: Temperature ===
fig1, ax1 = plt.subplots(figsize=(3*phi, 3), dpi=100)
ax1.plot(sol.t, tau, color='black', linewidth=2)

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.grid(False)
ax1.set_xlabel('Time $(s)$')
ax1.set_ylabel(r'Temperature ($^{\circ}$C)')

ax1.axhline(tau_amb, color='gray', linewidth=1)
ax1.text(
    x=1.0,
    y=tau_amb + 0.5,
    s=r'$\tau_{\mathrm{amb}}$',
    ha='right', va='bottom',
    color='gray',
    fontsize=14
)

plt.tight_layout()
plt.show()

# === Plot 2: Error ===
fig2, ax2 = plt.subplots(figsize=(3*phi, 3), dpi=100)
ax2.plot(sol.t, epsilon, color='tab:red', linewidth=2)

ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.grid(False)
ax2.set_xlabel('Time $(s)$')
ax2.set_ylabel(r'$\epsilon = \tau_{\mathrm{amb}} - \tau$ ($^{\circ}$C)')

plt.tight_layout()
plt.show()