---
layout: default
title: Code
permalink: /code/
header_phrase: "What we observe is not nature itself, but nature exposed to our method of questioning. — Werner Heisenberg"
show_header_phrase: false
---

<h1>Scientific Code & Projects</h1>

<p>Links to my research code and tools. “Featured” highlights a few active projects; the full list below updates automatically from GitHub.</p>

<!-- ========= Featured (curate these) ========= -->
<h2>Featured</h2>
<div class="project-grid">
  <article class="project-card">
    <h3><a href="https://github.com/matc-thaher/dark-matter-simulations" target="_blank" rel="noopener">Dark Matter Simulations</a></h3>
    <p>Scripts and analysis pipelines to explore ultralight/FDM cores, core–halo scaling, and rotation-curve fits.</p>
    <div class="project-meta">
      <span class="tag">Python</span>
      <span class="tag">Astro</span>
      <a class="badge-link" href="https://github.com/matc-thaher/dark-matter-simulations" target="_blank" rel="noopener">Repo →</a>
    </div>
  </article>

  <article class="project-card">
    <h3><a href="https://github.com/matc-thaher/gravitational-wave-analysis" target="_blank" rel="noopener">Gravitational-Wave Analysis</a></h3>
    <p>Adaptive spline fitting + wavelet shrinkage for glitch suppression; reproducible workflows on open LIGO/Virgo data.</p>
    <div class="project-meta">
      <span class="tag">Python</span>
      <span class="tag">Signal Proc</span>
      <a class="badge-link" href="https://github.com/matc-thaher/gravitational-wave-analysis" target="_blank" rel="noopener">Repo →</a>
    </div>
  </article>
</div>

<!-- ========= All repositories (auto) ========= -->
<h2>All repositories</h2>

{% assign repos = site.data.repos.repos | where_exp: "r", "r.fork == false" %}
{% assign repos = repos | sort: "stargazers_count" | reverse %}

{% if repos and repos.size > 0 %}
<div class="project-grid">
  {% for r in repos %}
  <article class="project-card">
    <h3><a href="{{ r.html_url }}" target="_blank" rel="noopener">{{ r.name }}</a></h3>
    <p>{{ r.description }}</p>
    <div class="project-meta">
      {% if r.language %}<span class="tag">{{ r.language }}</span>{% endif %}
      {% if r.topics %}{% for t in r.topics limit:3 %}<span class="tag">{{ t }}</span>{% endfor %}{% endif %}
      <span class="muted">★ {{ r.stargazers_count }}</span>
      <span class="muted">Updated {{ r.updated_at | date: "%b %Y" }}</span>
    </div>
  </article>
  {% endfor %}
</div>
<p class="pub-updated"><em>Last synced: {{ site.data.repos.updated | date: "%B %d, %Y" }}</em></p>
{% else %}
<p><em>GitHub data isn’t loaded yet—showing hand-picked projects above.</em></p>
{% endif %}

<!-- Quote only at the bottom -->
<aside class="prose quote-callout" style="margin-top:24px;">
  <em>{{ page.header_phrase }}</em>
</aside>
