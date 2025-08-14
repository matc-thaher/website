---
layout: default
title: Contact
permalink: /contact/
header_phrase: "We are a way for the cosmos to know itself. — Carl Sagan"
show_header_phrase: false
---

<h1>Contact</h1>

<section class="contact-grid">
  <div class="content">
    <p>If you’re interested in collaborating or have questions about my research, I’d be happy to hear from you.</p>

    <div class="contact-actions">
      <a class="button" href="mailto:chowdm4@rpi.edu?subject=Hello%20from%20your%20website">Email me</a>
      <button class="button button-secondary" type="button"
        onclick="navigator.clipboard.writeText('chowdm4@rpi.edu'); this.textContent='Copied!'; setTimeout(()=>this.textContent='Copy email', 1400);">
        Copy email
      </button>
    </div>

    <p class="muted" style="margin-top:10px;">I typically respond within a couple of days during the semester.</p>
  </div>

  <div class="contact-card">
    <div class="contact-row">
      <span class="label">Email</span>
      <a href="mailto:chowdm4@rpi.edu">chowdm4@rpi.edu</a>
    </div>

    <div class="contact-row">
      <span class="label">Location</span>
      <a href="https://maps.google.com/?q=Rensselaer%20Polytechnic%20Institute,%20Troy,%20NY" target="_blank" rel="noopener">
        RPI · Troy, NY, USA
      </a>
    </div>

    <div class="socials" style="margin-top:10px;">
      <a href="https://github.com/matc-thaher" aria-label="GitHub" rel="me" target="_blank">
        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true"><path d="M12 .5a12 12 0 0 0-3.79 23.4c.6.11.82-.26.82-.58v-2.2c-3.34.73-4.04-1.61-4.04-1.61-.55-1.41-1.34-1.79-1.34-1.79-1.09-.74.08-.72.08-.72 1.2.08 1.83 1.23 1.83 1.23 1.07 1.83 2.8 1.3 3.48.99.11-.78.42-1.3.77-1.6-2.67-.3-5.47-1.33-5.47-5.9 0-1.3.47-2.37 1.23-3.2-.12-.3-.53-1.52.12-3.17 0 0 1.01-.32 3.3 1.22a11.4 11.4 0 0 1 6.01 0c2.28-1.54 3.29-1.22 3.29-1.22.66 1.65.25 2.87.12 3.17.77.83 1.23 1.9 1.23 3.2 0 4.59-2.81 5.59-5.49 5.89.43.37.82 1.09.82 2.2v3.26c0 .32.21.7.83.58A12 12 0 0 0 12 .5Z"/></svg>
      </a>
      <a href="https://www.linkedin.com/in/thaher608" aria-label="LinkedIn" rel="me" target="_blank">
        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.13 1.45-2.13 2.95v5.66H9.37V9h3.4v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.6 0 4.26 2.37 4.26 5.45v6.29ZM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12Zm-1.78 13.02h3.56V9H3.56v11.45Z"/></svg>
      </a>
      <!-- Add ResearchGate/ORCID here later when you have the exact URLs -->
    </div>
  </div>
</section>

<!-- Quote only at the bottom -->
<aside class="prose quote-callout" style="margin-top:24px;">
  <em>{{ page.header_phrase }}</em>
</aside>
