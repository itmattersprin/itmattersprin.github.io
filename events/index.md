---
layout: index
content: true
docs_list_title: Events
use-site-title: false
---

<h1>A few events</h1>

{% assign items = site.eventsIT | sort: 'date' | reverse %}


<div class="events-list">
  {% for n in items %}
    <h4> {{ n.date | date_to_long_string }} {{ n.name }} </h4>
    {% if n.wp %}
	  <a haref="{{ n.wp }}">More here</a>
    {% endif %}
  {% endfor %}
</div>

