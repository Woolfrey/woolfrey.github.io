---
layout: post
title: "Lagrangian Mechanics"
date: yy-mm-dd
categories: [keywords]
---

Newton's law: force = time derivative of momentum:
$$
    \mathbf{f} = \frac{\mathrm{d}}{\mathrm{dt}}\left(\boldsymbol{\Lambda}\dot{\mathbf{x}}\right)
$$

d'Alembert's principle: constraint forces disappear under projection of admissible displacements $\delta\mathbf{x}$:
$$
\sum_\mathrm{i=1}^\mathrm{n}\delta\mathbf{x}_\mathrm{i}^\mathrm{T} \left( \mathbf{f}\mathrm{_i^{app.}} + \mathbf{f}\mathrm{_i^{grav.}} - \frac{\mathrm{d}}{\mathrm{dt}}\left(\boldsymbol{\Lambda}_\mathrm{i}\dot{\mathbf{x}}_\mathrm{i}\right)\right) = 0
$$

Using generalised coordinates $\mathbf{q}\in\mathbb{R}^\mathrm{n}$:
$$
    \delta\mathbf{x}_\mathrm{i} = \frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}}\delta\mathbf{q}
$$
Then:
$$
    \delta\mathbf{q}^\mathrm{T}\sum_\mathrm{i=1}^\mathrm{n} \frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}}^\mathrm{T} \left(\mathbf{f}\mathrm{_i^{app.}} + \mathbf{f}\mathrm{_i^{grav.}} - \frac{\mathrm{d}}{\mathrm{dt}}\left(\boldsymbol{\Lambda}_\mathrm{i}\frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}}\dot{\mathbf{q}}\right) \right) = 0
$$
Rearranging:
$$
\begin{align}
    \overbrace{\sum_\mathrm{i=1}^\mathrm{n}\frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}}^\mathrm{T}\mathbf{f}\mathrm{_i^{app.}}}^{\boldsymbol{\tau}} &= \sum_\mathrm{i=1}^\mathrm{n} \frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}}^\mathrm{T}\left(\frac{\mathrm{d}}{\mathrm{dt}}\left(\boldsymbol{\Lambda}_\mathrm{i}\frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}}\dot{\mathbf{q}}\right) - \mathbf{f}\mathrm{_i^{grav.}}\right)\\
    &= \underbrace{\left(\sum_\mathrm{i=1}^\mathrm{n}\frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}}^\mathrm{T}\boldsymbol{\Lambda}_\mathrm{i}\frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}}\right)}_{\mathbf{M}(\mathbf{q})}\ddot{\mathbf{q}} + \underbrace{\left(\sum_\mathrm{i=1}^\mathrm{n}\frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}}^\mathrm{T}\left(\dot{\mathbf{\boldsymbol{\Lambda}}}_\mathrm{i}\frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}} + \boldsymbol{\Lambda}_\mathrm{i}\frac{\mathrm{d}}{\mathrm{dt}}\left(\frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}}\right)\right)\right)}_{\mathbf{C}(\mathbf{q},\dot{\mathbf{q}})}\dot{\mathbf{q}} - \underbrace{\sum_\mathrm{i=1}^\mathrm{n}\frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}}^\mathrm{T}\mathbf{f}\mathrm{_i^{grav.}}}_{\mathbf{g}(\mathbf{q})}
\end{align}
$$

Kinetic energy:
$$
    \mathcal{K}(\mathbf{q},\dot{\mathbf{q}}) = \tfrac{1}{2}\dot{\mathbf{q}}^\mathrm{T}\mathbf{M}(\mathbf{q})\dot{\mathbf{q}} = \tfrac{1}{2}\dot{\mathbf{q}}^\mathrm{T}\left(\sum_\mathrm{i=1}^\mathrm{n}\frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}}^\mathrm{T}\boldsymbol{\Lambda}_\mathrm{i}\frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}}\right)\dot{\mathbf{q}}
$$

If we re-order the chain rule:
$$
\begin{align}
    \sum_\mathrm{i=1}^\mathrm{n}\frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}}^\mathrm{T}\frac{\mathrm{d}}{\mathrm{dt}}\left(\boldsymbol{\Lambda}_\mathrm{i}\frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}}\dot{\mathbf{q}}\right) &= \sum_\mathrm{i=1}^\mathrm{n}\frac{\mathrm{d}}{\mathrm{dt}}\left(\frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}}^\mathrm{T}\boldsymbol{\Lambda}_\mathrm{i}\frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}}\right)-\frac{\mathrm{d}}{\mathrm{dt}}\left(\frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}}\right)^\mathrm{T}\boldsymbol{\Lambda}_\mathrm{i}\frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}}\dot{\mathbf{q}} \\
     &= \sum_\mathrm{i=1}^\mathrm{n}\frac{\mathrm{d}}{\mathrm{dt}}\underbrace{\left(\frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}}^\mathrm{T}\boldsymbol{\Lambda}_\mathrm{i}\frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}}\right)}_{\partial\mathcal{K}/\partial\dot{\mathbf{q}}} - \underbrace{\dot{\mathbf{q}}^\mathrm{T}\frac{\partial^2\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}^2}^\mathrm{T}
     \boldsymbol{\Lambda}_\mathrm{i}\frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}}\dot{\mathbf{q}}}_{\partial\mathcal{K}/\partial\mathbf{q}}
\end{align}
$$

Work done against gravity is opposite the force:
$$
    \delta\mathcal{W} = -\sum_\mathrm{i=1}^\mathrm{n}\delta\mathbf{x}\mathrm{_i^T}\mathbf{f}\mathrm{_i^{grav.}} = -\delta\mathbf{q}^\mathrm{T}\underbrace{\sum_\mathrm{i=1}^\mathrm{n}\frac{\partial\mathbf{x}_\mathrm{i}}{\partial\mathbf{q}}^\mathrm{T}\mathbf{f}\mathrm{_i^{grav.}}}_{-\partial\mathcal{P}/{\partial\mathbf{q}}}
$$

So we may write:

$$
\boldsymbol{\tau} = \frac{\mathrm{d}}{\mathrm{dt}}\left(\frac{\partial\mathcal{K}}{\partial\dot{\mathbf{q}}}\right) - \frac{\partial\mathcal{K}}{\partial\mathbf{q}} + \frac{\partial\mathcal{P}}{\partial\mathbf{q}}
$$

If we define:
$$
    \mathcal{L}(\mathbf{q},\dot{\mathbf{q}}) \triangleq \mathcal{K}(\mathbf{q},\dot{\mathbf{q}}) - \mathcal{P}(\mathbf{q})
$$

Then:
$$
\boldsymbol{\tau} = \frac{\mathrm{d}}{\mathrm{dt}}\left(\frac{\partial\mathcal{L}}{\partial\dot{\mathbf{q}}}\right) - \frac{\partial\mathcal{L}}{\partial\mathbf{q}}
$$