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
    <p class="academic-eyebrow">PhD Researcher · {{ cv.location }}</p>
    <h2 class="academic-lead">Learning to understand<br>human movement.</h2>
    <p class="academic-intro">I am a PhD researcher at the University of Florence’s MICC, working on computer vision,
    self-supervised learning and multimodal representations for human movement analysis and healthcare.</p>
    <p>My research connects video understanding with wearable sensing, with a focus on generalisable representations
    and motor impairment assessment. I developed EgoInertia-MI, an egocentric video–IMU benchmark, and previously
    worked on pain estimation from facial landmark dynamics.</p>
    <div class="academic-actions">
      <a class="academic-button" href="{{ '/research/' | relative_url }}">Explore my research</a>
      <a class="academic-button academic-button-secondary" href="{{ '/cv/' | relative_url }}">Academic CV</a>
    </div>
    <nav class="academic-profile-links" aria-label="Contact and profiles">
      <a href="mailto:{{ cv.email }}">Email</a>
      <a href="https://scholar.google.com/citations?user={{ site.data.socials.scholar_userid }}">Google Scholar</a>
      <a href="https://github.com/{{ site.data.socials.github_username }}">GitHub</a>
      <a href="https://www.linkedin.com/in/{{ site.data.socials.linkedin_username }}/">LinkedIn</a>
    </nav>
  </div>
  <aside class="academic-profile-panel" aria-label="Profile and affiliation">
    <img class="academic-portrait" src="{{ '/assets/img/prof_pic.png' | relative_url }}"
      alt="Portrait of Fatemah Alhamdoosh" width="563" height="704" fetchpriority="high">
    <p class="academic-eyebrow">Current affiliation</p>
    <p><strong>{{ experience[0].company }}</strong><br>{{ experience[0].position }}</p>
    <p>PhD in Smart Computing<br>Expected October 2027</p>
  </aside>
</div>

<section class="academic-section" aria-labelledby="research-interests">
  <p class="academic-eyebrow">Research interests</p>
  <h2 id="research-interests">Vision, movement and multimodal learning</h2>
  <ul class="academic-topics">
    <li>Video understanding</li><li>Self-supervised learning</li><li>Multimodal representations</li>
    <li>Human movement foundation models</li><li>Domain generalisation</li><li>Motor impairment assessment</li>
  </ul>
</section>

<section class="academic-section" aria-labelledby="research-experience">
  <h2 id="research-experience">Research experience</h2>
  {% for role in experience limit:2 %}
  <div class="academic-timeline-entry">
    <p class="academic-date">{{ role.start_date | append: '-01' | date: '%b %Y' }} – {% if role.end_date == 'present' %}Present{% else %}{{ role.end_date | append: '-01' | date: '%b %Y' }}{% endif %}</p>
    <div><h3>{{ role.position }}</h3><p>{{ role.company }}</p><p>{{ role.summary }}</p></div>
  </div>
  {% endfor %}
</section>

<section class="academic-section" aria-labelledby="selected-publications">
  <h2 id="selected-publications">Selected publications</h2>
  <div class="publications">{% bibliography --query @*[selected=true] %}</div>
  <a href="{{ '/publications/' | relative_url }}">View publications and citation details</a>
</section>

<section class="academic-contact" aria-labelledby="contact">
  <h2 id="contact">Get in touch</h2>
  <p>For research enquiries and collaboration, contact me at <a href="mailto:{{ cv.email }}">{{ cv.email }}</a>.</p>
</section>
