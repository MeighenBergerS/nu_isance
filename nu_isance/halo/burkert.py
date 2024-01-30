# -*- coding: utf-8 -*-
# burkert.py
# Authors: Stephan Meighen-Berger
# Basic Burkert functions
# Cite: arXiv:astro-ph/9504041

import numpy as np


def burkert_rho(r: np.ndarray, rs: float, rhos: float) -> np.ndarray:
    """ basic burkert density function

    Parameters
    ----------
    r: np.ndarray / float
        The radius to evaluate at. Units should be in kpc
    rs: float
        The scale radius, this will be set with the config file
    rhos: float
        The scale density, this will be set with the config file

    Returns
    -------
    dens: np.ndarray / float
        The resulting density in the shape of the input.
        Units are 10**7 M_sol / kpc**3

    Notes
    -----
    The analytical form of the function is:
    .. math::
    \\rho(r) = \\frac{\\rho_0 r^3_0}{(r + r_0)(r^2 + r_0^2)}
    """
    dens = (
       rhos * rs**3 / (
           (r + rs) * (r**2 + rs**2)
       )
    )
    return dens