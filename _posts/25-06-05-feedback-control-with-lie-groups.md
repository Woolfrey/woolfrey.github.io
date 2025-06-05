---
layout: post
title: "Feedback Control With Lie Groups"
date: 2025-06-05
categories: [feedback, control, robot, lie group]
---

> In this post I extend the concept of linear feedback control for scalars and vectors in to the realm of Lie groups. Lie groups are mathematical objects with generalised properties for combining, inverting, and computing "differences". They are used to represent orientation in 3D space in robotics and animation. By understanding their properties we can apply the same logic as linear systems and solve more sophisticated, nonlinear control problems.

### 🧭 Navigation
- [Linear Feedback Control](#linear-feedback-control)
- [Lie Groups](#lie-groups)
- [Orientation Control with Rotation Matrices](#orientation-control-with-rotation-matrices)

## Linear Feedback Control

In a [previous post](25-06-04-feedback-with-lie-groups.md) I discussed the problem of solving feedback control for a linear system using a 3-step process. Given the current position $\mathbf{x}\in\mathbb{R}^m$ and the desired position $\mathbf{x}_d\in\mathbb{R}^{m}$, we:

1. Denote the error from the desired position:

$$
    \boldsymbol{\epsilon} = \mathbf{x}_d - \mathbf{x}. \tag{1}
$$

2. Evaluate the time derivative:

$$
    \dot{\boldsymbol{\epsilon}} = \dot{\mathbf{x}}_d - \dot{\mathbf{x}} \tag{2}
$$

3. Solve the input to force an exponential decay for the error:

$$
    \dot{\mathbf{x}} = \dot{\mathbf{x}}_d + \mathbf{K}\boldsymbol{\epsilon} ~\Longrightarrow~ \dot{\boldsymbol{\epsilon}} = -\mathbf{K}\boldsymbol{\epsilon} ~\Longrightarrow~ \boldsymbol{\epsilon}(t) = e^{-\mathbf{K}t}\boldsymbol{\epsilon}_0. \tag{3}
$$

where $\mathbf{K}\in\mathbb{R}^{n\times n}$ is a positive definite matrix, such that $-\mathbf{K}$ has negative eigenvalues.

How do we perform feedback control for other types of mathematical structures?

For example, it is common to represent the orientation of a rigid body using a rotation matrix:

$$
\mathbf{R} =
\begin{bmatrix}
	r_{11} & r_{12} & r_{13} \\
	r_{21} & r_{22} & r_{23} \\
	r_{31} & r_{32} & r_{33}
\end{bmatrix}
\in\mathbb{R}^{3\times 3}. \tag{4}
$$

Each of the columns are unit norm:

$$
r_{1i}^2 + r_{2i}^2 + r_{3i}^2 = 1 \quad \text{for } i \in\{1,2,3\} \tag{5}
$$

and are orthogonal:

$$
r_{1i}r_{1j} + r_{2i}r_{2j} + r_{3i}r_{3j} = 0 \quad \quad \text{for } i, j \in\{1,2,3\} \text{ and } i \ne j \tag{6}
$$

So we **cannot** add or subtract these matrices $\mathbf{R}_d - \mathbf{R}$ without violating these properties.

## Lie Groups

Lie groups are mathematical structures that satisfy 4 properties:
1. Closure: combining 2 objects in the group remains in the group,
2. Associativity: the order in which we cluster operations doesn't matter, as long as the sequence remains the same,
3. Identity: The element in the group that results in no change, and
4. Inverse: The element that leads to the identity.

Vectors (over addition) form a Lie group.

|     | Vectors (Over Addition) |
| --: | :---------------------: |
| **Closure:** | $\mathbf{x}_1,\mathbf{x}_2\in\mathbb{R}^n$ : $\mathbf{x}_1 + \mathbf{x}_2 \in\mathbb{R}^n$ |
| **Associativity:** | $\mathbf{x}_1 + \left(\mathbf{x}_2 + \mathbf{x}_3 \right) = \left(\mathbf{x}_1 + \mathbf{x}_2 \right) + \mathbf{x}_3$ |
| **Identity:** | $\mathbf{0} \in\mathbb{R}^n : \mathbf{x} + \mathbf{0} = \mathbf{x}$ |
| **Inverse:** | $-\mathbf{x} : \mathbf{x} + (-\mathbf{x}) = \mathbf{0}$ |

The closure and inverse property were applied to define the position error, Eq. (1). In fact, we can see that when the desired position is equal to the actual position, this leads to the identity:

$$
	\mathbf{x}_d = \mathbf{x} ~\Longrightarrow~ \mathbf{x}_d - \mathbf{x} = \mathbf{0}. \tag{7}
$$

## Orientation Control with Rotation Matrices

The rotation matrix, Eq. (4), actually belongs to the Special Orthogonal $\mathbb{SO}$ group:

$$
\mathbf{R}\in\mathbb{SO}(n) \triangleq \big\{\mathbf{R}\in\mathbb{R}^{n\times n} : \mathbf{RR}^T = \mathbf{I},~\det(\mathbf{R}) = 1 \big\}. \tag{8}
$$

Importantly, the closure property is defined by matrix multiplication, and inverse by its transpose.

|     | Special Orthogonal Group  |
| --: | :-----------------------: |
| **Closure:** | $\mathbf{R}_1,\mathbf{R}_2\in\mathbb{SO}(n)$ : $\mathbf{R}_1\mathbf{R}_2\in\mathbb{SO}(n)$ |
| **Associativity:** | $\mathbf{R}_1 \left(\mathbf{R}_2 \mathbf{R}_3 \right) = \left(\mathbf{R}_1 \mathbf{R}_2 \right) \mathbf{R}_3$ |
| **Identity:** | $\mathbf{I} \in\mathbb{SO}(n)\subset\mathbb{R}^{n\times n} : \mathbf{R}\mathbf{I} = \mathbf{R}$ |
| **Inverse:** | $\mathbf{R}^T : \mathbf{RR}^T = \mathbf{I}$ |

As with Eq. (1), we first apply the closure and inverse properties of $\mathbb{SO}(n)$ to define the rotation error as:

$$
    \mathbf{E} = \mathbf{R}_d\mathbf{R}^T. \tag{9}
$$

The $\mathbb{SO}$ group can actually be written as a matrix exponential, so we can instead write Eq. (9) as:

$$
    \mathbf{E} = e^{S(\boldsymbol{\epsilon})} \tag{10}
$$

where:

- $\theta = \|\boldsymbol{\epsilon}\| \in [0, 2\pi]$ is the magnitude of the rotation error (rad), and
- $\hat{\boldsymbol{\epsilon}} = \frac{\boldsymbol{\epsilon}}{\|\boldsymbol{\epsilon}\|} \in\mathbb{R}^3$ is the axis to rotate about,

and

$$
    S(\boldsymbol{\epsilon}) =
    \begin{bmatrix}
                 \phantom{-}0 &           -\epsilon_z & \phantom{-}\epsilon_y \\
        \phantom{-}\epsilon_z &          \phantom{-}0 &           -\epsilon_x \\
                  -\epsilon_y & \phantom{-}\epsilon_x &          \phantom{-}0 
    \end{bmatrix}  \in\mathfrak{so}(3) \tag{11}
$$

is the Lie algebra of $\mathbb{SO}(3)$ (a skew-symmetric matrix).

Second, we evaluate the time derivative which, from Eq. (10), becomes:

$$
    S(\dot{\boldsymbol{\epsilon}})\mathbf{E}, \quad \dot{\boldsymbol{\epsilon}} = \boldsymbol{\omega}_d - \boldsymbol{\omega}. \tag{12}
$$

The time derivative of the Lie algebra is actually the difference between the desired velocity $\boldsymbol{\omega}_d\in\mathbb{R}^3$ (rad/s), and the actual velocity $\boldsymbol{\omega}\in\mathbb{R}^3$ (rad/s).

Now instead of operating over $\mathbb{SO}(3)$ or $\mathfrak{so}(3)$, we can apply what we already know about $\mathbb{R}^n$. If we define the input angular velocity as:

$$
    \boldsymbol{\omega} \triangleq \boldsymbol{\omega}_d + \mathbf{K}\boldsymbol{\epsilon} \tag{13}
$$

for a matrix $\mathbf{K}\in\mathbb{R}^{3\times 3}$, then the error derivative becomes:

$$
    \dot{\boldsymbol{\epsilon}} = -\mathbf{K}\boldsymbol{\epsilon} ~\Longrightarrow~ \boldsymbol{\epsilon} = e^{-\mathbf{K}t}\boldsymbol{\epsilon}_0. \tag{14}
$$

Likewise, the rotation error will decay to the identity:
$$
\lim_{t\to\infty} \mathbf{E} = e^{-S\left(\mathbf{K}\boldsymbol{\epsilon}\right)t} = \mathbf{I}.
$$

Below is a simulation of the [ergoCub](https://ergocub.eu) where I used this principle to enable it to rotate an object when grasping with 2 hands.

<p align="center">
    <img src="/assets/images/projects/ergocub_bimanual_sim_rotating.gif" width="300" height="auto" loading=lazy />
    <br>
    <em> We can use the underlying Lie algebra of the rotation matrix to control the orientation of a robot's hands. </em>
</p>