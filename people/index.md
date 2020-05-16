---
layout: index
content: true
docs_list_title: People
use-site-title: false
---

{% assign people = site.staff | sort: 'secondname' %}

<div class="people-list">
  {% for p in people %}
  <p>
	<strong>{{ p.firstname }} {{ p.secondname }}</strong>
	({{ p.affiliation }})
	<ul>
	<li>Contact: <a href="mailto:{{ p.email }}">{{ p.email }}</a></li>
	<li>web: <a href="{{ p.web }}">homepage</a></li>
	</ul>
  </p>
  <br>
  {% endfor %}
</div>

