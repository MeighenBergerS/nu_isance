# -*- coding: utf-8 -*-
# nfw.py
# Authors: Stephan Meighen-Berger
# Basic NFW functions
# Cite: arXiv:astro-ph/9508025

import numpy as np


def nfw_rho(r: np.ndarray, rs: float, rhos: float) -> np.ndarray:
    """ basic nfw density function

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
    \\rho(r) = \\frac{\\rho_s}{\\frac{r}{r_s} \\left(1 + \\left(\\frac{r}{r_s}\\right)^2\\right)}
    """
    dens = (
        rhos / (
            (r / rs) * (1 + (r / rs))**2.
        )
    )
    return dens