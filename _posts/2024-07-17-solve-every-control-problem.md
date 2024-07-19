---
layout: post
title:  "How to Solve Every Control Problem: Linear Systems"
date:   2024-07-17 12:00:00 +0000
categories: jekyll update
tags:
- control
---

# Inspiration in Nature

```math
\mathrm{\dot{x} = \frac{dx}{dt} = a\cdot x(t)}
```

```math
\mathrm{x(t) = e^{a\cdot t}\cdot x_0 ~\Longrightarrow~ \dot{x}(t) = a\cdot\underbrace{e^{a\cdot t}\cdot x_0}_{\mathrm{x(t)}}}
```

# The Linear Control Problem
```math
\boldsymbol{\epsilon} = \mathbf{x_\mathrm{d} - x}
```

```math
\dot{\boldsymbol{\epsilon}} = \mathrm{\dot{x}_\mathrm{d} - \dot{x}}
```

Assign:
```math
\mathbf{\dot{x} = \dot{x}_\mathrm{d}} + \mathbf{K}\underbrace{\left(\mathbf{x_\mathrm{d} - x}\right)}_{\boldsymbol{\epsilon}}
```

```math
\dot{\epsilon} = -\mathbf{K}\boldsymbol{\epsilon} ~\Longrightarrow~ \boldsymbol{\epsilon}(\mathrm{t}) = \mathrm{e}^{-\mathbf{K}\mathrm{t}}\cdot\boldsymbol{\epsilon}_0
```

# Examples

## A Generic Control System

```math
\mathbf{\dot{x} = Ax + Bu}
```

```math
\begin{align}
\boldsymbol{\epsilon} &= \mathbf{x_\mathrm{d} - x} \\
\dot{\boldsymbol{\epsilon}} &= \mathbf{\dot{x}_\mathrm{d} - \dot{x}} \\
&= \mathbf{\dot{x}_\mathrm{d} - Ax - Bu}
\end{align}
```

```math
\begin{align}
\mathbf{\dot{x}_\mathrm{d} - Ax - Bu} &= -\mathbf{K}\boldsymbol{\epsilon} \\
\mathbf{Bu} &= \mathbf{\dot{x}}_\mathrm{d} + \mathbf{K}\boldsymbol{\epsilon} - \mathbf{Ax} \\
\mathbf{u} &= \mathbf{B}^\dagger \left(\mathbf{\dot{x}}_\mathrm{d} + \mathbf{K}\boldsymbol{\epsilon} - \mathbf{Ax}\right)
\end{align}
```

where:
```math
\mathbf{B}^\dagger =
\begin{cases}
\left(\mathbf{B^\mathrm{T}B}\right)^{-1}\mathbf{B}^\mathrm{T} & \text{for } \mathrm{m > n} \\
\mathbf{B}^{-1} & \text{for } \mathrm{m = n} \\
\mathbf{B}^\mathrm{T}\left(\mathbf{BB^\mathrm{T}}\right)^{-1} & \text{for } \mathrm{m < n}.
\end{cases}
```

## Torque Control of a Robot Arm

```math
\boldsymbol{\tau} = \mathbf{M(q)\ddot{q} + n(q,\dot{q})}
```

```math
\begin{align}
  \boldsymbol{\epsilon}        &= \mathbf{q_\mathrm{d} - q} \\
  \dot{\boldsymbol{\epsilon}}  &= \mathbf{\dot{q}_\mathrm{d} - \dot{q}} \\
  \ddot{\boldsymbol{\epsilon}} &= \mathbf{\ddot{q}_\mathrm{d} - \ddot{q}}
\end{align}
```

```math
\mathbf{\ddot{q}} = \mathbf{\ddot{q}}_\mathrm{d} + \underbrace{\mathbf{K}_\mathrm{d}\overbrace{\left(\mathbf{\dot{q}_\mathrm{d} - \dot{q}}\right)}^{\dot{\boldsymbol{\epsilon}}}}_{\text{velocity feedback}} + \underbrace{\mathbf{K}_\mathrm{p}\overbrace{\left(\mathbf{q_\mathrm{d} - q}\right)}^{\boldsymbol{\epsilon}}}_{\text{position feedback}}
```

```math
\ddot{\boldsymbol{\epsilon}} = -\mathbf{K}_\mathrm{d}\dot{\boldsymbol{\epsilon}} - \mathbf{K}_\mathrm{p}\boldsymbol{\epsilon}
```

```math
\begin{bmatrix}
  \dot{\boldsymbol{\epsilon}} \\
  \ddot{\boldsymbol{\epsilon}}
\end{bmatrix}
=
\begin{bmatrix}
  & \mathbf{I} \\
-\mathbf{K}_\mathrm{p} & -\mathbf{K}_\mathrm{d}
\end{bmatrix}
\begin{bmatrix}
  \boldsymbol{\epsilon} \\
  \dot{\boldsymbol{\epsilon}}
\end{bmatrix}
```

```math
\boldsymbol{\tau} =
\mathbf{M}\left(\mathbf{\ddot{q}}_\mathrm{d} + \mathbf{K}_\mathrm{d}\dot{\boldsymbol{\epsilon}} + \mathbf{K}_\mathrm{p}\boldsymbol{\epsilon}\right) + \mathbf{n}
```

## Velocity Control of an End-Effector

```math
\mathbf{x = f(q)}
```

```math
\mathbf{\dot{x} = J(q)\dot{q}}
```
where:
```math
\mathbf{J(q)} = \frac{\partial\mathbf{f}}{\partial\mathbf{q}}
```

```math
\begin{align}
\boldsymbol{\epsilon} &= \mathbf{x_\mathrm{d} - x} \\
\dot{\boldsymbol{\epsilon}} &= \mathbf{\dot{x}_\mathrm{d} - \dot{x}} \\
&= \mathbf{\dot{x}_\mathrm{d} - J\dot{q}}
\end{align}
```

```math
\begin{align}
\mathbf{\dot{x}_\mathrm{d} - J\dot{q}} &= -\mathbf{K}\boldsymbol{\epsilon} \\
\mathbf{J\dot{q}} &= \mathbf{\dot{x}_\mathrm{d} + K}\boldsymbol{\epsilon} \\
\mathbf{\dot{q}} &= \mathbf{J}^\dagger\left(\mathbf{\dot{x}_\mathrm{d} + K}\boldsymbol{\epsilon}\right)
\end{align}
```

```math
\mathbf{J}^\dagger =
\begin{cases}
\left(\mathbf{J^\mathrm{T}J}\right)^{-1}\mathbf{J}^\mathrm{T} & \text{for } \mathrm{m > n} \\
\mathbf{J}^{-1} & \text{for } \mathrm{m = n} \\
\mathbf{J}^\mathrm{T}\left(\mathbf{JJ^\mathrm{T}}\right)^{-1} & \text{for } \mathrm{m < n}.
\end{cases}
```

