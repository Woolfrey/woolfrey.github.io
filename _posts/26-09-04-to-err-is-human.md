---
categories: [lss, error]
date: 2026-09-04
image: ../assets/images/posts/2026/error_classification.png
layout: post
preview: "Humans are prone to error; it's in our nature as mortal beings. In this post I discuss the concept of error prevention. First, by looking at how psychologists classify types of errors, and how we might address them. Second, I give my 3 rules for a good error-prevention method. Finally, I give some examples from everyday life."
title: "To Err Is Human"
---

> Humans are prone to error; it's in our nature as mortal beings. In this post I discuss the concept of error prevention. First, by looking at how psychologists classify types of errors, and how we might address them. Second, I give my 3 rules for a good error-prevention method. Finally, I give some examples from everyday life.

#### 🧭 Navigation

- [A Story](#a-story-about-error-proofing)
- [Human Error](#human-error)
    - [Aviation Accidents](#aviation-accidents)
    - [Classifying Human Error](#classifying-human-error)
- [Poka Yoke (ポカヨケ)](#poka-yoke-ポカヨケ)
    - [What Is It?](#what-is-it)
    - [3 Rules](#3-rules)
- [Examples](#examples)
- [Key Takeaways](#key-takeaways)

## A Story About Error-Proofing

A soap manufacturer was occasionally shipping empty boxes, which was costing a substantial amount of money, and causing bad repute with their customers.

They hired an engineering firm for **$8,000,000** to develop a solution. The firm installed an expensive electronic weighing station at the end of the packing conveyer belt. Every box was weighed to ensure it was full. If an empty box was detected the production line automatically halted, sirens rang, and lights flashed to alert the workers.

<p align="center">
    <img src="/assets/images/posts/2026/weigh_station_1.png" width="600" height="auto" loading="lazy"/>
</p>

After a couple of months not a single empty box made it through the packing line. Customer satisfaction and revenue were up. Success! Money well spent.

But the production manager hadn't heard a single alarm go off in over a month. Curious as to why, he paid a visit to the production floor to investigate.

He found that the weighing station had been unplugged. Instead someone had placed a large fan facing the conveyor belt. Any empty box that passed by was blown off the conveyer, without stopping production.

<p align="center">
    <img src="/assets/images/posts/2026/weigh_station_2.png" width="600" height="auto" loading="lazy"/>
</p>

He asked one of the production workers why they had bypassed the weighing station. The worker replied that they were getting annoyed with the alarm going off every few minutes, so they used a fan to blow off the empty boxes instead.

---

I like this story because it emphasises some important principles around problem-solving:

- Economic, effective solutions: a decent industrial fan would only cost a hundred dollars or so (instead of millions),
- The fan does not halt production, or disturb workers, and
- The solution was a simple invention of the workers themselves; not an engineer who sits behind a desk.

## On Human Error

Now you might be thinking _"OK Jon, that's a neat story but the title of your post refers to human error."_ The bridge between this story and the theme of this post is exemplified by a book called "A Human Error Approach to Aviation Accident Analysis" [^1].

(Fun fact: I read this book on a plane in a middle of a thunderstorm!)

### Aviation Accidents

Below is a plot of the number of aviation accidents and human fatalities over time. The invention of the jet engine in the 1930s led to a proliferation of human flight in the 1940s. But the juvenile technology was prone to catastrophic engineering failures, as reflected in the data.

<p align="center">
    <img src="/assets/images/posts/2026/aviation_accidents.png" width="600" height="auto" loading="lazy"/>
    <br>
    <em style="font-size: 0.8em;"> Engineering failures driving aviation accidents have been rectified, but human errors are persistent (<a href="https://github.com/rsgilltc/Aviation-Accidents">source</a>).</em>
</p>

Eventually the sophistication of aerodynamics, mechanics, and material science prevented these fatal engineering failures. But after the precipitous decline in accidents in the 1940s there remains a persistent, constant failure rate up until the present day.

These errors are largely attributable to human error.

Even _with_ the rapid decline in aviation accidents the number of fatalities only showed a moderate decrease from about 1945 to 1970. It is only from about the 1970s onward that we observe a steady decline in deaths.

Whilst we can use our knowledge of the physical sciences to prevent engineering failures, the problem of human error remains a constant. To address it we must turn to studying the mind rather than the physical world.

### Classifying Human Error

Psychologists have studied and classified human error into two broad categories [^2] [^3] 

1. **Mistakes:** when the wrong action is applied to a task, even if said action is executed properly, and
2. **Slips:** when the action itself is correct, but applied inappropriately.

A mistake is what a layman might categorise as a genuine error, whereas one might regard a slip as being careless, or inattentive. But slips are a real phenomenon. Rather than dismiss them we should understand their mechanics so we can mitigate or prevent them.

<p align="center">
    <img src="/assets/images/posts/2026/error_classification.png" width="400" height="auto" loading="lazy"/>
    <br><br>
    <em style="font-size: 0.8em;">A tree diagram illustrating the decomposition of human error into different categories.</em>
</p>


| Mistake         |  Definition     | Fix |
|-----------------|-----------------|-----|
| Knowledge-based | An incorrect decision is made due to insufficient or incomplete knowledge of a situation. | More training, and provide better information at the point-of-use; signs, manuals, digital displays etc.  |
| Memory lapse    | Failing to recall the correct action when required. | Retrain to refresh knowledge, provide memory cues in the environment; use size, shape, colour, form, signage, etc. |
| Rule-based      | A procedure is applied to a familiar, but incorrect situation. | Engineer the task to make relevant differences between situations obvious, and prevent the wrong procedure from being selected where possible. |

<br>

| Slip         |  Definition     | Fix |
|--------------|-----------------|-----|
| Action-based | A habitual action is applied to the wrong situation.   | Make the activity physically, visually, procedurally distinct. Make the incorrect actions impossible.  |
| Memory lapse | Forgetting to perform an intended action in the moment. | Minimise disruptions, use checklists, or restrict progress until the correct action is performed.|

## Poka-yoke (ポカヨケ)

### What Is It?

Poka-yoke is Japanese for "mistake-proofing", or "error-proofing", and is a tenet of the Toyota Production System[^4]. Its intention is to implement systems, procedures, and constraints that either prevent errors outright, or halt production so defects cannot proceed through the production line. It is both a method and an attitude. 

It was originally called "baka-yoke" (idiot-proofing), but was renamed since one of the principles of the Toyota Management Philosophy is respect for people.

### 3 Rules

So what makes a good poka-yoke device or method? Here are 3 rules I've found that can cover the majority of use cases:

1. Mistakes are prevented from occurring, or the process is prevented from continuing if one occurs.
2. It is applied to 100% of items or events, not just a random sample.
3. There is an immediate return on investment.

Rule #1 follows directly from the Toyota Production System. It is not sufficient for an error to be observed, or documented. It must be prevented entirely.

In mass production systems sampling methods are used to detect errors. I witnessed this myself when working for a company that made buttons and valves for aerosols. This relies on probability; if we don't detect errors in the sample we can be confident (but not certain!) that the entire production batch does not contain defects. Rule #2 asserts that this is insufficient: Every. Single. Item. must pass through the detector.

Rule #3 is a bit more vague, but as we saw in the story [above](#a-story-about-error-proofing), the error prevention should be cost-effective. There's no point spending \\$1,000,000 on a problem that costs you \\$1,000 a year. A good heuristic here is that the error-prevention method should cost less than the defects within a financial year.

## Examples

Below are some real-world examples to demonstrate that error-proofing is all around us. Maybe you'll even start to notice more of them!

### Boiling Water from the Kitchen Faucet

This is a photo I took in the kitchen at The University of Technology Sydney (building 2, level 11 - near the robotics labs). The faucet dispenses chilled water, and boiling water. You can activate the chilled water by depressing the blue lever.

To activate the boiling water you must press both the lever _and_ the little button on the shaft. This makes dispensing boiling water a conscious effort; it prevents an action-based slip from occurring!

I also like that if you were colour blind you can't accidentally mix up the red and blue levers (preventing a knowledge-based mistake?).

<p align="center">
    <img src="/assets/images/posts/2026/kitchen_faucet.png" width="250" height="auto" loading="lazy"/>
    <br>
    <em style="font-size: 0.8em;">To activate the boiling water you must simultaneously depress the red lever, and hold the red button.</em>
</p>


### Power Outlets

If you've done any global travel (as I have!) then you need to carry numerous adaptors for all the different power outlets in different countries. The figure below shows the various designs. The shape of the sockets prevents the wrong power plug from being inserted.

Different countries have different power sources (in terms of voltage magnitude, and frequency of the AC current). This kind of poka-yoke prevents knowledge-based mistakes (not knowing the correct power source), or even action-based slips (absent-mindedly inserting the wrong plug).

A lot of the designs are also _asymmetric_. This prevents you from inserting the plug into the wrong orientation.

<p align="center">
    <img src="/assets/images/posts/2026/power_outlets.png" width="400" height="auto" loading="lazy"/>
    <br>
    <em style="font-size: 0.8em;"> Power outlets are designed to physically constrain the type of plug that can be inserted (<a href="https://commons.wikimedia.org/wiki/File:Plug_types.svg">source</a>). </em>
</p>

### Game Boy Cartridge

The original Game Boy had a little notch in the top-right corner of the game cartridge. When you switched the power on it was physically impossible to remove it. This prevents a memory lapse slip, in case you forgot to turn it off first.

This feature was unfortunately removed from the Game Boy Advance, and its successors the Nintendo DS, and Nintendo Switch.

<p align="center">
    <img src="/assets/images/posts/2026/game_boy_cartridge.png" width="200" height="auto" loading="lazy"/>
    <br>
    <em style="font-size: 0.8em;"> The original Game Boy cartridge had a notch so you can't remove it while the console is turned on (<a href="https://www.youtube.com/shorts/JbUm5m5mJuM">source</a>). </em>
</p>


### Programming

Poka-yoke doesn't have to be physical! I've programmed lots of robots and it's very important to prevent the robot from losing control, damaging itself, or injuring someone. This is an example from my own [RobotLibrary](https://github.com/Woolfrey/software_robot_library).

If I want to control the end-effector velocity I need to use a thing called the Jacobian matrix. It maps the joint motor velocities to the end-effector velocity:

$$
    \mathbf{J} =
    \begin{bmatrix}
        \mathrm{J}_{11} & \cdots & \mathrm{J}_\mathrm{1n} \\
                 \vdots & \ddots &                 \vdots \\
        \mathrm{J}_{61} & \cdots & \mathrm{J}_\mathrm{6n}
    \end{bmatrix}
$$

<p align="center">
    <img src="/assets/images/projects/cup_balancing.gif" width="300" height="auto" loading="lazy"/>
    <br>
    <em style="font-size: 0.8em;"> To balance the cup we need to invert the Jacobian matrix.</em>
</p>

It has:
- 6 rows corresponding to:
   - 3 linear velocities $v_x$, $v_y$, and $v_z$,
   - 3 angular velocities $\omega_x$, $\omega_y$, and $\omega_z$
- n columns for the variable number of joints on a robot arm (typically 6, or 7).

The function signature looks like this:

```
Eigen::Matrix<double, 6, Eigen::Dynamic>
KinematicTree::jacobian(std::string &frameName)
```

Take note of the first row:

- `Eigen::Matrix` says this is a `Matrix` object from the `Eigen` library,
- `double` is the data type,
- `6` is what enforces the 6 rows,
- `Eigen::Dynamic` says the number of columns is dynamic; it can change.

It tells the compiler:
1. This _must_ be a `double`; it cannot be a `float`, `int`, `char`, or anything else.
2. It _must_ have 6 rows; it can't be 5, or 7, or anything else.

If I tried to do this:

```
Eigen::Matrix<double,3,Eigen::Dynamic> J = model->jacobian("ee_frame");
```

The compiler throws an error:

<p align="center">
    <img src="/assets/images/posts/2026/compile_error.png" width="800" height="auto" loading="lazy"/>
</p>

Programming features like these ensure you can't even run the code, thus preventing any unsafe errors happening whilst the robot is running.

## Key Takeaways

- Human error is a fundamental part of our being, and we should find intelligent ways to prevent it.
- A good error-proofing method _prevents_ errors from occurring.
- Error-proofing has been quietly designed into many aspects of modern life.
- It doesn't have to be physical; even good software design prevents errors.

---


[^1]: Wiegmann, D. A., & Shappell, S. A. (2017). "A Human Error Approach to Aviation Accident Analysis: The Human Factors Analysis and Classification System". Routledge.
[^2]: Reason, J. (2000). "Human Error: Models and Management". Bmj, 320(7237), 768-770.
[^3]: Norman, D. (2013). "The Design of Everyday Things" (Vol. 272). New York: Basic books.
[^4]: Liker, J. K. (2004). "The Toyota Way: 14 Management Principles from The World's Greatest Manufacturer." McGraw-Hill.
