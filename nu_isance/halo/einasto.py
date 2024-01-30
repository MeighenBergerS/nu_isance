# -*- coding: utf-8 -*-
# einasto.py
# Authors: Stephan Meighen-Berger
# Basic Einasto functions
# Cite: https://ui.adsabs.harvard.edu/abs/1965TrAlm...5...87E

import numpy as np


def einasto_rho(r: np.array, rm2: float, rhom2: float, alpha: float) -> np.array:
    """ basic einasto density function

    Parameters
    ----------
    r: np.array / float
        The radius to evaluate at. Units should be in kpc
    rm2: float
        The scale radius
    rhom2: float
        The scale density
    alpha: float
        The shape parameter

    Returns
    -------
    dens: np.array /float
        The resulting density in the shape of the input.
        Units are 10**7 M_sol / kpc**3
    """
    dens = (
        rhom2 * np.exp(
            -2. / alpha * ((r / rm2)**alpha - 1.)
        )
    )
    return dens