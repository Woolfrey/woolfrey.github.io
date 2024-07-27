---
layout: post
title: "How to Solve Every Control Problem: Nonlinear Systems"
date: 2024-07-26
categories: blog control
---

<a name="top"></a>

### Contents:

# Inspiration in Nature

# The Nonlinear Control Problem

$$
\mathrm{V}(\boldsymbol{\epsilon})
\begin{cases}
  \> 0 & \forall \boldsymbol{\epsilon} \ne \mathbf{0} \\
  = 0 & \text{for } \boldsymbol{\epsilon} = \mathbf{0}.
\end{cases}
$$

$$
\mathrm{V}(\boldsymbol{\epsilon},\dot{\boldsymbol{\epsilon}}) \le \mathrm{0} ~ \forall\boldsymbol{\epsilon,\dot{\epsilon}}.
$$

$$
\begin{align}
        \boldsymbol{\epsilon} &= \mathbf{x_\mathrm{d} - x} \\
  \boldsymbol{\dot{\epsilon}} &= \mathbf{\dot{x}_\mathrm{d} - \dot{x}}.
\end{align}
$$

$$
  \mathrm{V} = \frac{1}{2}\boldsymbol{\epsilon}^\mathrm{T}\boldsymbol{\epsilon} = \sum_\mathrm{i=1}^\mathrm{m} \epsilon_\mathrm{i}^2 \ge 0 ~ \forall \boldsymbol{\epsilon}
$$

$$
  \dot{\mathrm{V}} = \boldsymbol{\epsilon}^\mathrm{T}\dot{\boldsymbol{\epsilon}} = \boldsymbol{\epsilon}\left(\mathbf{\dot{x}_\mathrm{d} - \dot{x}}\right).
$$

If we can force:

$$
  \dot{\mathrm{V}} = -\boldsymbol{\epsilon}^\mathrm{T}\mathbf{K}\boldsymbol{\epsilon} \le 0 ~ \forall \boldsymbol{\epsilon}
$$

then the error will decay to zero over time.

A simple choice is:

$$
\mathbf{\dot{x}} = \mathbf{\dot{x}}_\mathrm{d} + \mathbf{K}\boldsymbol{\epsilon}.
$$

# Examples

## Mobile Robot Control

## Quaternion Feedback

# Conclusion:

#### Footnotes:
