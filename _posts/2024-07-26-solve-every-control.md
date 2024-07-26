---
layout: post
title: "How to Solve Every Control Problem: Linear Systems"
date: 2024-07-26
categories: blog control
---

<a name="top"></a>

### Contents:

- [Inspiration in Nature](#inspiration-in-nature)
- [The Linear Control Problem](#the-linear-control-problem)
- [Examples](#examples)
   - [A Generic Control System](#a-generic-control-system)
   - [Torque Control of a Robot Arm](#torque-control-of-a-robot-arm)
   - [Velocity Control of an End-Effector](#velocity-control-of-an-end-effector)
- [Conclusion](#conclusion)
- [Comments](#comments)

# Inspiration in Nature

We can observe many natural phenomena that exhibit exponential decay:
- The voltage across an RC[^1] circuit in your phone or computer,
- The bouncing of your car suspension as it goes over a speed hump, and
- The temperature of a hot cup of coffee,

<p align="center">
   <img src="https://github.com/user-attachments/assets/2992f0f6-143d-40c7-ad64-1bafbbf11163" width="700" height="auto" />
</p>

The fundamental property of these systems is that the rate of change is proportional to its position $\mathrm{x}$ at any given time $\mathrm{t}$:

$$
\mathrm{\dot{x} = \frac{dx}{dt} = -a\cdot x(t)}
$$

where $\mathrm{a}\in\mathbb{R}^+$ is a constant related to an intrinsic physical property.

The solution for the position as a function of time is an exponential equation:

$$
\mathrm{x(t) = e^{-a\cdot t}\cdot x_0 ~\Longrightarrow~ \dot{x}(t) = -a\cdot\underbrace{e^{-a\cdot t}\cdot x_0}_{\mathrm{x(t)}}}
$$

And, most importantly, as time goes to infinity, its value decays asymptotically to zero:

$$
\lim_{\mathrm{t}\to\infty} ~ \mathrm{x(t)} = 0.
$$

The fact that this phenomena is ubiquitous in nature hints at something deeper about how our physical world operates. Moreover, we can use this as inspiration for designing control equations. After all, the systems we are controlling are bounded by the laws of physics. By imitating these laws in control we obtain solutions that are elegant, clear, understandable, and predictable.

[^1]: Resistor-Capacitor.

[⬆️ Back to top.](#top)

# The Linear Control Problem

Formulating and solving a linear control problem can be achieved in 3 steps:
1. Define your position and/or state error,
2. Evaluate its time derivative, and
3. Denote the control input such that the error decays exponentially.

Assume we have some m-dimensional system:

$$
\mathbf{x} =
\begin{bmatrix}
    \mathrm{x}_1 \\
    \vdots \\
    \mathrm{x_n}
\end{bmatrix}
\in\mathbb{R}^\mathrm{m}.
$$

We can denote its error from some _desired_ value $\mathbf{x_d}$ as:

$$
\boldsymbol{\epsilon} = \mathbf{x_\mathrm{d} - x}
$$

and its time derivative is simply:

$$
\dot{\boldsymbol{\epsilon}} = \mathbf{\dot{x}_\mathrm{d} - \dot{x}}.
$$

Now we want the error velocity to be (negatively) proportional to its current state, such that it decays asymptotically to zero:

$$
\dot{\boldsymbol{\epsilon}} = -\mathbf{K}\boldsymbol{\epsilon} \quad \Longrightarrow \quad \boldsymbol{\epsilon}(\mathrm{t}) = \mathrm{e}^{-\mathbf{K}\mathrm{t}}\cdot\boldsymbol{\epsilon}_0 \quad \Longrightarrow \quad \lim_{\mathrm{t}\to \infty} ~ \boldsymbol{\epsilon}(\mathrm{t}) = \mathbf{0}.
$$

where $\mathbf{K}\in\mathbb{R}^\mathrm{m\times m}$ is a gain matrix. As long as $\mathbf{K}$ has _positive_ eigenvalues (such that $-\mathbf{K}$ has negative eigenvalues), the error will reduce to zero[^2].

By equating $\dot{\boldsymbol{\epsilon}}$ and re-arranging we obtain:

$$
\begin{align}
    \mathbf{\dot{x}_\mathrm{d} - \dot{x}} &= -\mathbf{K}\boldsymbol{\epsilon} \\
                     \mathbf{\dot{x}} &= \mathbf{\dot{x}}_\mathrm{d} + \mathbf{K}\boldsymbol{\epsilon}
\end{align}
$$

We can see that imposed velocity $\mathbf{\dot{x}}$ consists of 2 terms:
1. A feedforward velocity $\mathbf{x}_\mathrm{d}$, and
2. A feedback term $\mathbf{K}\left(\mathbf{x_\mathrm{d} - x}\right)$.

In most applications, the velocity $\mathbf{\dot{x}}$ is usually a more complicated function of some other coordinate system, and a control input. But the principle remains the same.

[^2]: The reason for this is too complicated for this post. But a simple solution is a diagonal matrix with positive elements.

[⬆️ Back to top.](#top)

# Examples

## A Generic Control System

A common starting point in control theory is with a simple, "control affine" system[^3] of the form:

$$
\mathbf{\dot{x} = Ax + Bu}
$$

where:
- $\mathbf{A}\in\mathbb{R}^\mathrm{m\times m}$ is the "state transition" matrix,
- $\mathbf{B}\in\mathbb{R}^\mathrm{m\times n}$ is the "control matrix", and
- $\mathbf{u}\in\mathbb{R}^\mathrm{n}$ is the control input.

Following the process above, we 1st define the error, and 2nd evaluate its time derivative:

$$
\begin{align}
      \boldsymbol{\epsilon} &= \mathbf{x_\mathrm{d} - x} \\
\dot{\boldsymbol{\epsilon}} &= \mathbf{\dot{x}_\mathrm{d} - \dot{x}} \\
                            &= \mathbf{\dot{x}_\mathrm{d} - Ax - Bu}.
\end{align}
$$

And 3rd, we need to assign the control input $\mathbf{u}$ to force the error $\boldsymbol{\epsilon}$ to decay exponentially. Equating $\dot{\boldsymbol{\epsilon}}$, re-arranging for $\mathbf{u}$, and solving we obtain:

$$
\begin{align}
    \mathbf{\dot{x}_\mathrm{d} - Ax - Bu} &= -\mathbf{K}\boldsymbol{\epsilon} \\
                          \mathbf{Bu} &= \mathbf{\dot{x}}_\mathrm{d} + \mathbf{K}\boldsymbol{\epsilon} - \mathbf{Ax} \\
                           \mathbf{u} &= \mathbf{B}^\dagger \left(\mathbf{\dot{x}}_\mathrm{d} + \mathbf{K}\boldsymbol{\epsilon} - \mathbf{Ax}\right)
\end{align}
$$

where:

$$
\mathbf{B}^\dagger =
\begin{cases}
    \left(\mathbf{B^\mathrm{T}B}\right)^{-1}\mathbf{B}^\mathrm{T} & \text{for } \mathrm{m > n} \\
                          \mathbf{B}^{-1} & \text{for } \mathrm{m = n} \\
    \mathbf{B}^\mathrm{T}\left(\mathbf{BB^\mathrm{T}}\right)^{-1} & \text{for } \mathrm{m < n}.
\end{cases}
$$

The solution has 3 components:
1. A feedforward term defined by the rate of change in the target point $\mathbf{\dot{x}}_\mathrm{d}$,
2. A feedback gain on the target error $\mathbf{K}\boldsymbol{\epsilon}$, and
3. Subtracting the natural system dynamics contributing to our desired motion $-\mathbf{Ax}$.

Many control courses begin with the conclusion:

$$
\mathbf{u = -Kx} ~\Longrightarrow ~\mathbf{\dot{x}} = \left(\mathbf{A - BK}\right)\mathbf{x}
$$

but this presumes that:
1. $\mathbf{x}_\mathrm{d} = \mathbf{0}$, instead of $\boldsymbol{\epsilon}\to\mathbf{0}$ over time, and
2. $\mathbf{\dot{x}}_\mathrm{d} = \mathbf{0}$, meaning the desired position never changes.

There are many applications in real life where we want to follow a moving target or trajectory. By following the 3-step process above, the concept of a feedforward/feedback control naturally appears.

[^3]: I've never actually encountered a system like this in reality 🤷‍♂️

[⬆️ Back to top.](#top)

## Torque Control of a Robot Arm

A common task for robot control is joint trajectory tracking for pick-and-place tasks. In short, we have some trajectory that defines the desired joint positions $\mathbf{q}_\mathrm{d}(\mathrm{t})$ that transition the robot from one configuration to another. We need to design the motor torque inputs $\boldsymbol{\tau}\in\mathbb{R}^\mathrm{n}$ to make the robot track this trajectory.

<p align="center">
   <img src="https://github.com/user-attachments/assets/1c52f165-225b-4a4b-834b-d74060289e82" width="300" height="auto"/>
</p>

The inverse dynamics of a robot arm is given by:

$$
\boldsymbol{\tau} = \mathbf{M(q)\ddot{q} + n(q,\dot{q})}
$$

where:
- $\mathbf{M(q)}\in\mathbb{R}^\mathrm{n\times n}$ is the joint inertia matrix, and
- $\mathbf{n(q,\dot{q})}\in\mathbb{R}^\mathrm{n}$ is the nonlinear effects of gravity, Coriolis, and centripetal forces.

As before, we 1. define the error from the desired position, and 2. take the time derivative:

$$
\begin{align}
  \boldsymbol{\epsilon}        &= \mathbf{q_\mathrm{d} - q} \\
  \dot{\boldsymbol{\epsilon}}  &= \mathbf{\dot{q}_\mathrm{d} - \dot{q}} \\
  \ddot{\boldsymbol{\epsilon}} &= \mathbf{\ddot{q}_\mathrm{d} - \ddot{q}}.
\end{align}
$$

In this case, we must also evaluate the _second_ time derivative since the inverse dynamics gives is naturally a function of $\mathbf{\ddot{q}}$.

If we choose:

$$
\mathbf{\ddot{q}} = \mathbf{\ddot{q}}_\mathrm{d} + \underbrace{\mathbf{K}_\mathrm{d}\overbrace{\left(\mathbf{\dot{q}_\mathrm{d} - \dot{q}}\right)}^{\dot{\boldsymbol{\epsilon}}}}_{\text{velocity feedback}} + \underbrace{\mathbf{K}_\mathrm{p}\overbrace{\left(\mathbf{q_\mathrm{d} - q}\right)}^{\boldsymbol{\epsilon}}}_{\text{position feedback}}
$$

then the error acceleration becomes:

$$
\ddot{\boldsymbol{\epsilon}} = -\mathbf{K}_\mathrm{d}\dot{\boldsymbol{\epsilon}} - \mathbf{K}_\mathrm{p}\boldsymbol{\epsilon}.
$$

Since this is a second-order system, we can compose an equivalent, first-order "companion system" of the first and second derivatives:

$$
\underbrace{
\begin{bmatrix}
  \dot{\boldsymbol{\epsilon}} \\
  \ddot{\boldsymbol{\epsilon}}
\end{bmatrix}
}_{\dot{\tilde{\boldsymbol{\epsilon}}}}
    =
\underbrace{
\begin{bmatrix}
                       & \mathbf{I} \\
    -\mathbf{K}_\mathrm{p} & -\mathbf{K}_\mathrm{d}
\end{bmatrix}
}_{\tilde{\mathbf{K}}}
\underbrace{
\begin{bmatrix}
  \boldsymbol{\epsilon} \\
  \dot{\boldsymbol{\epsilon}}
\end{bmatrix}
}_{\tilde{\boldsymbol{\epsilon}}}

~ \Longrightarrow ~ \tilde{\boldsymbol{\epsilon}} = \mathrm{e}^{-\tilde{\mathbf{K}}\mathrm{t}}\cdot\tilde{\boldsymbol{\epsilon}}_0
$$

If the composite matrix has negative eigenvalues, then the errors will exponentially decay.

Substituting this back in to the inverse dynamics the control torque becomes:

$$
\boldsymbol{\tau} =
\mathbf{M}\left(\mathbf{\ddot{q}}_\mathrm{d} + \mathbf{K}_\mathrm{d}\dot{\boldsymbol{\epsilon}} + \mathbf{K}_\mathrm{p}\boldsymbol{\epsilon}\right) + \mathbf{n}.
$$

[⬆️ Back to top.](#top)

## Velocity Control of an End-Effector

In other applications of robotics, we want to control the tip of the arm directly, at all times. For example, we may want to track a straight line in a welding, or spray painting task, or provide a more intuitive control input for human users [^4]

<p align="center">
   <img src="https://github.com/user-attachments/assets/3f6544dc-a726-45c0-bfa7-6c6cf46fc85a" width="300" height="auto" />
</p>

The position of the endpoint of a robot arm $\mathbf{x}\in\mathbb{R}^\mathrm{m}$ is a function of the joint angles $\mathbf{q}\in\mathbb{R}^\mathrm{n}$:

$$
\mathbf{x = f(q)}
$$

This is known as the forward kinematics. Normally the kinematics involves many complicated, trigonometric functions. However, the _instantaneous_ velocity is linear which we can readily solve.

As before, we can define the error from the desired position and evaluate the time derivative using the chain rule:

$$
\begin{align}
    \boldsymbol{\epsilon}       &= \mathbf{x_\mathrm{d} - f(q)} \\
    \boldsymbol{\dot{\epsilon}} &= \mathbf{\dot{x}_\mathrm{d} - J(q)\dot{q}}
\end{align}
$$

where:

$$
\mathbf{J(q)} = \frac{\partial\mathbf{f}}{\partial\mathbf{q}} \in\mathbb{R}^\mathrm{m\times n}
$$

is the Jacobian matrix[^5].

Again, we equate the error derivative $\dot{\boldsymbol{\epsilon}}$ so that it is proportional to itself, then rearrange:

$$
\begin{align}
    \overbrace{\mathbf{\dot{x}_\mathrm{d} - J\dot{q}}}^{\dot{\boldsymbol{\epsilon}}} &= -\mathbf{K}\boldsymbol{\epsilon} \\
                     \mathbf{J\dot{q}} &= \mathbf{\dot{x}}_\mathrm{d} + \mathbf{K}\boldsymbol{\epsilon} \\
                      \mathbf{\dot{q}} &= \mathbf{J}^\dagger\left(\mathbf{\dot{x}}_\mathrm{d} + \mathbf{K}\boldsymbol{\epsilon}\right)
\end{align}
$$

where:

$$
\mathbf{J}^\dagger =
\begin{cases}
\left(\mathbf{J^\mathrm{T}J}\right)^{-1}\mathbf{J}^\mathrm{T} & \text{for } \mathrm{m > n} \\
\mathbf{J}^{-1} & \text{for } \mathrm{m = n} \\
\mathbf{J}^\mathrm{T}\left(\mathbf{JJ^\mathrm{T}}\right)^{-1} & \text{for } \mathrm{m < n}.
\end{cases}
$$

As before, we have a feedforward + feedback term in the "task space" of the robot, which is converted to the joint space by the (pseudo)inverse Jacobian $\mathbf{J}^\dagger$.

In practice, orientation feedback for the endpoint of a robot arm requires more complicated, non-linear feedback. But the high-level principle is the same.

We could also extend the problem to the acceleration level:

$$
\mathbf{\ddot{x} = J(q)\ddot{q} + J(q,\dot{q})\dot{q}}
$$

but this is better resolved as a _dynamic_ problem, rather than a kinematic one (another time).

[^4]: Whitney, D. E. (1969). Resolved motion rate control of manipulators and human prostheses. IEEE Transactions on man-machine systems, 10(2), 47-53.

[^5]: Whitney, D. E. (1972). The mathematics of coordinated control of prosthetic arms and manipulators.

# Conclusion

Many theoretical control courses, and research articles on control, begin with the conclusion. That is, by stating some sort of control law $\mathbf{u}(\mathbf{x,\dot{x}},\mathrm{t})$ and then inviting the student/reader to see how it leads to stability of a control problem.

Instead, it is more intuitive, and straightforward to:
1. Start by expressing the control problem in terms of _error_ from desired position,
2. Seeing how this error evolves over time, and
3. Choosing the control input so that the error decays.

Importantly, step 3 follows that same equations of motion that we can observe in many natural, physical phenomena in our daily lives. This leads to control equations that are easy to interpret.

Moreover, this simple process allows us to solve a variety of control problems - including trajectory tracking, or following moving targets.

Next time we will see how to apply the same principle to nonlinear systems.

[⬆️ Back to top.](#top)

#### Footnotes:
