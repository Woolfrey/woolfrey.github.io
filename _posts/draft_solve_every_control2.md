---
layout: post
title: "How to Solve Every Control Problem: Nonlinear Systems"
date: 2024-07-26
categories: blog control
---

<a name="top"></a>

### Contents:

# Inspiration in Nature

I started the [previous post](https://woolfrey.github.io/blog/control/2024/07/26/solve-every-control/) on linear systems by looking at the dynamics of natural phenomena for inspiration in designing control equations. The same can be applied here.

A simple example might be to consider the dynamics of a mass-spring-damper system, which you will find in the suspension system of a car, aeroplane, or train. We can use Newtonian mechanics to model it as a second-order differential:

$$
\begin{align}
  \mathrm{m\ddot{x}} &= \mathrm{-kx - d\dot{x}} \\
   \mathrm{\ddot{x}} &= \mathrm{-m^{-1}\left(kx + d\dot{x}\right)}.
\end{align}
$$

To determine its stability we can form a 1st order companion system:

$$
\begin{bmatrix}
  \mathrm{\dot{x}} \\
  \mathrm{\ddot{x}}
\end{bmatrix} =
\begin{bmatrix}
  0 & 1 \\
  -\mathrm{m^{-1}k} & -\mathrm{m^{-1}d}
\end{bmatrix}
\begin{bmatrix}
  \mathrm{x} \\
  \mathrm{\dot{x}}
\end{bmatrix}
$$

and analyse the eigenvalues of the matrix.

But, instead of thinking about forces, we can also think about the energy in the system:

$$
\mathrm{E} = \underbrace{\mathrm{\frac{1}{2}m\dot{x}^2}}_{\text{kinetic}} + \underbrace{\mathrm{\frac{1}{2}kx^2}}_{\text{potential}}.
$$

If we take the time derivative we can see that the energy is monotonically decreasing[^1]:

[^1]: Meaning that it may temporarily remain constant, but can never increase over time.

$$
\begin{align}
  \mathrm{\dot{E}} &= \mathrm{m\dot{x}\ddot{x} + kx\dot{x}} \\
                   &= \mathrm{-kx\dot{x} - d\dot{x}^2 + kx\dot{x}} \\
                   &= -\mathrm{d\dot{x}^2} \\
                   &\le 0
\end{align}
$$

There are 3 important insights here. Energy is:
1. A scalar quantity,
2. Always greater than, or equal to, 0,
3. Decreasing with time (when not acted on by an external force).

Often it is easier to analyse the energy in a nonlinear system to prove its stability. Moreover, we can use energy-inspired methods to design and solve control problems.

# The Nonlinear Control Problem

To solve a control problem, we need only follow 3 simple steps:
1. Define our position/state error,
2. Evaluate the time derivative of said error, and
3. Design the control input such that error is decreasing with time.

But, based on our energy analogy, there are some conditions we must abide by. The error quantity must be:
1. A scalar value,
2. Greater than zero when the error is non-zero,
3. Equal to zero when the error is zero.

Canonically we use the letter $\mathrm{V}$ for this function:

$$
\mathrm{V}(\boldsymbol{\epsilon})
\begin{cases}
  \> 0 & \forall \boldsymbol{\epsilon} \ne \mathbf{0} \\
  = 0 & \text{for } \boldsymbol{\epsilon} = \mathbf{0}.
\end{cases}
$$

Then our control problem is to design the input that forces its time derivative to be negative (or at least monotonically decreasing):

$$
\mathrm{\dot{V}}(\boldsymbol{\epsilon},\dot{\boldsymbol{\epsilon}}) \le \mathrm{0} ~ \forall\boldsymbol{\epsilon,\dot{\epsilon}}.
$$

Let's consider a simple system whose position is denoted by $\mathbf{x}\in\mathbb{R}^\mathrm{m}$. We define the error as its difference from some desired position $\mathbf{x}_\mathrm{d}$. We can also evaluate the time derivative:
$$
\begin{align}
        \boldsymbol{\epsilon} &= \mathbf{x_\mathrm{d} - x} \\
  \boldsymbol{\dot{\epsilon}} &= \mathbf{\dot{x}_\mathrm{d} - \dot{x}}.
\end{align}
$$

For the _nonlinear_ control problem we need to convert the error to a scalar. A simple solution is to use the sum-of-squares:

$$
  \mathrm{V} = \frac{1}{2}\boldsymbol{\epsilon}^\mathrm{T}\boldsymbol{\epsilon} = \sum_\mathrm{i=1}^\mathrm{m} \epsilon_\mathrm{i}^2 \ge 0 ~ \forall \boldsymbol{\epsilon}
$$

We can see that this is analogous to energy in the [previous section](#inspiration-in-nature).

Taking the time derivative and expanding we obtain:

$$
  \dot{\mathrm{V}} = \boldsymbol{\epsilon}^\mathrm{T}\dot{\boldsymbol{\epsilon}} = \boldsymbol{\epsilon}\left(\mathbf{\dot{x}_\mathrm{d} - \dot{x}}\right).
$$

If we can force the time derivative to be of this form:

$$
  \dot{\mathrm{V}} = -\boldsymbol{\epsilon}^\mathrm{T}\mathbf{K}\boldsymbol{\epsilon} \le 0 ~ \forall \boldsymbol{\epsilon}
$$

where $\mathbf{K}\in\mathbb{R}^\mathrm{m\times m}$ is positive definite[^2] then the error will decay to zero over time.

[^2]: Positive definite means $\boldsymbol{\epsilon}^\mathrm{T}\mathbf{K}\boldsymbol{\epsilon} > 0 ~\forall\boldsymbol{\epsilon} \ne \mathbf{0}$. A simple solution is that $\mathbf{K}$ is a diagonal matrix with positive elements.

From inspection, an obvious choice is:

$$
\mathbf{\dot{x}} = \mathbf{\dot{x}}_\mathrm{d} + \mathbf{K}\boldsymbol{\epsilon}.
$$

We arrived at the same conclusion as the [linear problem](https://woolfrey.github.io/blog/control/2024/07/26/solve-every-control/). But in the next section, we will see how this principle can be used to solve more complicated problems.

# Examples

## Mobile Robot Control

## Quaternion Feedback

# Conclusion:

#### Footnotes:
