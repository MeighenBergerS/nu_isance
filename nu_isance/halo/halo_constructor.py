# -*- coding: utf-8 -*-
# halo_constructor.py
# Authors: Stephan Meighen-Berger
# Constructs the halo model

# imports
import logging
import numpy as np
from typing import Dict
from scipy.integrate import quad

# module import
from ..config import config
from ..errors import UnknownModelError, UnphysicalError

_log = logging.getLogger(__name__)

class Halo(object):
    """ class containing and building the halo object
    """
    def __init__(self):
        """ initializes the halo object 
        """
        params = config['halo']
        self._build_model(params)
        self._loc_dens = self.rho(config["halo"]["local distance"])  # The local density
        # Adding some docs
        self.rho.__func__.__doc__ = self._rho_docs
        self.rho2.__func__.__doc__ = self._rho_docs

    @property
    def mass(self) -> float:
        """ the total mass of the halo in units of 10**7 M_solar
        """
        return self._total_mass
    
    @property
    def avg_density(self) -> float:
        """ the average density in 10**7 M_sol / kpc**3
        """
        return self._avg_dens
    
    @property
    def volume(self) -> float:
        """ the halo's volume in kpc**3
        """
        return self._volume

    @property
    def local_density(self) -> float:
        """ the local dark matter density in GeV / cm^3
        """
        return self._loc_dens

    def rho(self, r: np.ndarray) -> np.ndarray:
        """ density function

        Parameters
        ----------
        r: np.array
            Radius of interest in kpc

        Returns
        -------
        rho: np.array
            The density in units of 10**7 M_sol / kpc**3
        """
        return self._rho(r) * self._scaling

    def rho2(self, r: np.ndarray) -> np.ndarray:
        """ density function squared

        Parameters
        ----------
        r: np.array
            Radius of interest in kpc

        Returns
        -------
        rho: np.array
            The density in units of 10**7 M_sol / kpc**3
        """
        return (self._rho(r) * self._scaling)**2

    def _build_model(self, params: Dict):
        """ method to buiild a halo model

        Parameters
        ----------
        params: Dict
            Dictionary of the relevant parameters

        Raises
        ------
        UnknownModelError:
            The defined dark matter halo model isn't known
        """
        _log.info("Building the halo object")
        if params["name"] not in ["nfw", "einasto", "burkert"]:
            raise UnknownModelError(
                "The dark matter model set isn't supported! It is set to %s" %params['name']
            )
        halo_params = params[params["name"]]
        outer_radius = params['virial radius']

        if params['name'] == "nfw":
            _log.info("Builing an NFW halo")
            _log.info("Please cite the original paper when using this profile: " + halo_params["citation"])
            _log.debug("Importing and setting functions")
            from .nfw import nfw_rho as tmp_rho
            rs = outer_radius / halo_params['concentration']
            # Function Docstring
            self._rho_docs = tmp_rho.__doc__
            def rho(r: np.ndarray) -> np.ndarray:
                """ Fetches the density as a function of r
                """
                return tmp_rho(r, rs, halo_params["rhos"])

        elif params['name'] == "einasto":
            _log.info("Builing an Einasto halo")
            _log.info("Please cite the original paper when using this profile: " + halo_params["citation"])
            _log.debug("Importing and setting functions")
            from .einasto import einasto_rho as tmp_rho
            def rho(r: np.ndarray) -> np.ndarray:
                """ Fetches the density as a function of r
                """
                return tmp_rho(r, rs, halo_params["rhos"])

        elif params['name'] == "burkert":
            _log.info("Builing an Burkert halo")
            _log.info("Please cite the original paper when using this profile: " + halo_params["citation"])
            _log.debug("Importing and setting functions")
            from .burkert import burkert_rho as tmp_rho
            rs =  7.2
            # Function Docstring
            self._rho_docs = tmp_rho.__doc__
            def rho(r: np.array) -> np.array:
                """ Fetches the density as a function of r
                """
                return tmp_rho(r, rs, 0.48)

        self._rho = rho
        self._scaling = params["local density"] / rho(params["local distance"])
        _log.debug("Integrating")
        def integrand(r: np.array):
            return r**2. * self._rho(r)

        _log.debug("Integrating the halo...")
        integral= quad(
            integrand,
            params['minimal distance'],
            outer_radius
        )
        _log.debug("Finished the integration of the halo...")

        _log.debug("Setting averages and totals")
        self._total_mass = integral[0] * 4. * np.pi
        self._total_mass_err = integral[1]
        outer_vol = 4. * np.pi * outer_radius**3. / 3.
        inner_vol = 4. * np.pi * params['minimal distance']**3. / 3.
        self._volume = outer_vol - inner_vol
        if outer_vol <= inner_vol:
            raise UnphysicalError("Inner radius of halo must be smaller than the outer one!")
        self._avg_dens = self._total_mass / ( outer_vol - inner_vol)
        _log.info("Done")
