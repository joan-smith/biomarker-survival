# biomarker-survival
Utilities for performing biomarker survival analyses (e.g. cox proportional hazards, kaplan-meier, etc) from TCGA, CBioPortal,
and other datasets

# Installation
Installation and use of this package has been tested on Ubuntu and Mac OS X. In both cases, it has been most thoroughly tested
using the Anaconda package manager. 

To install Anaconda, follow instructions [here](https://docs.anaconda.com/anaconda/install/)


```
$ conda install -c r rpy2
$ pip install biomarker-survival
```


Please note that rpy2 has been deprecated, and so must be installed with Anaconda, not pip. 


# Use
This package operates on data in the [TCGA](https://www.cancer.gov/about-nci/organization/ccg/research/structural-genomics/tcga). 
For processed data, please see [http://survival.cshl.edu](http://survival.cshl.edu)
