
We need an expression in polar coordinates $r(\theta(t))$ to generate a trajectory.

Minimize angular acceleration:
$$
I = \int_{t_0}^{t_f} \tfrac{1}{2}\ddot{\theta}^2 dt
$$
Solution is a cubic polynomial:
$$
\theta(t) = \alpha_0 + \alpha_1 t + \alpha_2 t^2 + \alpha_3 t^3
$$

Infinitesimal arc length:
$$
ds = \sqrt{dx^2 + dy^2} d\theta
$$

$$
\begin{align}
    x  &= r(\theta)\cdot\cos(\theta) \\
    dx &= r'\cdot \cos(\theta) - r\cdot\sin(\theta)
\end{align}
$$

$$
\begin{align}
    y  &= r(\theta)\cdot\sin(\theta) \\
    dy &= r'\cdot\cos(\theta) + r\cdot\sin(\theta)
\end{align}
$$

$$
ds = \sqrt{(r'^2 ) + r^2} d\theta
$$

But this is hard to solve, so consider the square:

$$
\int r'^2 + r^2 d\theta
$$

Solution:
$$
\begin{align}
 r'' = r \\
 r(\theta) = c_1 e^{\theta} + c_2 e^{-\theta}
 \end{align}
 $$

 $$
 r(0) = c_1 + c_2 = 0 \therefore c_2 = -c_1
 $$

 $$
 r'(0) = c_1 - c_2 = -2c_1
 $$

 $$
 v(t) = \frac{ds}{dt} = \frac{ds}{d\theta}\cdot\dot{\theta}
 $$


$$
\dot{\theta}(0) = \frac{v(0)}{\sqrt{r(0)^2 + r'(0)^2}} = \frac{v(0)}{2c_1}
$$
