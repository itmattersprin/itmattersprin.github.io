---
layout: index
content: true
docs_list_title: Publications
use-site-title: false
---

<h1>Talks & presentations</h1>
<h2>Internal Talks</h2>
{% assign items = site.talks | sort: 'date' | reverse %}
{% for n in items %}
<div class="talk-list">
- {{ n.title }}
  <span markdown="1" style="font-size:.75em"><br/>{{ n.speaker }}. {{ n.date | date: '%B %d, %Y' }}.
  {% if n.slides %}[Slides](talks/{{ n.slides }}){% endif %}</span>{% endfor %}
</div>

<h2>Outreach & dissemination talks</h2>
{% assign invited = site.data.invited | sort: 'date' | reverse %}
{% for n in invited %}
- {{ n.title }}
  <br/>
  <span markdown="1" style="font-size:.75em">{{ n.speaker}}. {{ n.date | date: '%B %d, %Y'}}.
  {% if n.slides %}[Slides](invited_talks/{{ n.slides }}){% endif %}</span><br/>{% endfor %}
