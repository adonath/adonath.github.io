## Gammapy
_________________________

<img src="static/images/gammapy-logo.png" alt="drawing" style="float:left;width:128px;height:128px;"/>

I am lead developer of a project called *Gammapy*. *Gammapy* is an **open source Python package for gamma-ray astronomy**. It supports the analyis of data from Imaging Atmospheric Cherenkov Telescopes, such as [CTA](https://www.cta-observatory.org), [H.E.S.S.](https://www.mpi-hd.mpg.de/hfm/HESS/)
[MAGIC](https://magic.mpp.mpg.de/) and [VERITAS](https://veritas.sao.arizona.edu/), but also from all-sky instruments such as [Fermi-LAT](https://fermi.gsfc.nasa.gov/) and [HAWC](https://www.hawc-observatory.org/). It also allows users to combine data from all those
instruments to improve their scientific results.

The project was started by my PhD supervisor [Christoph Deil](https://christophdeil.com) almost a decade ago. Since then *Gammapy* has accumulated >100 users in the gamma-ray astronomy community and is expected to grow further. In 2020 the project has been selected as the base library for the official Science Tools of the [Cherenkov Telescope Array](https://www.cta-observatory.org). In February 2022 the software was awarded the [Jury Prize of the Open Science Awards](https://www.ouvrirlascience.fr/open-science-free-software-award-ceremony/) at the Open Science European Conference in Paris. In November 2022 we released the first long term support (LTS) version v1.0.

**Links:**
[Webpage](https://gammapy.org) | [Docs](https://docs.gammapy.org) | [GitHub](https://github.com/gammapy/gammapy) | [Paper](https://www.aanda.org/articles/aa/full_html/2023/10/aa46488-23/aa46488-23.html) | [ICRC 2021 Virtual Poster (best poster award)](https://video.desy.de/video/Gammapy-a-Python-Package-for-Gamma-Ray-Astronomy/70ff153f6d30ac6b8ab86f90ce1fba2a) | [Scipy 2023 Talk](https://youtu.be/NOX-jVj4IPA?si=Ueo2toyeJnsHjw9M)


</br>


## Pylira
_________________________
<img src="static/images/pylira-logo.png" alt="drawing" style="float:left;width:128px;"/>

*Pylira* is a **Python package for deconvolution of astronomical images in the presence of Poisson noise**.
It is based on a Bayesian statistical approach and allows to sample images from the posterior distribution under a hierarchical multiscale prior. The sampling approach allows astronomers to measure uncertainties of the reconstructed image along with the posterior mean. The package itself is mostly a Python wrapper around an existing R implementation based on [*pybind11*](https://pybind11.readthedocs.io). On top it offers convenience functionality to serialise and visualise the
results and check for their validity.

**Links:**
[Docs](https://pylira.readthedocs.io/en/latest/) | [GitHub](https://github.com/astrostat/pylira) | [Proceeding](https://conference.scipy.org/proceedings/scipy2022/pdfs/donath.pdf) | 
[Scipy 2022 Talk](https://youtu.be/FYleK2-fjKE)


</br>


## Jolideco
_________________________

More info soon...


</br>


## Snakemake Workflows
_________________________

I developed and maintain [Snakemake](https://snakemake.github.io) workflows for convenient and reproducible data analysis of X-ray and gamma-ray data.
Snakemake is a workflow management tool used in Bioninformatics that allows user to define, execute and share complex scalable analysis workflows.

**Links**:
[Snakemake workflow for Fermi-LAT](https://github.com/adonath/snakemake-workflow-fermi-lat) | [Snakemake workflow for Chandra](https://github.com/adonath/snakemake-workflow-chandra)

</br>


## Other
_________________________
I have contributed to other astronomical open source software projects, such as [*Astropy*](https://astropy.org), where I am also one of the sub-package maintainers for *astropy.convolution*.
I have made multiple minor contributions to *Astropy* affiliated packages such as [*photutils*](https://github.com/astropy/photutils), [*regions*](https://github.com/astropy/regions) and [*hipspy*](https://github.com/hipspy/hips). I wrote the [initial prototype](https://github.com/adonath/blob_detection) for *Scikit-image’s* [blob detection functionality](https://scikit-image.org/docs/dev/auto_examples/features_detection/plot_blob.html).

I also contributed to [*gamma-cat*](https://github.com/gammapy/gamma-cat), an open source data collection for gamma-ray astronomy.
