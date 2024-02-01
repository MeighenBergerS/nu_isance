# Nuisance

Authors:

1. Stephan Meighen-Berger, developed the Nuisance Code

## Table of contents

1. [Introduction](#introduction)

2. [Citation](#citation)

3. [Installation](#installation)

## Introduction <a name="introduction"></a>

Welcome to Nuisance!

![WeirdLogo](./images/weird_logo.jpg)

A python package to simulate neutrino oscillations.

Examples are given in the notebook folder, but here is a basic script to get
you going:

```python
# Module import
from nu_isance import Nuisance, config

# A nusciance instance with options
config['oscillation']['matter'] = True
nusciance = Nuisance()

# Accessing the simulation
nu_e_e = nusciance.osc.oscillation_prob_e[0]  # For nu_e -> nu_e
nu_e_mu = nusciance.osc.oscillation_prob_e[1]  # For nu_e -> nu_mu
nu_e_tau = nusciance.osc.oscillation_prob_e[2]  # For nu_e -> nu_tau
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