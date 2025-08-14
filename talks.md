---
layout: default
title: Talks
permalink: /talks/
header_phrase: "Every great and deep difficulty bears in itself its own solution. It forces us to change our thinking in order to find it. — Niels Bohr"
show_header_phrase: false
---

<h1>Talks & Presentations</h1>

<p>Invited talks, conference presentations, seminars, and posters. Items are grouped by year. Manual entries are the source of truth; automated imports (when enabled) will only add missing items.</p>

{% assign talks = site.data.talks.items | sort: "date" | reverse %}
{% if talks and talks.size > 0 %}
  {% assign last_year = "" %}
  {% for t in talks %}
    {% assign y = t.date | date: "%Y" %}
    {% if y != last_year %}
      <h2 class="talk-year">{{ y }}</h2>
      {% assign last_year = y %}
    {% endif %}

    <article class="talk-item">
      <div class="talk-header">
        <span class="talk-type">{{ t.type | default: "Talk" }}</span>
        <h3 class="talk-title">{{ t.title }}</h3>
      </div>
      <div class="talk-meta">
        {% if t.event %}<span class="muted">{{ t.event }}</span>{% endif %}
        {% if t.location %}<span class="muted">· {{ t.location }}</span>{% endif %}
        {% if t.date %}<span class="muted">· {{ t.date | date: "%b %-d, %Y" }}</span>{% endif %}
      </div>
      {% if t.coauthors %}<div class="talk-coauthors">With {{ t.coauthors }}</div>{% endif %}
      {% if t.notes %}<p class="talk-notes">{{ t.notes }}</p>{% endif %}
      <div class="talk-links">
        {% if t.url %}<a class="badge-link" href="{{ t.url }}" target="_blank" rel="noopener">Event</a>{% endif %}
        {% if t.slides %}<a class="badge-link" href="{{ t.slides }}" target="_blank" rel="noopener">Slides</a>{% endif %}
        {% if t.poster %}<a class="badge-link" href="{{ t.poster }}" target="_blank" rel="noopener">Poster</a>{% endif %}
        {% if t.video %}<a class="badge-link" href="{{ t.video }}" target="_blank" rel="noopener">Video</a>{% endif %}
      </div>
    </article>
  {% endfor %}

  <p class="pub-updated"><em>Last updated: {{ site.data.talks.updated | date: "%B %d, %Y" }}</em></p>
{% else %}
  <p>No talks listed yet.</p>
{% endif %}

<!-- Quote only at the bottom -->
<aside class="prose quote-callout" style="margin-top:24px;">
  <em>{{ page.header_phrase }}</em>
</aside>
