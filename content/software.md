## Gammapy
_________________________
<img class="image-software" src="static/images/gammapy-logo.png"/>

I am lead developer of a project called *Gammapy*. *Gammapy* is an **open source Python package for gamma-ray astronomy**. It supports the analysis of data from Imaging Atmospheric Cherenkov Telescopes, such as [CTA](https://www.cta-observatory.org), [H.E.S.S.](https://www.mpi-hd.mpg.de/hfm/HESS/)
[MAGIC](https://magic.mpp.mpg.de/) and [VERITAS](https://veritas.sao.arizona.edu/), but also from all-sky instruments such as [Fermi-LAT](https://fermi.gsfc.nasa.gov/) and [HAWC](https://www.hawc-observatory.org/). It also allows users to combine data from all those
instruments to improve their scientific results.

The project was started by my PhD supervisor [Christoph Deil](https://christophdeil.com) almost a decade ago. Since then *Gammapy* has accumulated >100 users in the gamma-ray astronomy community and is expected to grow further. In 2020 the project has been selected as the base library for the official Science Tools of the [Cherenkov Telescope Array](https://www.cta-observatory.org). In February 2022 the software was awarded the [Jury Prize of the Open Science Awards](https://www.ouvrirlascience.fr/open-science-free-software-award-ceremony/) at the Open Science European Conference in Paris. In November 2022 we released the first long term support (LTS) version v1.0.

**Links:**
[Webpage](https://gammapy.org) | [Docs](https://docs.gammapy.org) | [GitHub](https://github.com/gammapy/gammapy) | [Paper](https://www.aanda.org/articles/aa/full_html/2023/10/aa46488-23/aa46488-23.html) | [ICRC 2021 Virtual Poster (best poster award)](https://video.desy.de/video/Gammapy-a-Python-Package-for-Gamma-Ray-Astronomy/70ff153f6d30ac6b8ab86f90ce1fba2a) | [Scipy 2023 Talk](https://youtu.be/NOX-jVj4IPA?si=Ueo2toyeJnsHjw9M)



## Jolideco
_________________________
<img class="image-software" src="static/images/jolideco-logo.png"style="width:196px"/>

*Jolideco* is a **Python package for joint deconvolution of astronomical images in the presence of Poisson noise**. It allows to reconstruct a single image from multiple observations of different instruments with different point spread functions and exposure times. For the reconstruction it uses a maximum a posteriori (MAP) estimate of the joint Poisson likelihood of all observations under a patch based image prior. The image prior is learned from astronomical images at other wavelengths, such as images from the James Webb Space Telescope (JWST) or GLEAM radio survey. The package is implemented 
based on [Pytorch](https://pytorch.org) and features a clean and extensible API. It is the first package to offer a joint deconvolution and reconstruction of images for the x-ray and gamma-ray domain.

**Links:**
[Docs](https://jolideco.readthedocs.io/en/latest/) | [GitHub](https://github.com/jolideco/jolideco) | [Paper Arxiv](https://arxiv.org/abs/2403.13933) | [AstroAI Talk 2024](https://www.youtube.com/watch?v=m9IkPz5HrK4)



## GMMX
_________________________
<img class="image-software" src="static/images/gmmx-logo.png"style="width:196px"/>

*GMMX* is a minimal implementation of **Gaussian Mixture Models (GMM) in Jax**. It features a simple, clean API with different abstractions for models and fitters. It currently supports fitting with the Expectation-Maximization (EM) algorithm. 
Thanks to [Jax](https://jax.readthedocs.io/en/latest/) it achieves an excellent performance: up to 5-6x better than Scikit-Learn for prediction and training on the CPU. It also supports GPU acceleration and can thus be used for training 
on large datasets witrh around 50x better performance than Scikit-Learn. The package is designed to be easily extensible and can be used as a drop-in replacement for Scikit-Learn's GMM implementation.


**Links:**
[Docs](https://adonath.github.io/gmmx/) | [GitHub](https://github.com/adonath/gmmx)


## Pylira
_________________________
<img  class="image-software" src="static/images/pylira-logo.png"/>

*Pylira* is a **Python package for deconvolution of astronomical images in the presence of Poisson noise**.
It is based on a Bayesian statistical approach and allows to sample images from the posterior distribution under a hierarchical multiscale prior. The sampling approach allows astronomers to measure uncertainties of the reconstructed image along with the posterior mean. The package itself is mostly a Python wrapper around an existing R implementation based on [*pybind11*](https://pybind11.readthedocs.io). On top it offers convenience functionality to serialise and visualise the results and check for their validity.

**Links:**
[Docs](https://pylira.readthedocs.io/en/latest/) | [GitHub](https://github.com/astrostat/pylira) | [Proceeding](http://conference.scipy.org.s3-website-us-east-1.amazonaws.com/proceedings/scipy2022/pdfs/donath.pdf) | 
[Scipy 2022 Talk](https://youtu.be/FYleK2-fjKE)


## Snakemake Workflows
_________________________

I developed and maintain [Snakemake](https://snakemake.github.io) workflows for convenient and reproducible data analysis of X-ray and gamma-ray data.
Snakemake is a workflow management tool used in Bioinformatics that allows user to define, execute and share complex scalable analysis workflows.

**Links**:
[Snakemake workflow for Fermi-LAT](https://github.com/adonath/snakemake-workflow-fermi-lat) | [Snakemake workflow for Chandra](https://github.com/adonath/snakemake-workflow-chandra)


## Other
_________________________
I have contributed to other astronomical open source software projects, such as [*Astropy*](https://astropy.org), where I am also one of the sub-package maintainers for *astropy.convolution*.
I have made multiple minor contributions to *Astropy* affiliated packages such as [*photutils*](https://github.com/astropy/photutils), [*regions*](https://github.com/astropy/regions) and [*hipspy*](https://github.com/hipspy/hips). I wrote the [initial prototype](https://github.com/adonath/blob_detection) for *Scikit-image’s* [blob detection functionality](https://scikit-image.org/docs/dev/auto_examples/features_detection/plot_blob.html).

I also contributed to [*gamma-cat*](https://github.com/gammapy/gamma-cat), an open source data collection for gamma-ray astronomy.
