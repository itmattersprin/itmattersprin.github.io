---
layout: index
content: true
docs_list_title: News
use-site-title: false
---

<h1>A few milestones of {{ site.title }}</h1>

{% assign items = site.msIT | sort: 'date' %}

<div class="news-list">
<ul>
  {% for m in items %}
	<li> <span style="color:#ff1111">{{ m.name }}</span>
	{% if m.date %} {{ m.date | date_to_long_string }} {% else %} ??? {% endif %}
    <br/>{{ m.description }} {% if m.url %} <a href="{{ m.url }}">here</a> {% endif %}
    </li>
  {% endfor %}
</ul>
</div>
