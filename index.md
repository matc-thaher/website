---
layout: default
title: Home
permalink: /
show_header_phrase: false
---

<section class="home-hero">
  <div>
    <span class="tagline-chip">PhD Researcher @ RPI · Cosmology · Scientific Computing</span>

    <h1>Mohammad Abu Thaher Chowdhury</h1>

    <p>
      I study dark matter and galaxy formation through theoretical and
      computational astrophysics. My current work examines fuzzy dark matter
      in dwarf-galaxy halos through cosmological simulations, numerical data
      analysis, and open-source scientific software. I also work on
      gravitational-wave data analysis and quantum-computing approaches to
      physics and simulation.
    </p>

    <div class="hero-cta">
      <a class="button" href="{{ '/research/' | relative_url }}">View Research</a>
      <a class="button" href="{{ '/publications/' | relative_url }}">Publications</a>
      <a class="button" href="{{ '/code/' | relative_url }}">Code</a>
      <a class="button" href="{{ '/assets/CV.pdf' | relative_url }}" target="_blank" rel="noopener">CV</a>
    </div>
  </div>

  <div>
    <img
      src="{{ '/assets/Images/FDM_Halo1.png' | relative_url }}"
      alt="Projected fuzzy dark matter halo density from a cosmological simulation"
      loading="lazy">
  </div>
</section>

## Current Work

I am investigating fuzzy dark matter structure formation in dwarf-galaxy halos
with masses of approximately 10<sup>9</sup> to 10<sup>10</sup> solar masses.
My workflow combines FDM simulations with GAMER-2, N-body comparison
simulations with GIZMO, initial conditions generated with MUSIC and axionCAMB,
and halo characterization with Rockstar.

This work brings together numerical simulation, data processing, halo analysis,
reproducible scientific software, and computational methods relevant to both
astrophysics research and data-intensive technical roles.

<p>
  <a href="{{ '/research/#galaxy-formation' | relative_url }}">Research overview</a>
  ·
  <a href="https://github.com/matc-thaher/PHANTOM" target="_blank" rel="noopener">PHANTOM software</a>
  ·
  <a href="https://github.com/matc-thaher/GW_Glitch_Identification_Subtraction" target="_blank" rel="noopener">GW glitch analysis code</a>
</p>

## Gallery

<div class="image-gallery">
  <figure>
    <img
      src="{{ '/assets/Images/FDM_Halo1.png' | relative_url }}"
      alt="Projected fuzzy dark matter halo density from a cosmological simulation"
      loading="lazy">
    <figcaption class="badge">
      Fuzzy dark matter halo density field
    </figcaption>
  </figure>

  <figure>
    <video
      controls
      preload="metadata"
      poster="{{ '/assets/Images/FDM_Halo1.png' | relative_url }}"
      style="width:100%; display:block; aspect-ratio:16/9; object-fit:cover;">
      <source
        src="{{ '/assets/Videos/Data_Proj_y_density_x10.mp4' | relative_url }}"
        type="video/mp4">
      Your browser does not support the video tag.
    </video>
    <figcaption class="badge">
      Fuzzy dark matter density evolution from a GAMER-2 simulation
    </figcaption>
  </figure>

  <figure>
    <img
      src="{{ '/assets/Images/DM_ring_galxycluster.jpg' | relative_url }}"
      alt="Ring galaxy cluster observed through gravitational lensing"
      loading="lazy">
    <figcaption class="badge">
      Ring galaxy cluster
    </figcaption>
  </figure>
</div>

## Recent News

- **August 2026** — Archived my open-source [gravitational-wave glitch identification and subtraction code](https://zenodo.org/records/22165032) on Zenodo.
- **August 2026** — Earned IBM's Road to Practitioner badge, recognizing advanced Qiskit proficiency in variational algorithms, quantum machine learning, and hardware-efficient workflows.
- **April 2026** — Released [**PHANTOM**](https://github.com/matc-thaher/PHANTOM), an open-source MATLAB and GNU Octave package for dark matter halo analysis. [Paper](https://arxiv.org/abs/2606.19104) · [Software releases](https://github.com/matc-thaher/PHANTOM/releases/latest)
- **September 2025** — Became an IBM Qiskit Advocate.
- **August 2025** — Completed IBM's summer program in Quantum Computing and Quantum Information.
- **May 2025** — Launched this personal website.

For more about my academic background, research trajectory, and current projects,
visit the [About Me]({{ '/about/' | relative_url }}) page.

<aside class="prose quote-callout" markdown="1">
_“Consider well the seed that gave you birth: You were not made to live like brutes, but to follow virtue and knowledge.” — Dante, *Inferno*_
</aside>
