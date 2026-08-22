---
layout: default
title: Jon Woolfrey
---

## 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Welcome 🇮🇹 Benvenuti 🇦🇺 G'Day

---

#### 🖋️ Latest Post

{% assign latest = site.posts.first %}

{% assign preview = latest.preview | default: latest.excerpt %}

#### [{{ latest.title }}]({{ latest.url | relative_url }})

<p style="font-size: 0.85em; color: var(--DressBlues);">{{ latest.date | date: "%B %-d, %Y" }}</p>

{{ preview }}

[Read more →]({{ latest.url | relative_url }})

Other recent posts:

{% for post in site.posts offset: 1 limit: 3 %}
- [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}
- [All posts →]({{ "/posts/" | relative_url }})

<style>
  .subscribe-box {
    margin: 0.6rem 0;
    padding: 0.6rem 0.85rem;
    border: 1px solid #eaeaea;
    border-radius: 6px;
    width: 100%;
    box-sizing: border-box;
  }

  .subscribe-box p.subscribe-lead {
    margin: 0 0 0.4rem 0;
    font-size: 0.85em;
    color: #444;
  }

  .subscribe-box form {
    display: flex;
    gap: 0.4rem;
    flex-wrap: wrap;
    align-items: center;
  }

  .subscribe-box label {
    display: none;
  }

  .subscribe-box input[type="email"] {
    flex: 1 1 10rem;
    padding: 0.3rem 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 0.85em;
  }

  .subscribe-box input[type="submit"] {
    padding: 0.3rem 0.7rem;
    border: none;
    border-radius: 4px;
    background: #222;
    color: #fff;
    font-size: 0.85em;
    cursor: pointer;
  }

  .subscribe-box input[type="submit"]:hover {
    background: #444;
  }

  .subscribe-box p.subscribe-footer {
    margin: 0.35rem 0 0 0;
    font-size: 0.7em;
    color: #999;
  }

  .subscribe-box p.subscribe-footer a {
    color: #999;
  }
</style>

<div class="subscribe-box">
  <p class="subscribe-lead">Get email notifications when I post something new:</p>
  <form action="https://buttondown.com/api/emails/embed-subscribe/Woolfrey" method="post" class="embeddable-buttondown-form">
    <label for="bd-email">Enter your email</label>
    <input type="email" name="email" id="bd-email" placeholder="you@example.com" aria-label="Enter your email" required />
    <input type="submit" value="Subscribe" />
  </form>
  <p class="subscribe-footer"><a href="https://buttondown.com/refer/Woolfrey" target="_blank">Powered by Buttondown.</a></p>
</div>

---

#### 🖥️ Find Me Online

- Coursera: My guest lectures for the Technical University of Munich:
  * [Lean Production Fundamentals](https://www.coursera.org/learn/lean-production-fundamentals/)
  * [Advanced Lean Production & Continuous Improvement](https://www.coursera.org/learn/advanced-lean-production-continuous-improvement/)
- [Github](https://github.com/Woolfrey): Explore my coding projects and repositories.
- [LinkedIn](https://www.linkedin.com/in/jonathanwoolfrey/): For professional connections.
- [YouTube](https://www.youtube.com/@Woolfrey/videos): For robot videos, lectures, and more.

---

#### ⌨️ Coding Projects

Here are some of my main projects:

- [tufteplotlib](https://pypi.org/project/tufteplotlib/): A Python library for generating beautiful, minimalist graphs in the style of [Edward Tufte](https://www.edwardtufte.com/).
- [RobotLibrary](https://github.com/Woolfrey/software_robot_library): My C++ library for robot motion control.
- [ROS2](https://docs.ros.org/en/humble/index.html) packages implementing RobotLibrary for real-time robot control:
  * [serial_link_interfaces](https://github.com/Woolfrey/interface_serial_link)
  * [serial_link_action_server](https://github.com/Woolfrey/server_serial_link)
  * [serial_link_action_client](https://github.com/Woolfrey/client_serial_link)
- [Simple QP Solver](https://github.com/Woolfrey/software_simple_qp): A light-weight convex optimisation algorithm.
- [ergoCub-bimanual](https://github.com/hsp-iit/ergocub-bimanual): Two-handed grasping control of a humanoid robot using [YARP](https://www.yarp.it/latest/).

---

#### 🤝 Current Collaborations

- [The Butcher's Pantry](https://thebutcherspantry.com.au/): A business improvement initiative to boost sales & revenue.
- [Crest Robotics](https://crestrobotics.co/): Helping solve force feedback control for teleoperated robots.
- [Robotic hip replacement surgery](https://www.uts.edu.au/research/centres/robotics-institute/partner-us/health-robotics) at the University of Technology Sydney.
