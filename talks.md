---
layout: default
title: Talks
permalink: /talks/
header_phrase: "Every great and deep difficulty bears in itself its own solution. — Niels Bohr"
show_header_phrase: false
render_with_liquid: true
---

# Talks & Presentations

Invited talks, conference presentations, seminars, and posters. Items are grouped by year. Manual entries are the source of truth; automated imports (when enabled) will only add missing items.

{% assign talks = site.data.talks.items | sort: "date" | reverse %}
{% if talks and talks.size > 0 %}
{% assign last_year = "" %}
{% for t in talks %}

  {%- comment -%}
  Compute a year string:
  1) Prefer t.year if you set it in your data
  2) Else use t.date and force it to a 4-char year by slicing
  {%- endcomment -%}
  {% assign y = t.year | default: t.date | date: "%Y" %}
  {% assign y = y | slice: 0, 4 %}

  **{{ t.title }}**  
  {%- if t.type -%}_{{ t.type }}_ · {%- endif -%}
  {%- if t.event -%}{{ t.event }}{%- endif -%}
  {%- if t.location -%} · {{ t.location }}{%- endif -%}
  {%- if t.date -%} · {{ t.date | date: "%Y" }}{%- endif -%}  
  {%- if t.coauthors -%}_With {{ t.coauthors }}_{%- endif -%}

  {%- if t.url or t.slides or t.poster or t.video -%}
  [Event]({{ t.url }}){%- if t.slides %} · [Slides]({{ t.slides }}){%- endif -%}{%- if t.poster %} · [Poster]({{ t.poster }}){%- endif -%}{%- if t.video %} · [Video]({{ t.video }}){%-    endif -%}
  {%- endif %}

  ---
{% endfor %}
{% else %}
No talks listed yet.
{% endif %}

> _{{ page.header_phrase }}_
