---
layout: index
content: true
docs_list_title: News
use-site-title: false
---

<h1> News from the IT-MATTERS folks </h1>

{% assign items = site.newsIT | sort: 'name' %}

<div class="news-list">
  {% for n in items %}
    <h2> {{ n.date | date_to_long_string }} {{ n.name }} </h2>
    <h2> {{ n.description }} </h2>
    <br/>
  {% endfor %}
</div>
