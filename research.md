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
  Dark matter (DM) is an unseen component of the universe that accounts for approximately 27%
  of its total mass-energy content. It neither emits nor absorbs light, making it detectable
  solely through its gravitational influence on visible structures such as galaxies and galaxy
  clusters. The first indication of dark matter emerged in the 1930s, when astronomer
  <a href="https://ned.ipac.caltech.edu/level5/March17/Zwicky/translation.pdf"
     target="_blank" rel="noopener">Fritz Zwicky</a> found that galaxies in the Coma Cluster
  moved far faster than the visible mass could explain. Subsequent work on galactic rotation
  curves — most famously by Rubin and Ford — confirmed that stars at the outskirts of galaxies
  orbit too rapidly to be bound by Newtonian gravity if only luminous matter is present. Lensing
  observations, the cosmic microwave background (CMB), and the Bullet Cluster together place the
  existence of dark matter on firm empirical ground.
</p>

<p>
  Despite this observational consensus, the particle nature of dark matter remains unknown. No
  confirmed direct detection has been made through any non-gravitational channel. The standard
  theoretical framework, Lambda-Cold Dark Matter (&Lambda;CDM), reproduces large-scale structure
  with impressive accuracy yet faces persistent tensions on small scales: the missing satellite
  problem, the too-big-to-fail problem, and the cusp-core problem. These tensions motivate
  alternatives such as self-interacting dark matter (SIDM), warm dark matter (WDM), and Fuzzy
  Dark Matter (FDM). My current research focuses on FDM, also known as ultralight dark matter
  (UDM), Bose-Einstein condensate dark matter (BECDM), and scalar field dark matter (SFDM). In
  this model the dark matter particle is an ultralight boson with a mass of order
  10<sup>-22</sup> eV/c<sup>2</sup>, giving it a de Broglie wavelength on kiloparsec scales and
  producing wave-like quantum phenomena inside dark matter halos. On large scales FDM recovers
  the &Lambda;CDM predictions, while on small scales quantum pressure suppresses low-mass halo
  formation and generates a distinct solitonic core at each halo centre — a signature my
  simulation work aims to characterise in the dwarf-galaxy mass range.
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
<section id="galaxy-formation" class="research-section flip">
  <div class="content">
    <h2>Galaxy Formation and Evolution</h2>

    <p>
  Galaxy formation began as tiny quantum density fluctuations in the early universe grew under
  gravity into dark matter halos, which then provided potential wells for baryonic gas to
  collapse, cool, and form stars
  <a href="https://doi.org/10.1093/mnras/183.3.341" target="_blank" rel="noopener">
  (White &amp; Rees, 1978)</a>. This hierarchical assembly process, in which smaller structures
  merge over billions of years to produce larger ones, accounts for the broad diversity of
  galaxy morphologies observed today. Yet important questions about the initial conditions and
  the feedback processes that shape a galaxy's final structure remain open
  <a href="https://doi.org/10.1146/annurev-astro-082812-140951" target="_blank" rel="noopener">
  (Somerville &amp; Davé, 2015)</a>.
</p>

<p>
  Dwarf galaxies, which span roughly 10<sup>7</sup> to 10<sup>10</sup> solar masses in stellar
  content, are the most numerous galaxies in the universe and serve as the primary testing
  ground for dark matter models on small scales. Cold dark matter simulations predict far more
  low-mass satellite halos than are observed around hosts like the Milky Way — the missing
  satellites problem
  <a href="https://doi.org/10.1146/annurev-astro-091916-055313" target="_blank" rel="noopener">
  (Bullock &amp; Boylan-Kolchin, 2017)</a> — and they predict cuspy central density profiles
  that observations of dwarf spheroidals favour as flat cores, the so-called cusp-core problem
  <a href="https://doi.org/10.1088/0004-637X/742/1/20" target="_blank" rel="noopener">
  (Walker &amp; Pe&ntilde;arrubia, 2011)</a>. My current project uses FDM cosmological
  simulations, run with GAMER-2 and GIZMO, to study halos in the mass range
  10<sup>9</sup>-10<sup>10</sup> M<sub>&#9737;</sub>. Initial conditions are generated with
  MUSIC and axionCAMB, and dark matter halos are identified and characterised with the
  phase-space halo finder Rockstar. By comparing FDM and N-body (CDM-like) runs at matched
  resolution in this dwarf-galaxy regime, I aim to quantify the degree to which quantum
  pressure and soliton cores relieve the small-scale tensions that &Lambda;CDM cannot resolve.
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
    
    <video controls preload="metadata" poster="{{ '/assets/Images/galaxy_formation1.webp' | relative_url }}" 
        style="margin-top:12px; width:100%; max-width:100%; display:block; aspect-ratio:16/9;">
      <source src="{{ '/assets/Videos/Data_Proj_z_density_x9.mp4' | relative_url }}" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    

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
      Gravitational wave detectors like LIGO, Virgo, and KAGRA are highly sensitive instruments designed to measure incredibly faint spacetime distortions caused by astrophysical events.  Their sensitivity, however, also increases the likelihood that they will pick up glitches, which are temporary noise artifacts. A number of factors, such as seismic activity, thermal fluctuations, electronic noise, and human-induced disturbances, can produce glitches, which are short-duration, non-astrophysical signals <a href="https://iopscience.iop.org/article/10.3847/2041-8205/833/1/L1" target="_blank" rel="noopener">(Abbott et al., 2016)</a>. It can be difficult to identify and analyze events like binary mergers or supernovae because of these noise artifacts, which can hide or mimic real gravitational wave signals across a wide range of time-frequency characteristics <a href="https://iopscience.iop.org/article/10.1088/1361-6382/34/3/034002" target="_blank" rel="noopener">(Powell et al., 2016)</a>. Fixing this problem is essential since errors obscure signals and raise the false alarm rate, lowering the statistical confidence of detections <a href="https://arxiv.org/abs/2105.10522" target="_blank" rel="noopener">(Mogushi, 2021)</a>.
    </p>

    <p>
      A mix of subtraction, classification, and detection methods are used to try to mitigate glitches. Currently, there are some methods that are working to mitigate glitches, which is summarized in <a href="https://arxiv.org/abs/2406.01318" target="_blank" rel="noopener">this paper</a>. Convolutional neural networks, a machine learning technique, have been used to categorize glitches and differentiate them from astrophysical signals <a href="https://www.sciencedirect.com/science/article/pii/S0370269317310390?via%3Dihub" target="_blank" rel="noopener">(George & Huerta, 2018)</a>. In order to identify glitches based on their spectral signatures, time-frequency domain analytic methods such as the Wavelet Detection Filter are also employed <a href="https://iopscience.iop.org/article/10.1088/0264-9381/21/20/024" target="_blank" rel="noopener">(Chatterji et al., 2004)</a>. Techniques like Bayesian inference allow for precise noise modeling and signal reconstruction, as demonstrated in the Bayesian framework for glitch subtraction <a href="https://journals.aps.org/prd/abstract/10.1103/PhysRevD.91.084034" target="_blank" rel="noopener">(Cornish & Littenberg, 2015)</a>. Among these, I worked on <a href="https://iopscience.iop.org/article/10.1088/1361-6382/acd0fe/meta" target="_blank" rel="noopener">the adaptive spline fitting method</a> for its ability to model glitches flexibly without requiring strong assumptions about their structure. However, challenges remain, particularly in automating these methods for real-time applications, optimizing parameters to avoid overfitting, and handling overlapping glitches and astrophysical signals.
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

<!-- ========== Software ========== -->
<section id="software" class="research-section">
  <div class="content">
    <h2>Software</h2>

    <h3>PHANTOM</h3>
    <p>
      A recurring challenge in dark matter research is that validated, native implementations
      of halo statistics and density profile models are largely absent from the MATLAB and
      Octave ecosystems, despite widespread use of these environments in astrophysics pipelines.
      To address this, I have published
      <a href="https://arxiv.org/abs/2606.19104" target="_blank" rel="noopener">PHANTOM</a>
      (Profile and Halo Analysis for Numerous Theoretical dark Matter Observables), an
      open-source MATLAB toolbox and Octave package that connects linear density field
      statistics to dark matter halo observables. PHANTOM can also run in Python through an
      Octave kernel, making it accessible across computing environments. The code is released
      under the MIT licence and is publicly available on
      <a href="https://github.com/matc-thaher/PHANTOM" target="_blank" rel="noopener">GitHub</a>.
    </p>

    <p>
      The package combines a flexible cosmology module with linear power spectrum, variance,
      and correlation function solvers alongside a halo module covering mass functions, linear
      bias, density profiles, and concentration-mass relations for cold, warm, and fuzzy dark
      matter scenarios. All core routines are cross-validated against the Python packages
      colossus, hmf, and halomod, with sub-percent agreement across shared models including
      distances, power spectra, halo mass functions, and density profiles. From a single
      cosmology structure object, users can obtain field statistics, halo statistics, and halo
      observables — including enclosed mass, circular velocity, projected density, and lensing
      convergence — on arbitrary user-defined grids. Full documentation and usage examples are
      on my <a href="{{ '/code/' | relative_url }}">Code Projects</a> page, or read the paper
      at <a href="https://arxiv.org/abs/2606.19104" target="_blank" rel="noopener">arXiv:2606.19104</a>.
    </p>

<!-- Quote moved to the bottom only -->
<aside class="prose quote-callout">
  <em>{{ page.header_phrase }}</em>
</aside>

