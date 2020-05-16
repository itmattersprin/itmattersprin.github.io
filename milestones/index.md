---
layout: index
content: true
docs_list_title: News
use-site-title: false
---

<h1>A few milestones of {{ site.title }}</h1>

{% assign items = site.msIT | sort: 'date' %}

<div class="news-list">
  {% for n in items %}
    <h2> {% if n.date%} {{ n.date | date_to_long_string }} {% else %} ??? {% endif %} {{ n.name }} </h2>
    <h3> {{ n.description }} </h3>
    <br/>
  {% endfor %}
</div>
