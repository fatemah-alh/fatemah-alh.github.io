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
  <p class="academic-eyebrow">Current directions</p>
  <h2 id="ongoing-research">Ongoing Research</h2>
  <div class="academic-grid">
    {% for project in sections['Ongoing Research Projects'] %}
    <article class="academic-research-entry">
      <h3 id="{{ project.name | slugify }}">{{ project.name }}</h3>
      <p>{{ project.summary }}</p>
    </article>
    {% endfor %}
  </div>
</section>

<section class="academic-section" aria-labelledby="completed-research">
  <p class="academic-eyebrow">Previous work</p>
  <h2 id="completed-research">Completed Research</h2>
  {% for project in sections['Completed Research Projects'] %}
  <article class="academic-research-entry">
    <h3 id="{{ project.name | slugify }}">{{ project.name }}</h3>
    <p>{{ project.summary }}</p>
    {% if project.name == 'EgoInertia-MI' %}
    <p><a href="https://arxiv.org/abs/2607.03934">Read the preprint</a> · <a href="https://fatemah-alh.github.io/EgoInertia-MI-Page/">Project website</a></p>
    {% elsif project.name == 'Video-Based Pain Estimation' %}
    <p><a href="https://doi.org/10.1109/TBIOM.2025.3592836">Read the journal article</a></p>
    {% endif %}
  </article>
  {% endfor %}
</section>

<p>For publication records and citations, see <a href="{{ '/publications/' | relative_url }}">Publications</a>.</p>
