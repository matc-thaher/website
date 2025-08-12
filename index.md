---
layout: default
title: Home
permalink: /
header_phrase: "Consider well the seed that gave you birth: You were not made to live like brutes, but to follow virtue and knowledge. - Dante (Inferno)"
---

<!-- HERO -->
<section style="display:grid; grid-template-columns: minmax(0,1fr) 420px; gap: 24px; align-items:center; margin: 24px 0;">
  <div>
    <span style="display:inline-block; padding:.3rem .6rem; border-radius:999px; border:1px solid var(--ring, rgba(0,122,204,.25)); color: var(--muted, #6b7280); font-size:.95rem; margin-bottom:.6rem;">
      PhD @ RPI · Cosmology
    </span>
    <h1 style="margin:.2rem 0 0;">Mohammad Abu Thaher Chowdhury</h1>
    <div class="prose">
      <p style="margin: .75rem 0 1rem;">
        I explore fuzzy/ultralight dark matter, galaxy formation, and glitch-resilient data analysis.
        Browse my research, publications, and open-source code—or reach out to collaborate.
      </p>
    </div>
    <div style="display:flex; gap:.6rem; flex-wrap:wrap;">
      <a class="button" href="{{ '/research/' | relative_url }}">View Research</a>
      <a class="button" href="{{ '/publications/' | relative_url }}">Publications</a>
      <a class="button" href="{{ '/code/' | relative_url }}">Code</a>
    </div>
  </div>

  <div>
    <img src="{{ '/assets/Images/NGC6217.jpg' | relative_url }}" alt="NGC 6217 galaxy" loading="lazy">
  </div>
</section>

<!-- GALLERY -->
<h2>Gallery</h2>
<div class="image-gallery">
  <figure>
    <img src="{{ '/assets/Images/DM_ring_galxycluster.jpg' | relative_url }}" alt="Ring galaxy cluster" loading="lazy">
    <figcaption class="badge">Ring galaxy cluster</figcaption>
  </figure>
  <figure>
    <img src="{{ '/assets/Images/NGC6217.jpg' | relative_url }}" alt="NGC 6217" loading="lazy">
    <figcaption class="badge">NGC 6217</figcaption>
  </figure>
  <figure>
    <img src="{{ '/assets/Images/heic1315a.jpg' | relative_url }}" alt="Galaxy cluster" loading="lazy">
    <figcaption class="badge">Galaxy cluster</figcaption>
  </figure>
</div>

<!-- NEWS -->
<h2>Recent News</h2>
<ul>
  <li><strong>May 2025</strong> — Launched this personal website!</li>
</ul>

<div class="prose" style="margin-top: 1rem;">
  <p>For more about my background and current projects, visit the <a href="{{ '/about/' | relative_url }}">About Me</a> page.</p>
</div>

<!-- OPTIONAL: Echo the long header phrase at the bottom as a callout -->
<aside class="prose" style="margin-top:20px; padding:12px 16px; border-left:4px solid var(--brand, #007acc); background: var(--panel, #fff); border-radius:8px; color: var(--muted, #6b7280);">
  <em>“Consider well the seed that gave you birth: You were not made to live like brutes, but to follow virtue and knowledge.” — Dante, <span style="font-style:italic;">Inferno</span></em>
</aside>


