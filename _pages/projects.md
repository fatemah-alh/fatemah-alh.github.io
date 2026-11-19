---
layout: page
title: Research
permalink: /research/
nav: true
nav_order: 1
description: Learning representations of human movement from video and wearable sensing.
---

<link rel="stylesheet" href="{{ "/assets/css/academic.css" | relative_url }}">

{% assign sections = site.data.cv.cv.sections %}

<section class="academic-section" aria-labelledby="ongoing-research">
  <h2 id="ongoing-research">Ongoing Research</h2>
    {% for project in sections['Ongoing Research Projects'] %}
    <article class="academic-research-entry">
      <h3 id="{{ project.name | slugify }}">{{ project.name }}</h3>
      <p>{{ project.summary }}</p>
    </article>
    {% endfor %}
</section>

<section class="academic-section" aria-labelledby="completed-research">
  <h2 id="completed-research">Completed Research</h2>
  {% for project in sections['Completed Research Projects'] %}
  <article class="academic-research-entry">
    <h3 id="{{ project.name | slugify }}">{{ project.name }}</h3>
    <p>{{ project.summary }}</p>
    {% if project.name == 'EgoInertia-MI' %}
    <p><a href="https://arxiv.org/abs/2607.03934">Preprint</a> · <a href="https://fatemah-alh.github.io/EgoInertia-MI-Page/">Project website</a></p>
    {% elsif project.name == 'Video-Based Pain Estimation' %}
    <p><a href="https://doi.org/10.1109/TBIOM.2025.3592836">Journal article</a></p>
    {% endif %}
  </article>
  {% endfor %}
</section>

<p>See <a href="{{ '/publications/' | relative_url }}">Publications</a>.</p>
