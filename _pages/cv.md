---
layout: page
title: CV
permalink: /cv/
nav: true
nav_order: 3
description: Academic and professional experience.
---

<link rel="stylesheet" href="{{ '/assets/css/academic.css' | relative_url }}">

{% comment %}
The stock CV 1.0.2 renderer drops custom sections, education summaries and publication
metadata. This content page reads the unchanged RenderCV data without a theme override.
{% endcomment %}
{% assign cv = site.data.cv.cv %}
<div class="academic-cv-header">
  <h2>{{ cv.name }}</h2>
  <p>{{ cv.headline }}<br>{{ cv.location }} · <a href="mailto:{{ cv.email }}">{{ cv.email }}</a></p>
  <div class="academic-actions">
    <a class="academic-button" href="{{ '/assets/rendercv/rendercv_output/Fatemah_Alhamdoosh_CV.pdf' | relative_url }}" download>Download CV (PDF)</a>
  </div>
</div>
<nav class="academic-cv-nav" aria-label="CV sections">
  {% for section in cv.sections %}
  <a href="#{{ section[0] | slugify }}">{{ section[0] }}</a>
  {% endfor %}
</nav>

{% for section in cv.sections %}
<section class="academic-cv-section" aria-labelledby="{{ section[0] | slugify }}">
  <h2 id="{{ section[0] | slugify }}">{{ section[0] }}</h2>
  {% for entry in section[1] %}
  <div class="academic-cv-entry">
    {% if entry.company %}
      <h3>{{ entry.position }}</h3><p>{{ entry.company }}{% if entry.location %} · {{ entry.location }}{% endif %}</p>
    {% elsif entry.institution %}
      <h3>{{ entry.degree }} in {{ entry.area }}</h3><p>{{ entry.institution }}</p>
    {% elsif entry.title %}
      <h3>{{ entry.title }}</h3>
      <p>{{ entry.authors | join: ', ' | markdownify | remove: '<p>' | remove: '</p>' }}</p>
      <p>{{ entry.journal }} · {{ entry.date }}</p>
      {% if entry.doi %}<p><a href="https://doi.org/{{ entry.doi }}">DOI: {{ entry.doi }}</a></p>{% endif %}
      {% if entry.url %}<p><a href="{{ entry.url }}">Read the preprint</a></p>{% endif %}
    {% elsif entry.name %}
      <h3>{{ entry.name }}</h3>
    {% elsif entry.label %}
      <h3>{{ entry.label }}</h3><p>{{ entry.details }}</p>
    {% else %}
      {{ entry | markdownify }}
    {% endif %}
    {% if entry.start_date %}
      <p class="academic-date">
        {% assign start = entry.start_date | append: '' %}
        {% assign finish = entry.end_date | append: '' %}
        {% if start.size == 4 %}{{ start }}{% else %}{{ start | append: '-01' | date: '%b %Y' }}{% endif %} –
        {% if finish == 'present' %}Present{% elsif finish.size == 4 %}{{ finish }}{% else %}{{ finish | append: '-01' | date: '%b %Y' }}{% endif %}
      </p>
    {% endif %}
    {% if entry.summary %}<p>{{ entry.summary }}</p>{% endif %}
    {% if entry.highlights %}<ul>{% for highlight in entry.highlights %}<li>{{ highlight }}</li>{% endfor %}</ul>{% endif %}
  </div>
  {% endfor %}
</section>
{% endfor %}
