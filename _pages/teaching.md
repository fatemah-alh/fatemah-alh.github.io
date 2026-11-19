---
layout: page
title: Teaching
permalink: /teaching/
nav: true
nav_order: 4
description: Machine learning, deep learning and natural language processing.
---

<link rel="stylesheet" href="{{ "/assets/css/academic.css" | relative_url }}">

{% for role in site.data.cv.cv.sections['Teaching Experience'] %}
<section class="academic-timeline-entry">
  <p class="academic-date">{{ role.start_date | append: '-01' | date: '%b %Y' }} – {% if role.end_date == 'present' %}Present{% else %}{{ role.end_date | append: '-01' | date: '%b %Y' }}{% endif %}</p>
  <div>
    <h2>{{ role.position }}</h2>
    <p>{{ role.company }}</p>
    <p>{{ role.summary }}</p>
  </div>
</section>
{% endfor %}
