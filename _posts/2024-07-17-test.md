---
layout: post
title:  "How to Solve Every Control Problem: Linear Systems"
date:   2024-07-17 12:00:00 +0000
categories: jekyll update
tags:
- control
---

```math
\mathrm{\dot{x} = \frac{dx}{dt} = a\cdot x(t)}
```

```math
\mathrm{x(t) = e^{a\cdot t}\cdot x_0 ~\Longrightarrow~ \dot{x}(t) = a\cdot\underbrace{e^{a\cdot t}\cdot x_0}_{\mathrm{x(t)}}}
```

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
