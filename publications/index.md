---
layout: index
content: true
docs_list_title: Publications
use-site-title: false
---


# Publications
Click [here](bysite) to sort by partners.

{% assign items = site.papers | sort: 'year' | reverse %}

{% assign lastyear = 9999 %}

<div class="paper-list">
  {% for paper in items %}
  {% if paper.year != lastyear %}<h2> {{ paper.year }}</h2>{% endif %}
  {% assign lastyear = paper.year %}
  <article class="paper-preview">
	<strong>{{ paper.title }}</strong>
	{% if paper.wps %}
    <span style="color:#f98811">({% for w in paper.wps %}WP{{w}}{% if forloop.last %}{% else %}, {% endif %}{% endfor %})</span>
  {% endif %}
  {% if paper.partner %}
    <span style="color:#11bbff">
  {% for p in paper.partner %}{{ p }}{% if forloop.last %}{% else %}, {% endif %} {% endfor %}
  </span>
  {% endif %}
	<br>
  <em>
	{% for a in paper.author %}
	  {{ a }}{% if forloop.last %}.{% else %}, {% endif %}
	{% endfor %}
  </em>
	<br>
	{% if paper.container-title %} {{ paper.container-title }}. {% endif %}
	{% if paper.published %}
	{% if paper.editor %}
	  Editors
	  {% for e in paper.editor %}
	    {{ e }}{% if forloop.last %}.{% else %}, {% endif %}
	  {% endfor %}
	<br>
	{% endif %}
	{% if paper.journal %} {{ paper.journal }}. {% endif %}
	{% if paper.collection-title %} {{ paper.collection-title }}, {% endif %}
  {% if paper.series %} {{ paper.booktitle }} {{ paper.series }}, {% else %} {{ paper.booktitle }}, {% endif %}
	{% if paper.volume %}Volume {{ paper.volume }}{% if paper.issue %} ({{ paper.issue }}){% endif %},{% endif%}
	{% if paper.pages %} {{ paper.pages }}, {% endif %}
	{{ paper.year }}.
	{% if paper.URL %} <a href="{{ paper.URL }}" target="new"><i class="fa fa-link"></i></a> {% endif %}
	<br/>
		  {% if paper.oalink %}<a href="{{ paper.oaline }}">
	  {% if paper.oa %}Open Access: {{ paper.oa }}{% else %}{{ paper.oalink }}{% endif %}</a>{% endif %}
	{% else %}
	{% if paper.journal %} {{ paper.journal }}. {% endif %}
	{% if paper.collection-title %} {{ paper.collection-title }}. {% endif %}
	{% if paper.note %}{{ paper.note }}.{% else %}boom {{paper.title}}To appear.{% endif%}
	{% endif %}
   </article>
   <br/>
  {% endfor %}
</div>


# Unpublished Manuscripts

{% assign sub = site.submitted %}

<div class="paper-list">
  {% for paper in sub %}
  <article>
	<strong>{{ paper.title }}</strong>
	<br/>
	{% for a in paper.author %}
	  {{ a }}{% if forloop.last %}.{% else %}, {% endif %}
	{% endfor %}
	<br/>
    {{ paper.note }}
	{% if paper.wps %} <span style="color:#f98811">({% for w in paper.wps %}WP{{w}}{% if forloop.last %}) <span style="color:#11bbff">{% for p in paper.partner %}{{ p }}{% if forloop.last %}{% else %}, {% endif %} {% endfor %}</span>{% else %}, {% endif %}{% endfor %}</span>{% endif %}
  </article>
  <br/>
  {% endfor%}
</div>
