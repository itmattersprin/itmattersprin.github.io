---
layout: index
content: true
docs_list_title: Events
use-site-title: false
---

{% assign items = site.toolkits | sort: 'name' %}

<h1> Tools </h1>

<div class="tools-list">
  {% for n in items %}
    <h2> {{ n.name }} {% if n.date %} ({{ n.date | date_to_long_string }}) {% endif %}</h2>
    <p>{{ n.description }}
		{% if n.url %}<br/>Available <a href="{{ n.url }}">here</a> {% endif %}
		{% if n.contact %}<br/><a href="mailto:{{ n.contact }}">Contact</a>. {% endif %}
    </p>
  {% endfor %}
</div>
