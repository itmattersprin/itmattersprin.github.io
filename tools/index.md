---
layout: index
content: true
docs_list_title: Events
use-site-title: false
---

{% assign items = site.toolkits | sort: 'name' %}

<h1> Tools </h1>

<!--p>
VoxLogicA: the Voxel-based Logical Analyser. VoxLogicA is a model checker dedicated to classifying pixels/voxels in 2D/3D images, based on their spatial logical properties, such as proximity, distance, reachability, texture, colour, etc. 
</p>
<p>Github: <a href="https://www.github.com/vincenzoml/voxlogica">www.github.com/vincenzoml/voxlogica</a></p>
<p>Official site: <a href="https://www.voxlogica.org">www.voxlogica.org</a></p-->


<div class="tools-list">
  {% for n in items %}
    <h2> {{ n.name }}</h2>
    <p>{{ n.description }}
		<!--{% if n.url %}<br/>Available <a href="{{ n.url }}">here</a> {% endif %}-->
		{% if n.github %}<br/>Available <a href="{{ n.github }}">here</a> {% endif %}
		{% if n.website %}<br/>Website <a href="{{ n.website }}">here</a> {% endif %}
		{% if n.contact %}<br/><a href="mailto:{{ n.contact }}">Contact</a>. {% endif %}
    </p>
  {% endfor %}
</div>
