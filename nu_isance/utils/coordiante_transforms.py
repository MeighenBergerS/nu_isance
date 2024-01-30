# -*- coding: utf-8 -*-
# coordinate_transforms.py
# Authors: Stephan Meighen-Berger
# Triangle integrator for a generalized grid

# imports
import numpy as np

# module imports
from ..config import config

def r_obs_point(x: np.ndarray, psi: float, R0=config["halo"]["local distance"]) -> np.ndarray:
    """ recast of the radius

    Parameters
    ----------
    x: np.ndarray
        The distance between observer and the desired point
    psi: float
        The angles of interest (between point and GC)
    R0: float
        The scale radius (our distance)

    Returns
    -------
    r: np.ndarray
        The equilent distance in the new coordinate system
    """
    r = np.sqrt(
        R0**2 + x**2 - 2 * x * R0 * np.cos(psi)
    )
    return np.nan_to_num(r)

# EQ to GC coordinates
def l(
        alpha, delta,
        alpha0 = np.deg2rad(192.8595),
        delta0 = np.deg2rad(27.1284),
        l0 = np.deg2rad(123)
        ):
    """ utility function to go from EQ to GC
    Either alpha or delta can be a combination of:
    (float, float), (float, np.ndarray), (np.ndarray, float),
    and (np.ndarray, np.ndarray). In the latter case, the shapes
    must be the same.

    Parameters
    ----------
    alpha: np.ndarray
        right ascencion

    delta: np.ndarray
        declination

    alpha0, delta0, l0: floats
        Optional parameters to calibrate the transformation

    Returns
    -------
    l: np.ndarray
        The GC l coordinate with the same shape as the input
    """
    right = (
        (np.cos(delta) * np.sin(alpha - alpha0)) /
        (np.sin(delta) * np.cos(delta0) - np.cos(delta) * np.sin(delta0) *
         np.cos(alpha - alpha0))
    )
    l = l0 - np.arctan(right)
    return l

def b(
        alpha, delta,
        alpha0 = np.deg2rad(192.8595),
        delta0 = np.deg2rad(27.1284)
        ):
    """ utility function to go from EQ to GC
    Either alpha or delta can be a combination of:
    (float, float), (float, np.ndarray), (np.ndarray, float),
    and (np.ndarray, np.ndarray). In the latter case, the shapes
    must be the same.

    Parameters
    ----------
    alpha: np.ndarray
        right ascencion

    delta: np.ndarray
        declination

    alpha0, delta0: floats
        Optional parameters to calibrate the transformation

    Returns
    -------
    b: np.ndarray
        The GC b coordinate with the same shape as the input
    """
    right = (
        (np.sin(delta) * np.sin(delta0) + np.cos(delta) * np.cos(delta0) *
         np.cos(alpha - alpha0))
    )
    b =  np.arcsin(right)
    return b