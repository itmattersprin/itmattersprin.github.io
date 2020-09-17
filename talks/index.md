---
layout: index
content: true
docs_list_title: Publications
use-site-title: false
---

<h1>Talks & presentations</h1>
{% assign items = site.talks | sort: 'date' | reverse %}
{% for n in items %}
- {{ n.title }}
  <span markdown="1" style="font-size:.75em"><br/>{{ n.speaker }}. {{ n.date | date: '%B %d, %Y' }}. [Slides](talks/{{ n.slides }})</span>{% endfor %}
<div class="talk-list">
</div>
