#  PyCoA release v2 <img src="https://github.com/coa-project/coa-project.github.io/blob/main/fig/logo-anime.gif" width="140px" align=bottom > 

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
![GitHub last commit](https://img.shields.io/github/last-commit/pycoa/coa/dev?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/pycoa/coa?style=for-the-badge)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/coa-project/pycoa/dev)
_April 2020/October 2021_

[<img src="https://github.com/coa-project/coa-project.github.io/raw/main/fig/UK.png" height="14px" alt="UK flag"> English  version ](https://github.com/coa-project/pycoa)
/
[<img src="https://github.com/coa-project/coa-project.github.io/raw/main/fig/FR.png" height="14px" alt="FR flag"> Version française ](https://github.com/coa-project/pycoa/blob/main/README_FR.md)

<center>
<a href="https://github.com/coa-project/coa-project.github.io/raw/main/fig/mapFranceVariant.html" target="_blank"><img src="https://github.com/coa-project/coa-project.github.io/raw/main/fig/pycoa_v2.10_mapFranceVariant.html"></a>
</center>

`PyCoA` (Python Covid Analysis) is a Python™ framework which provides:
- a simple access to common Covid-19 databases;
- tools to represent and analyse Covid-19 data such as time series plots, histograms and maps.

|Time serie (cumulative) | Time series (G20) |
|------------|-------------|
|<a href="https://github.com/coa-project/coa-project.github.io/raw/main/fig/pycoa_v2.10_plot_sumall.html" target="_blank"><img src="https://github.com/coa-project/coa-project.github.io/raw/main/fig/pycoa_v2.10_plot_sumall.png"></a>|<a href="https://github.com/coa-project/coa-project.github.io/raw/main/fig/pycoa_v2.10_plot_g20.html" target="_blank"><img src="https://github.com/coa-project/coa-project.github.io/raw/main/fig/pycoa_v2.10_plot_g20.png"></a>|

|MAP (OECD) | Histogram (World| 
|------------|-------------|
|<a href="https://github.com/coa-project/coa-project.github.io/raw/main/fig/pycoa_v2.10_plot_oecd.html" target="_blank"><img src="https://github.com/coa-project/coa-project.github.io/raw/main/fig/pycoa_v2.10_plot_oecd.png"></a>|<a href="https://github.com/coa-project/coa-project.github.io/raw/main/fig/pycoa_v2.10_hist_bycountry.html" target="_blank"><img src="https://github.com/coa-project/coa-project.github.io/raw/main/fig/pycoa_v2.10_hist_bycountry.png"></a>|

|PIE (EU) | Histogram by value (Asia) |
|------------|-------------|
|<a href="https://github.com/coa-project/coa-project.github.io/raw/main/fig/pycoa_v2.10_pie.html" target="_blank"><img src="https://github.com/coa-project/coa-project.github.io/raw/main/fig/pycoa_v2.10_pie.png"></a>|<a href="https://github.com/coa-project/coa-project.github.io/raw/main/fig/pycoa_v2.10_histval.html" target="_blank"><img src="https://github.com/coa-project/coa-project.github.io/raw/main/fig/pycoa_v2.10_histval.png"></a>|

It is designed to be accessible to non-specialists: teenagers learning Python™, students, science journalists, even scientists who are not familiar in data access methods. A simple analysis can be performed out of the box, as well as a more complex analysis for people familiar with Python™ programming. As an example, after <a href="https://github.com/coa-project/pycoa/wiki/Install" target=_blank>installing pycoa</a> to your framework, the following few lines of code produce the four figures introducing this short documentation.

```python
import coa.front as cf
# default database is JHU
cf.plot(option='sumall') # default is 'deaths', for all countries
cf.plot(where='g20') # managing region
cf.map(where='oecd',what='daily',when='01/02/2021',which='confirmed')

cf.setwhom('owid') # changing database
cf.hist(which='total_vaccinations') # default is for all countries
cf.hist(which='cur_icu_patients',typeofhist='pie',where='european union')
cf.hist(which='total_people_fully_vaccinated_per_hundred',typeofhist='byvalue',where='asia')
```

Since the `v2.0` version, PyCoA manages also local data :
- [JHU-USA](https://coronavirus.jhu.edu/) or [CovidTracking](https://covidtracking.com) for the United-States, 
- [SPF](https://www.santepubliquefrance.fr/dossiers/coronavirus-covid-19), [OpenCovid19](https://github.com/opencovid19-fr) or [Obepine](https://www.reseau-obepine.fr/donnees-ouvertes/) for France,
- [DPC](https://github.com/pcm-dpc/COVID-19) for Italy,
- [Covid19India](https://api.covid19india.org) for India,
- [RKI](https://github.com/jgehrcke/covid-19-germany-gae) for Germany,
- [Escovid19Data](https://github.com/montera34/escovid19data) for Spain,
- [PHE](https://api.coronavirus.data.gov.uk) for United Kingdom,
- [Sciensano](https://epistat.sciensano.be) for Belgium,
- [DGS](https://github.com/dssg-pt/covid19pt-data) for Portugal,
- [MOH](https://github.com/MoH-Malaysia) for Malaysia.

Then we get plots like the ones just below. Other databases has been added for Italy or India.

|SPF data | JHU-USA data |
|------------|-------------|
|<a href="https://github.com/coa-project/coa-project.github.io/raw/main/fig/pycoa_v2.10_spf.html" target="_blank"><img src="https://github.com/coa-project/coa-project.github.io/raw/main/fig/pycoa_v2.10_spf.png" width=504></a>|<a href="https://github.com/coa-project/coa-project.github.io/raw/main/fig/pycoa_v2.10_jhu-usafolium.html" target="_blank"><img src="https://github.com/coa-project/coa-project.github.io/raw/main/fig/pycoa_v2.10_jhu-usafolium.png" width=504></a>|

```python
cf.setwhom('spf') # Santé Publique France database
cf.map(which='tot_vacc',tile='esri') # Vaccinations, map view optional tile 

cf.setwhom('jhu-usa') # JHU USA database
cf.map(visu='folium') # deaths, map view with folium visualization output
```

`PyCoA` works currently inside `Jupyter` notebook, over a local install or on online platforms such as <a href="https://colab.research.google.com/" target=_blank>Google Colab</a>.

A basic demo code is available as a notebook on <a href="https://github.com/coa-project/coabook/blob/master/demo_pycoa.ipynb" target=_blank ><img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" height="20" alt="GitHub logo" /> GitHub</a>, on <a href="https://colab.research.google.com/github/coa-project/coabook/blob/master/demo_pycoa.ipynb" target=_blank ><img src="https://colab.research.google.com/img/colab_favicon_256px.png" height="20" alt="Google colab logo" /> Google Colab</a>, or on <a href="https://nbviewer.jupyter.org/github/coa-project/coabook/blob/master/demo_pycoa.ipynb" target=_blank ><img src="https://nbviewer.jupyter.org/static/img/nav_logo.svg" height="20" alt="NbViewer logo" /> Jupyter NbViewer</a>. Other notebooks are provided in our <a href="https://github.com/coa-project/coabook/blob/master/README.md" target=_blank >coabook page</a>.

Full documentation is on <a href="https://github.com/coa-project/pycoa/wiki/Home" target=_blank>the Wiki</a>.

### Authors

* Tristan Beau - [Université de Paris](http://u-paris.fr) - [LPNHE laboratory](http://lpnhe.in2p3.fr/)
* Julien Browaeys - [Université de Paris](http://u-paris.fr) - [MSC laboratory](http://www.msc.univ-paris-diderot.fr/)
* Olivier Dadoun - [CNRS](http://cnrs.fr) - [Sorbonne Université](https://www.sorbonne-universite.fr/) - [LPNHE laboratory](http://lpnhe.in2p3.fr/)

### Contact
* Email : [`support@pycoa.fr`](mailto:support@pycoa.fr)
* Web page : [`www.pycoa.fr`](http://www.pycoa.fr)
* On twitter : [`@pycoa_fr`](https://twitter.com/pycoa_fr)
