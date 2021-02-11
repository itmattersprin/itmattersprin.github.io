---
layout: index
content: true
docs_list_title: Events
use-site-title: false
---

<h1>A few events</h1>

{% assign items = site.eventsIT | sort: 'date' | reverse %}


<div class="events-list">
<ul>
  {% for n in items %}
    <li> {{ n.date | date_to_long_string }} - {{ n.enddate | date_to_long_string }} {{ n.name }}
    {% if n.wp %}
	  <a href="{{ n.wp }}">More here</a>
    {% endif %}
 </li>
 {% endfor %}
</ul>
</div>

