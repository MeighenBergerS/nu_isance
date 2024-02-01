# Nuisance

Authors:

1. Stephan Meighen-Berger, developed the Nuisance Code

## Table of contents

1. [Introduction](#introduction)

2. [Citation](#citation)

3. [Installation](#installation)

## Introduction <a name="introduction"></a>

Welcome to Nuisance!

A python package to simulate neutrino fluxes.

Examples are given in the notebook folder, but here is a basic script to get
you going:

```
# Module import
from nu_isance import Nuisance, config

# A nusciance instance with options
config['oscillation']['matter'] = True
nusciance = Nuisance()
```


## Citation <a name="citation"></a>

Please cite this [software](https://github.com/MeighenBergerS/nu_isance) using
```
@software{nuisance@github,
  author = {Stephan Meighen-Berger},
  title = {{Nuisance}: Dark Matter Halo},
  url = {https://github.com/MeighenBergerS/nu_isance},
  version = {0.0.1},
  year = {2024},
}
```

## Installation <a name="installation"></a>
Once ready use:

Install using pip:
```python
pip install nu_isance
```
[The PyPi webpage](https://pypi.org/project/nu_isance/)