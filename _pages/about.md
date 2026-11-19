---
layout: about
title: About
permalink: /
subtitle: Computer Vision · Multimodal Machine Learning
selected_papers: false
social: false
announcements:
  enabled: false
latest_posts:
  enabled: false
---

<link rel="stylesheet" href="{{ '/assets/css/academic.css' | relative_url }}">

{% assign cv = site.data.cv.cv %}
{% assign experience = cv.sections['Professional Experience'] %}

<div class="academic-hero">
  <div>
    <p class="academic-intro">I am a PhD researcher at the University of Florence’s MICC, working on computer vision,
    self-supervised learning and multimodal representations for human movement analysis and healthcare.</p>
    <p>I developed EgoInertia-MI, an egocentric video–IMU benchmark for motor impairment assessment,
    and studied pain estimation from facial landmark dynamics.</p>
    <nav class="academic-profile-links" aria-label="Contact and profiles">
      <a href="mailto:{{ cv.email }}">Email</a>
      <a href="https://scholar.google.com/citations?user={{ site.data.socials.scholar_userid }}">Google Scholar</a>
      <a href="https://github.com/{{ site.data.socials.github_username }}">GitHub</a>
      <a href="https://www.linkedin.com/in/{{ site.data.socials.linkedin_username }}/">LinkedIn</a>
    </nav>
<section class="academic-interest-summary" aria-labelledby="research-interests">
  <h2 id="research-interests">Research interests</h2>
  <p>Video understanding; self-supervised and multimodal learning; human movement foundation models;
  domain generalisation; motor impairment assessment.</p>
</section>
  </div>
  <aside class="academic-profile-panel" aria-label="Profile and affiliation">
    <img class="academic-portrait" src="{{ '/assets/img/prof_pic.png' | relative_url }}"
      alt="Portrait of Fatemah Alhamdoosh" width="563" height="704" fetchpriority="high">
    <p class="academic-date">{{ cv.location }}</p>
  </aside>
</div>

<section class="academic-section" aria-labelledby="research-experience">
  <h2 id="research-experience">Research experience</h2>
  {% for role in experience limit:2 %}
  <div class="academic-timeline-entry">
    <p class="academic-date">{{ role.start_date | append: '-01' | date: '%b %Y' }} – {% if role.end_date == 'present' %}Present{% else %}{{ role.end_date | append: '-01' | date: '%b %Y' }}{% endif %}</p>
    <div><h3>{{ role.position }}</h3><p>{{ role.company }}</p></div>
  </div>
  {% endfor %}
</section>

<section class="academic-section" aria-labelledby="selected-publications">
  <h2 id="selected-publications">Selected publications</h2>
  <div class="publications">{% bibliography --query @*[selected=true] %}</div>
  <a href="{{ '/publications/' | relative_url }}">All publications</a>
</section>

<section class="academic-contact" aria-labelledby="contact">
  <h2 id="contact">Contact</h2>
  <p>Research enquiries: <a href="mailto:{{ cv.email }}">{{ cv.email }}</a>.</p>
</section>
