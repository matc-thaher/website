---
layout: default
title: Research
permalink: /research/
header_phrase: "Study hard what interests you the most in the most undisciplined, irreverent, and original manner possible. - Richard Feynman"
show_header_phrase: false
---

<h1>Research</h1>

<p>My primary research area involves investigating the properties and interactions of dark matter. Here are some ongoing projects:</p>

<!-- ========== Topic 1: text left | media right ========== -->
<section class="research-section">
  <div class="content">
    <h2>Dark Matter</h2>

    <p>
      Dark matter (DM) is a mysterious, non-luminous component that makes up ~27% of the Universe’s
      mass–energy. It’s observed through gravity—galaxy rotation curves, cluster dynamics,
      lensing—not through direct emission/absorption. Early evidence traces back to
      <a href="https://ned.ipac.caltech.edu/level5/March17/Zwicky/translation.pdf" target="_blank" rel="noopener">Zwicky’s Coma Cluster</a>
      and the flat rotation curves of disk galaxies.
    </p>

    <p>
      ΛCDM remains successful on large scales but faces small-scale tensions
      (missing satellites, too-big-to-fail, cusp–core). Alternative models include SIDM, WDM, and
      fuzzy/ultralight dark matter (FDM/UDM/BECDM/SFDM). I’m currently exploring FDM’s potential to
      reconcile small-scale structure while matching large-scale success.
    </p>
  </div>

  <div class="media">
    <figure style="margin:0 0 12px 0">
      <img src="{{ '/assets/Images/DM_existence.jpg' | relative_url }}" alt="Evidence for dark matter overview" loading="lazy">
      <figcaption class="badge" style="display:inline-block; margin-top:6px;">
        Evidence overview — source:
        <a href="https://www.anl.gov/science-101/dark-matter-and-dark-energy" target="_blank" rel="noopener">Argonne National Laboratory</a>
      </figcaption>
    </figure>

    <figure style="margin:0">
      <img src="{{ '/assets/Images/DM_simulation.webp' | relative_url }}" alt="Dark matter simulations across models" loading="lazy">
      <figcaption class="badge" style="display:inline-block; margin-top:6px;">
        Simulations across DM models — source:
        <a href="https://link.springer.com/article/10.1007/s41115-021-00013-z" target="_blank" rel="noopener">Springer review</a>
      </figcaption>
    </figure>
  </div>
</section>

<!-- ========== Topic 2: media left | text right (.flip) ========== -->
<section class="research-section flip">
  <div class="content">
    <h2>Galaxy Formation</h2>

    <p>
      Galaxies form within dark matter halos seeded by primordial fluctuations. Gas cooling,
      angular-momentum transport, star formation, and feedback sculpt the Hubble sequence.
      Key open questions remain on how initial conditions and merger histories set final structure
      and how baryonic processes reshape inner halo profiles.
    </p>

    <p>
      Dwarf galaxies, as laboratories of high DM fractions, highlight small-scale tensions such as
      the core–cusp and missing-satellites problems. My work examines whether FDM’s wave support and
      soliton–halo coupling can mitigate these while remaining consistent with large-scale statistics.
    </p>
  </div>

  <div class="media">
    <!-- IMAGE OPTION (default) -->
    <figure style="margin:0 0 12px 0">
      <img src="{{ '/assets/Images/galaxy_formation1.webp' | relative_url }}" alt="Galaxy formation schematic 1" loading="lazy">
      <figcaption class="badge" style="display:inline-block; margin-top:6px;">
        Galaxy components — source:
        <a href="https://www.nature.com/articles/490024a" target="_blank" rel="noopener">Nature</a>
      </figcaption>
    </figure>

    <figure style="margin:0">
      <img src="{{ '/assets/Images/galaxy_formation2.webp' | relative_url }}" alt="Galaxy formation schematic 2" loading="lazy">
      <figcaption class="badge" style="display:inline-block; margin-top:6px;">
        Formation processes — source:
        <a href="https://www.nature.com/articles/490024a" target="_blank" rel="noopener">Nature</a>
      </figcaption>
    </figure>

    <!-- VIDEO OPTIONS (uncomment ONE when you have media) -->

    <!-- Local video -->
    <!--
    <video controls preload="metadata" poster="{{ '/assets/Images/galaxy_formation1.webp' | relative_url }}" style="margin-top:12px">
      <source src="{{ '/assets/videos/galaxy_overview.mp4' | relative_url }}" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    -->

    <!-- YouTube/Vimeo embed -->
    <!--
    <iframe
      src="https://www.youtube.com/embed/VIDEO_ID?rel=0"
      title="Galaxy formation overview"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      allowfullscreen
      style="margin-top:12px">
    </iframe>
    -->
  </div>
</section>

<!-- ========== Topic 3: text left | media right ========== -->
<section class="research-section">
  <div class="content">
    <h2>Gravitational-Wave Data Analysis</h2>

    <p>
      Interferometers (LIGO/Virgo/KAGRA) are exquisitely sensitive—and susceptible to short,
      non-astrophysical transients (glitches). I work on methods to model and subtract these
      artifacts (adaptive splines, wavelet-based denoising), preserving compact-binary signals and
      improving detection confidence.
    </p>

    <p>
      I focus on reproducible pipelines, uncertainty tracking, and practical deployment on
      publicly-available datasets. This includes comparisons against CNN-based classifiers and
      Bayesian noise-modeling approaches.
    </p>
  </div>

  <div class="media">
    <figure style="margin:0">
      <img src="{{ '/assets/Images/glitch_GW170817.png' | relative_url }}" alt="Glitch subtraction on GW170817 (BNS)" loading="lazy">
      <figcaption class="badge" style="display:inline-block; margin-top:6px;">
        Glitch subtraction on GW170817 — from
        <a href="https://www.proquest.com/openview/7f68a2c9fc2972f4eb08e0d1a8fcbd2e/1?cbl=18750&diss=y&pq-origsite=gscholar" target="_blank" rel="noopener">Master’s thesis</a>
      </figcaption>
    </figure>
  </div>
</section>

<p>More details on specific projects can be found in my <a href="{{ '/code/' | relative_url }}">Code Projects</a> section.</p>

<!-- Quote moved to the bottom only -->
<aside class="prose quote-callout">
  <em>{{ page.header_phrase }}</em>
</aside>

