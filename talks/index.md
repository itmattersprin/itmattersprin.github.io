---
layout: index
content: true
docs_list_title: Publications
use-site-title: false
---

# Talks & presentations

## Outreach & dissemination talks
{% assign invited = site.data.invited | sort: 'date' | reverse %}
{% for n in invited %}
- **{{ n.title }}**  
  <span markdown="1" style="font-size:.95em"> {{ n.speaker}}.  {{ n.date | date: '%B %d, %Y'}}.<br/> {{ n.descr}}. {% if n.slides %}[Slides](invited_talks/{{ n.slides }}){% endif %}</span><br/>{% endfor %}

## Internal Talks
{% assign items = site.talks | sort: 'date' | reverse %}
{% for n in items %}
- **{{ n.title }}**  
  <span markdown="1" style="font-size:.95em">{{ n.speaker }}. {{ n.date | date: '%B %d, %Y'}}.
  {% if n.slides %}[Slides]({{ n.slides }}){% endif %}</span>{% endfor %}
