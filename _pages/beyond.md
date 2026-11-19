---
layout: page
title: Beyond Research
permalink: /beyond/
nav: true
nav_order: 5
description: Plants, handcrafts and community.
---

<link rel="stylesheet" href="{{ "/assets/css/academic.css" | relative_url }}">

{% for interest in site.data.cv.cv.sections['Personal Interests'] %}
<section class="academic-section" aria-labelledby="{{ interest.label | slugify }}">
  <h2 id="{{ interest.label | slugify }}">{{ interest.label }}</h2>
  <p>{{ interest.details }}</p>
  {% if interest.label == 'Plant care' %}
  <div class="academic-photo-placeholder">Photo placeholder · Plants and blooms</div>
  {% elsif interest.label == 'Handcrafts' %}
  <div class="academic-photo-placeholder">Photo placeholder · Embroidery and handmade projects</div>
  {% endif %}
</section>
{% endfor %}
