---
layout: archive
title:  "Touring 2016 Archive"
categories: meta
image:
  teaser: teaser_IMG_7577.JPG
excerpt_separator: ""
---

<div class="tiles">
{% for post in site.categories.touring_2016 %}
  {% include post-grid.html %}
{% endfor %}
</div><!-- /.tiles -->
