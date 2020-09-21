---
layout: index
content: true
docs_list_title: Publications
use-site-title: false
---

<h1>Publications</h1>

{% assign items = site.papers | sort: 'year' | reverse %}

{% assign lastyear = 9999 %}

<div class="paper-list">
  {% for paper in items %}
  {% if paper.year != lastyear %}<h2> {{ paper.year }}</h2>{% endif %}
  {% assign lastyear = paper.year %}
  <article class="paper-preview">
	<strong>{{ paper.title }}</strong>
	{% if paper.wps %} <span style="color:#f98811">(WP {% for w in paper.wps %} {{ w }}{% if forloop.last %}) <span style="color:#11bbff">{% for p in paper.partner %}{{ p }}{% if forloop.last %}{% else %}, {% endif %} {% endfor %}</span>{% else %}, {% endif %}{% endfor %}</span>{% endif %}
	<br>
	{% for a in paper.author %}
	  {{ a }}, 
	{% endfor %}
	<br>
	{% if paper.container-title %} {{ paper.container-title }}. {% endif %}
	{% if paper.published %}
	{% if paper.editor %}
	  Editors
	  {% for e in paper.editor %}
	    {{ e['given'] }} {{ e['dropping-particle'] }} {{ e['family'] }}{% if forloop.last %}.{% else %}, {% endif %} 
	  {% endfor %}
	<br>
	{% endif %}
	{% if paper.journal %} {{ paper.journal }}. {% endif %}
	{% if paper.collection-title %} {{ paper.collection-title }}, {% endif %}
	{% if paper.volume %}Volume {{ paper.volume }}{% if paper.issue %} ({{ paper.issue }}){% endif %},{% endif%}
	{% if paper.pages %} {{ paper.pages }}, {% endif %}
	{{ paper.year }}.
	{% if paper.URL %} <a href="{{ paper.URL }}" target="new"><i class="fa fa-link"></i></a> {% endif %}
	{% else %}
	{% if paper.journal %} {{ paper.journal }}. {% endif %}
	{% if paper.collection-title %} {{ paper.collection-title }}. {% endif %}
	{% if paper.note %}{{ paper.note }}.{% else %}To appear.{% endif%}
	{% endif %}
   </article>
  {% endfor %}
  
  <h1>Unpublished Manuscripts</h1>

{% assign sub = site.submitted %}

<div class="paper-list">
  {% for paper in sub %}
	<strong>{{ paper.title }}</strong>
	{% for a in paper.author %}
	  {{ a }}, 
	{% endfor %}
	<br/>
    {{ paper.note }}
	{% if paper.wps %} <span style="color:#f98811">(WP {% for w in paper.wps %} {{ w }}{% if forloop.last %}) <span style="color:#11bbff">{% for p in paper.partner %}{{ p }}{% if forloop.last %}{% else %}, {% endif %} {% endfor %}</span>{% else %}, {% endif %}{% endfor %}</span>{% endif %}
  {% endfor%}
</div>