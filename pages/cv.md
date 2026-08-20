---
layout: page
title: "Curriculum Vitae"
permalink: /cv/
---
<a id="top"></a>

<style>
  .cv-row {
    display: grid;
    grid-template-columns: minmax(9rem, max-content) 1fr;
    column-gap: 1.5rem;
    padding: 1rem 0;
    border-bottom: 1px solid #eaeaea;
  }

  .cv-date {
    font-weight: 600;
    color: #555;
    white-space: normal;
  }

  .cv-content > *:first-child {
    margin-top: 0;
  }

  .cv-content ul {
    margin: 0.4rem 0;
    padding-left: 1.25rem;
  }

  .cv-content ul ul {
    margin: 0.2rem 0;
  }

  @media (max-width: 640px) {
    .cv-row {
      grid-template-columns: 1fr;
      row-gap: 0.35rem;
    }
  }
</style>

<a href="../assets/docs/2026-06-27_curriculum_vitae.pdf">📄 Download PDF version of my CV.</a>

> You can see some examples of the work I've done in the projects link on the side, or just click [here](/projects/).

### 🧭 Navigation
- [Skills](#skills)
- [Work](#work)
- [Education](#education)
- [Other Qualifications](#other)
- [Publications](/publications/)

<a id="skills"></a>
## Skills

#### Technical:
- Mathematical optimisation
- Statistics
   - Regression
   - Hypothesis testing
   - Design of experiments
- Classical mechanics
- Robot control
- Mechanical design

#### Soft:
- Systems thinking
- Project management (Six Sigma & DMAIC)
- Root cause analysis
- Workshopping

#### Programming Languages:
- C++ (advanced)
- Python (basic)
- MATLAB

#### Spoken Languages:
- 🇬🇧 English (native)
- 🇮🇹 Italian (beginner)

<a id="work"></a>
## Work

<div class="cv-row">
<div class="cv-date">January 2026 – <br> Present</div>
<div class="cv-content" markdown="1">

**Independent Business & Engineering Consultant**  
_Sydney, Australia_

- Leading a business process improvement investigation with an estimated impact of **$500,000** for [The Butcher's Pantry](https://thebutcherspantry.com.au/), involving:
  - Designing and analysing customer surveys.
  - Identifying key performance indicators (KPIs) for analysis.
  - Hosting root cause analysis workshops.
- Developing force-feedback control algorithms for [Crest Robotics](https://crestrobotics.co/) to enable remote operation of high-voltage switchgear, reducing human exposure to hazardous environments.
- Collaborating with the Italian Institute of Technology to develop predictive control for dynamic collision avoidance of mobile robots, involving:
  - Designing reusable C++ software architecture for trajectory generation and control.
  - Integrating the software into a [ROS 2 Nav2](https://docs.nav2.org/) plugin for deployment on the [R1 humanoid robot](https://icub.iit.it/products/r1-robot).
- Collaborating with the University of Technology Sydney on nonlinear regression to characterise the behaviour of non-Newtonian fluids (oobleck) for force control in human–robot interaction.

</div>
</div>

<div class="cv-row">
<div class="cv-date">February 2024 – <br> January 2026</div>
<div class="cv-content" markdown="1">

**Research Fellow**  
_University of Leeds, United Kingdom_

- Provided expertise on software design & control methods for the [Terabotics project](https://warwick.ac.uk/fac/sci/physics/research/condensedmatt/ultrafastphotonics/emmasthzgroup/terabotics/) (high-frequency light sensors with robotic systems in cancer diagnosis).
- Secured **£22,000** in competitive, and international research funding.
- Principal Investigator on an international collaboration for [magnetic tentacle robots for heart intervention](https://wun.ac.uk/wun/research/view/magnetically-controlled-tentacle-robots-for-transcatheter-structural-heart-intervention/) with the University of Technology Sydney, and Chinese University of Hong Kong.
- Designed and implemented a [C++ library for robot control](https://github.com/Woolfrey/software_robot_library) with modular [ROS2 action servers](https://github.com/Woolfrey/server_serial_link) to support complex robot manipulation tasks.
- Led a [cross-disciplinary workshop](https://woolfrey.github.io/projects/#terabotics-workshop) between physicists and engineers for a mini-project involving:
  - Enumerating engineering specifications,
  - Identifying risks & countermeasures, and
  - Sequencing task dependencies.

</div>
</div>

<div class="cv-row">
<div class="cv-date">July 2021 – <br> December 2023</div>
<div class="cv-content" markdown="1">

**Postdoc**  
_Humanoid Sensing & Perception, Istituto Italiano di Tecnologia_

- Team leader for Humanoid Sensing & Perception on the [ergoCub humanoid robot project](https://ergocub.eu/) which involved:
  - Leading [collaborative planning workshops](https://woolfrey.github.io/projects/#ergocub),
  - Directing Agile sprints to meet project deadlines,
  - Chairing weekly project progress meetings.
- Designed and implemented [bimanual control classes](https://github.com/hsp-iit/ergocub-bimanual) in C++ for the ergoCub and iCub2 robots.
- Developed and deployed a [convex optimization algorithm](https://github.com/Woolfrey/software_simple_qp) for real-time robot control.
- Developed interface definition layers (IDLs) for controlling a humanoid robot as part of an [autonomous human–robot interaction system](https://github.com/ergoCub-HSP/ergocub-manipulation) involving perception and decision trees.

</div>
</div>

<div class="cv-row">
<div class="cv-date">February 2015 – <br> June 2020</div>
<div class="cv-content" markdown="1">

**Doctoral Candidate / Engineer / Research Associate**  
_Center for Autonomous Systems, University of Technology Sydney_

- Contributed to the [submerged pile inspection robot](https://www.youtube.com/watch?v=hFtW2cXaHYk) by:
  - Designing mechanical components in SolidWorks,
  - Developing technical drawings for production, and
  - Developing a hierarchy and version control system to manage engineering files.
- Led [collaborative design workshops](https://woolfrey.github.io/projects/#submerged-pile-inspection-robot) for prototype development to:
  - Identify critical use cases,
  - Enumerate engineering specifications, and
  - Brainstorm innovative features.
- Developed predictive control algorithms in C++ for robot arms on moving platforms.
- Collected and analyzed time-series data for wave motion prediction, implementing real-time forecasting algorithms in MATLAB.

</div>
</div>

<div class="cv-row">
<div class="cv-date">December 2011 – <br> December 2014</div>
<div class="cv-content" markdown="1">

**Engineering Scholar, Six Sigma Project Manager**  
_Continuous Improvement Group, Maintenance Directorate, Sydney Trains_

- Led a project to save **$1,900,000 / year** for intercity train pantograph collector strip wear involving:
  - Measurement system analysis of gauges,
  - Regression modeling of wear rates, and
  - Hypothesis testing to identify root causes.
- Led a project to save **$100,000 / year** by streamlining train inspections using:
  - Root cause analysis with fishbone (Ishikawa) diagrams, and
  - Process mapping and task sequencing to reduce inspection time.
- Managed cross-functional stakeholder engagement across engineering, operations, and management teams to ensure project alignment and success.
- Investigated systemic causes of train punctuality and prepared reports for senior management.

</div>
</div>

<div class="cv-row">
<div class="cv-date">April 2007 – <br> March 2011</div>
<div class="cv-content" markdown="1">

**Maintenance Fitter**  
_Precision Valve Australia_

- Conducted preventative & reactive maintenance on assembly machines for aerosol valves:
  - Increased output from **114% to 140%** on a sub-assembly machine by identifying & rectifying excess movement in the pulley system.
  - Improved yield from **84% to 98%** on a machine by identifying and reducing variation in diameter of the spring component.
- Fabricated, and modified small machine parts to reduce machine downtime, and increase yield.
- Applied 5S methodology to the production area, improving organisation and workflow.
- Authored and compiled reports on product defects, and machine reliability, for management, and international customers.

</div>
</div>

<div class="cv-row">
<div class="cv-date">2006</div>
<div class="cv-content" markdown="1">

**Barista, Server**  
_Jester's Pies, Panania, NSW_

- Managed stock-keeping, inventory ordering, and daily opening/closing procedures.
- Delivered attentive customer service, building positive relationships and repeat business.
- Recognized for barista skills; frequently requested by management to assist on high-demand days.
- Disseminated expertise with other staff on coffee preparation techniques and machine maintenance.

</div>
</div>

<a id="education"></a>
## Education

<div class="cv-row">
<div class="cv-date">2015 – 2020</div>
<div class="cv-content" markdown="1">

**Doctor of Philosophy**  
_University of Technology Sydney_

**Thesis:** _Control of Manipulators on Moving Platforms Under Disturbance_

Mobile robots, such as underwater vehicles, drones, and rovers, are now being combined with manipulators to perform a variety of work in the field. But current state of the art in control assumes that disturbances from the environment are minimal. However, the effects of wind, waves, and rough terrain may make it difficult for the vehicle to hold a steady base for the manipulator. Or, in some cases, the vehicle may lack the control authority to negate disturbances in all directions. In this thesis, predictions of the base motion are used to formulate control strategies that enable a manipulator to proactively counter, and even make use of, these disturbances.

</div>
</div>

<div class="cv-row">
<div class="cv-date">2010 – 2015</div>
<div class="cv-content" markdown="1">

**B.E. Mechanical & Mechatronic Engineering (1st Class Honors)**  
_University of Technology Sydney_

- Ranked in the top 15% of all UTS students in 2012.
- Electives:
  - Control of Mechatronics Systems
  - Advanced Robotics
  - Design Optimisation for Manufacturing
  - Biomedical Instrumentation
- **Honors thesis:** _"A Systems Thinking Approach to Pantograph Collector Strip Wear"_ — Examined interrelated causal factors contributing to collector strip wear on rollingstock; applied regression modeling and hypothesis testing to identify key root causes to improve longevity.

</div>
</div>

<div class="cv-row">
<div class="cv-date">2007 – 2009</div>
<div class="cv-content" markdown="1">

**Certificate IV in Mechanical Trades (MEM40105)**  
_South Western Sydney Institute of TAFE_

Key competencies:

- Complex milling and turning (gear cutting, thread cutting, eccentric turning).
- Advanced fitting techniques (pipe bending, mechanical seals, shrink/expansion fitting, non-destructive bearing removal, wheel balancing).
- Machine installation, alignment, and floor planning.
- Fault diagnosis and repair of mechanical systems.
- MIG welding.

</div>
</div>

<div class="cv-row">
<div class="cv-date">2000 – 2005</div>
<div class="cv-content" markdown="1">

**High School Certificate**  
_St Mary's Cathedral College, Sydney_

- Received a certificate for perfect attendance in Grade 11 (2004) and Grade 12 (2005).
- Member of the competitive swimming team; represented school at multiple state-level competitions.
- Electives included:
  - 3 Unit Advanced English
  - 3 Unit Advanced Mathematics
  - 2 Unit Information Technology
  - 2 Unit Studies of Religion

</div>
</div>

<a id="other"></a>
## Other Qualifications

| Year | Qualification |
|------|---------------|
| 2017 | Lean Six Sigma Black Belt <br> _UTS Business School_ |
| 2014 | Lean Six Sigma Green Belt <br> _Sydney Trains_ |
| 2011 | National OHS Construction Induction Training <br> _Safework NSW_ |
| 2011 | Rail Industry Safety Induction <br> _RailCorp_ |
| 2011 | Work Safely in the Construction Industry <br> _Advance OHS_ |
| 2009 | Certificate III in Competitive Manufacturing (MCM 30104) <br> _Skillup Australia_ |

<a id="teaching"></a>
## Teaching and Supervision

<div class="cv-row">
<div class="cv-date">2025 - Present</div>
<div class="cv-content" markdown="1">

**PhD Co-Supervisor**  
_University of Technology Sydney_

- Co-supervising a PhD student researching model predictive contouring control applied to robotic hip replacement surgery.
- Mentoring in control theory, fundamental robotics concepts, and research methods, including experimental design, simulation, and implementation.
- Coaching the student on articulating research problems, solutions, and benefits to both professional and academic audiences.
- Providing guidance in C++ programming to support simulation, testing, and integration of robotic control algorithms.

</div>
</div>

<div class="cv-row">
<div class="cv-date">2018 - Present</div>
<div class="cv-content" markdown="1">

**Guest Lecturer, Teaching Assistant**  
Lean Six Sigma Yellow Belt Certification Program  
_Technical University of Munich (via edX.org, Coursera)_

- Delivered guest lectures on advanced topics in Lean manufacturing and the Toyota Production System, connecting theory to real-world professional practice.
- Actively engaged with hundreds of thousands of students worldwide via online forums, answering questions, providing applied examples, and facilitating discussions.
- Delivered live information sessions on Lean Six Sigma professional practice, responding to participant questions and encouraging course engagement.
- Contributed to course development and learning experience for a globally ranked top 10 online course of all time by [Class Central](https://www.classcentral.com/collection/top-free-online-courses?sort=rating-up&page=2).

</div>
</div>

<div class="cv-row">
<div class="cv-date">2016 - Present</div>
<div class="cv-content" markdown="1">

**Casual Academic**  
Industrial Robotics, Mechanical & Mechatronic Design  
_University of Technology Sydney_

- Helped design & develop the Industrial Robotics subject when it first launched in 2016:
  - Recorded core lecture videos, which have been seen by tens of thousands of people on YouTube,
  - Designed and developed tutorial exercises, and
  - Developed online learning material for the UTS Canvas platform.
- Developed lecture content for the Mechanical & Mechatronic Design subject.
- Supervised and mentored students in tutorials, laboratories, and design projects.
- Participated in project review panels & live student assessments, evaluating outcomes and offering constructive feedback.

</div>
</div>

<a id="publications"></a>
## Publications

⬅️ Click the link on the sidebar, or click [here](/publications/).

[🔝 Back to top.](#top)
