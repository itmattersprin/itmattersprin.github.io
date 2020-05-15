---
title: Publications
use-site-title: false
---

{% assign items = site.papers | sort: 'year' | reverse %}

{% assign lastyear = 9999 %}

<div class="paper-list">
  {% for paper in items %}
  {% if paper.year != lastyear %}
  <h2> {{ paper.year }}</h2>
  {% endif %}
  {% assign lastyear = paper.year %}
  <article class="paper-preview">
	<strong>{{ paper.title }}</strong><br>
	{% for a in paper.author %}
	  {{ a }}, 
	{% endfor %}
	<br>
	{% if paper.container-title %} {{ paper.container-title }}. {% endif %}
	{% if paper.editor %}
	  Editors
	  {% for e in paper.editor %}
	    {{ e['given'] }} {{ e['dropping-particle'] }} {{ e['family'] }}{% if forloop.last %}.{% else %}, {% endif %} 
	  {% endfor %}
	<br>
	{% endif %}
	{% if paper.journal %} {{ paper.journal }}. {% endif %}
	{% if paper.collection-title %} {{ paper.collection-title }}, {% endif %}
	Volume {{ paper.volume }}{% if paper.issue %} ({{ paper.issue }}){% endif %},
	{% if paper.page %} {{ paper.page }}, {% endif %}
	{{ paper.year }}.
	{% if paper.URL %} <a href="{{ paper.URL }}" target="new"><i class="fa fa-link"></i></a> {% endif %}
   </article>
  {% endfor %}
</div>
