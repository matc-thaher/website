---
layout: default
title: Research
permalink: /research/
header_phrase: "Study hard what interests you the most in the most undisciplined, irreverent, and original manner possible. - Richard Feynman"
---

# Research

My primary research area involves investigating the properties and interactions of dark matter. Here are some ongoing projects:

## Dark Matter

![Dark Matter existence graph](/assets/Images/DM_existence.jpg){: .custom-image3}
![Dark Matter simulation](/assets/Images/DM_simulation.webp){: .custom-image3}


(1st image: Proof of Dark Matter (this image is taken from [Argonne National Laboratory website](https://www.anl.gov/science-101/dark-matter-and-dark-energy)),
2nd image: Dark Matter Simulation based ofn different Dark Matter Theory ( this image is taken from [a paper](https://link.springer.com/article/10.1007/s41115-021-00013-z)))


Dark matter (DM) is a mysterious and unseen matter that makes up approximately 27% of the universe's mass-energy content. It doesn't emit, absorb, or reflect light, making it invisible and detectable only through its gravitational effects on visible matter, such as galaxies and galaxy clusters. The first assumption of dark matter arose in the 1930s when astronomer [Fritz Zwicky](https://ned.ipac.caltech.edu/level5/March17/Zwicky/translation.pdf) observed that galaxies in the Coma Cluster were moving faster than expected based on the visible matter present. This led to the hypothesis that unseen "dark matter" was exerting extra gravitational pull to explain the high velocities. The galactic rotation curve problem in Babcock's observation proved that the stars move too fast to be bound by Newtonian gravity if all matter is visible. Other observations and work have demonstrated that DM exists. However, the nature of DM is still a mystery. How does it interact amongst DM particles and with other baryonic particles? Even if it does interact, which type of interaction is it? If a DM particle exists, does it have a dual nature like a photon?

Despite decades of research, it has not been directly detected through any known particles or interactions outside of its gravitational effects. This discrepancy challenges existing particle physics and cosmology models, leading to ongoing debates and searches for alternative explanations. Until now, the most successful theory is Lambda—Cold Dark Matter (ΛCDM) theory, which can not explain the small-scale problems that arose from the theoretical model, like the missing satellite problem, too-big-to-fail problem, and cusp-core problem. There are other models, such as self-interacting dark matter (SIDM), fuzzy dark matter (FDM), and warm dark matter (WDM). I am currently investigating FDM, which is also known as Ultralight Dark Matter (UDM), Bose-Einstein condensate Dark Matter (BECDM), quantum Dark Matter, and Scalar Field Dark Matter (SFDM). This model may help solve the small-scale cosmology problem that Lambd-CDM can not solve.

## Galaxy Formation

![Galaxy formation 1](/assets/Images/galaxy_formation1.webp){: .custom-image3}
![Galaxy Formation 2](/assets/Images/galaxy_formation2.webp){: .custom-image3}

(Both images represent the component for forming a galaxy and various galaxy components (these images are taken from [this paper](https://www.nature.com/articles/490024a)))

Galaxy formation is a complex process that began shortly after the Big Bang and continues to shape the universe today. Galaxies are believed to have formed from tiny density fluctuations in the early cosmos, which expanded into enormous formations of gas, dark matter, and stars due to gravity. The formation of dark matter halos due to these early fluctuations gave baryonic matter, or "normal" matter. This gravitational anchor helped it collapse and give rise to the first stars and galaxies [(White & Rees, 1978)](https://doi.org/10.1093/mnras/183.3.341). The variety of galaxy types we see today, from the graceful spirals to the more amorphous ellipticals, results from smaller galaxies merging over billions of years. According to [Somerville and Davé (2015)](https://doi.org/10.1146/annurev-astro-082812-140951), there are still important concerns regarding how initial conditions and subsequent interactions influence a galaxy's final structure, even after a great deal of observational and simulation-based research.

Compared to larger galaxies like the Milky Way, which has hundreds of billion stars, dwarf galaxies are the smallest and most common galaxies in the universe, with as few as one billion stars. These small galaxies are intriguing because they serve as "building blocks" for larger galaxies and provide information about the distribution of dark matter and galaxy formation. However, there are several difficulties in comprehending dwarf galaxies, especially in relation to the distribution and amount of dark matter they contain. Observations reveal that the distribution of dark matter in dwarf galaxies frequently deviates from predictions. The "core-cusp" problem, in which dark matter should be densely packed in the center (a "cusp") but instead appears more spread out (a "core") [(Walker & Peñarrubia, 2011)](https://doi.org/10.1088/0004-637X/742/1/20), is one of the most contentious issues. Additionally, there are still unanswered questions regarding the nature of dark matter and the physics governing galaxy formation due to the "missing satellites problem"—the existence of fewer dwarf galaxies in the vicinity of larger galaxies than simulations predict [(Bullock & Boylan-Kolchin, 2017)](https://doi.org/10.1146/annurev-astro-091916-055313). My current work can also shed some light on these problems. For large structures in the universe, FDM produces the same conclusion as the ΛCDM model, and it may alleviate these issues on a small scale.

## Gravitational Wave Data Analysis

![Glitch subtraction from GW170817 (binary neutron star signal)](/assets/Images/glitch_GW170817.png){: .custom-image3}

(Glitch subtraction from GW170817 (binary neutron star signal) is taken from [my master's thesis](https://www.proquest.com/openview/7f68a2c9fc2972f4eb08e0d1a8fcbd2e/1?cbl=18750&diss=y&pq-origsite=gscholar).)
Gravitational wave detectors like LIGO, Virgo, and KAGRA are highly sensitive instruments designed to measure incredibly faint spacetime distortions caused by astrophysical events.  Their sensitivity, however, also increases the likelihood that they will pick up glitches, which are temporary noise artifacts. A number of factors, such as seismic activity, thermal fluctuations, electronic noise, and human-induced disturbances, can produce glitches, which are short-duration, non-astrophysical signals [(Abbott et al., 2016)](https://iopscience.iop.org/article/10.3847/2041-8205/833/1/L1). It can be difficult to identify and analyze events like binary mergers or supernovae because of these noise artifacts, which can hide or mimic real gravitational wave signals across a wide range of time-frequency characteristics [(Powell et al., 2016)](https://iopscience.iop.org/article/10.1088/1361-6382/34/3/034002). Fixing this problem is essential since errors obscure signals and raise the false alarm rate, lowering the statistical confidence of detections. [(Mogushi, 2021)](https://arxiv.org/abs/2105.10522).

A mix of subtraction, classification, and detection methods are used to try to mitigate glitches. Currently, there are some methods that are working to mitigate glitches, which is summarized in [this paper](https://arxiv.org/abs/2406.01318). Convolutional neural networks, a machine learning technique, have been used to categorize glitches and differentiate them from astrophysical signals [(George & Huerta, 2018)](https://www.sciencedirect.com/science/article/pii/S0370269317310390?via%3Dihub). In order to identify glitches based on their spectral signatures, time-frequency domain analytic methods such as the Wavelet Detection Filter are also employed [(Chatterji et al., 2004)](https://iopscience.iop.org/article/10.1088/0264-9381/21/20/024). Techniques like Bayesian inference allow for precise noise modeling and signal reconstruction, as demonstrated in the Bayesian framework for glitch subtraction [(Cornish & Littenberg, 2015)](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.91.084034). Among these, I worked on [the adaptive spline fitting method](https://iopscience.iop.org/article/10.1088/1361-6382/acd0fe/meta) for its ability to model glitches flexibly without requiring strong assumptions about their structure. However, challenges remain, particularly in automating these methods for real-time applications, optimizing parameters to avoid overfitting, and handling overlapping glitches and astrophysical signals.

More details on specific projects can be found in my [Code Projects](/code/) section.
