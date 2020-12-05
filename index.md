---
layout: index
content: true
---

# {{ site.title}}

<table>
  <tr>
    <th style="width:85; text-align:left"></th>
    <th style="width:15%; text-align:left"></th>
  </tr>
  <tr>
    <td valign="top" markdown="1" style="padding-right: 50px;">
## {{ site.subtitle}}
The goal of the {{ site.title }} is the development and the experimentation
of a novel methodology for the specification, implementation and
validation of trustworthy [smart systems](description/smart.html) based on formal
methods. We envisage system development in three steps by first
providing and analysing system models to find design errors, then
moving from models to executable code by translation into
domain-specific programming languages and, finally, monitoring runtime
execution to detect anomalous behaviours and to support systems in
taking context-dependent decisions autonomously.
More details about  {{ site.title }} are [here](description).
</td>
    <td valign="top" markdown="1" style="padding-right: 50px;">
## News
<div markdown="1" class="scroll">
<li>{% assign items = site.newsIT %}
{% for n in items reversed %}
{% if forloop.index <= 10 %}
<b>{{ n.date  | date: '%B %d, %Y' }}</b>: {{ n.descr }} {% if n.link %} see <a href="{{ n.link }}" target="_blank">here</a>
{% endif %}
<hr>
{% else %} {% break %} {% endif%}
{% endfor %}
</li>
</div>
</td>
</tr>
</table>

