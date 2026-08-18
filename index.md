---
layout: default
title: Jon Woolfrey
---

#### 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Welcome 🇮🇹 Benvenuti 🇦🇺 G'Day

This is a portal to my online content.

You can find your way around this website with the links on the left panel 👈

### 🖥️ Find Me Online

- Coursera: My guest lectures for the Technical University of Munich:
  * [Lean Production Fundamentals](https://www.coursera.org/learn/lean-production-fundamentals/)
  * [Advanced Lean Production & Continuous Improvement](https://www.coursera.org/learn/advanced-lean-production-continuous-improvement/)
- [Github](https://github.com/Woolfrey): Explore my coding projects and repositories.
- [LinkedIn](https://www.linkedin.com/in/jonathanwoolfrey/): For professional connections.
- [YouTube](https://www.youtube.com/@Woolfrey/videos): For robot videos, lectures, and more.

### ⌨️ Coding Projects

Here are some of my main projects:

- [tufteplotlib](https://pypi.org/project/tufteplotlib/): A Python library for generating beautiful, minimalist graphs in the style of [Edward Tufte](https://www.edwardtufte.com/).
- [RobotLibrary](https://github.com/Woolfrey/software_robot_library): My C++ library for robot motion control.
- [ROS2](https://docs.ros.org/en/humble/index.html) packages implementing RobotLibrary for real-time robot control:
  * [serial_link_interfaces](https://github.com/Woolfrey/interface_serial_link)
  * [serial_link_action_server](https://github.com/Woolfrey/server_serial_link)
  * [serial_link_action_client](https://github.com/Woolfrey/client_serial_link)
- [Simple QP Solver](https://github.com/Woolfrey/software_simple_qp): A light-weight convex optimisation algorithm.
- [ergoCub-bimanual](https://github.com/hsp-iit/ergocub-bimanual): Two-handed grasping control of a humanoid robot using [YARP](https://www.yarp.it/latest/).

### 🤝 Current Collaborations

- [The Butcher's Pantry](https://thebutcherspantry.com.au/): A business improvement initiative to boost sales & revenue.
- [Crest Robotics](https://crestrobotics.co/): Helping solve force feedback control for teleoperated robots.
- [Robotic hip replacement surgery](https://www.uts.edu.au/research/centres/robotics-institute/partner-us/health-robotics) at the University of Technology Sydney.

---

## Latest Post

{% assign latest = site.posts.first %}

{% comment %}
  Prefer a <!--preview--> ... <!--preview--> snippet if the post has one
  (kept short and hand-written, same one used for LinkedIn/Slack link
  previews). Falls back to the <!--more--> excerpt for older posts that
  don't have preview markers yet.
{% endcomment %}
{% assign preview_parts = latest.content | split: "<!--preview-->" %}
{% if preview_parts.size >= 3 %}
  {% assign preview = preview_parts[1] %}
{% else %}
  {% assign preview = latest.excerpt %}
{% endif %}

### [{{ latest.title }}]({{ latest.url | relative_url }})

<p style="font-size: 0.85em; color: var(--DressBlues);">{{ latest.date | date: "%B %-d, %Y" }}</p>

{{ preview }}

[Read more →]({{ latest.url | relative_url }})
