#!/usr/bin/env python

import pathlib
from setuptools import setup

# Parent directory
HERE = pathlib.Path(__file__).parent

# The readme file
README = (HERE / "README.md").read_text()

setup(
    name="nuisance",
    version="0.0.1",
    description="Neutrino Flux",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Stephan Meighen-Berger",
    author_email="stephan.meighenberger@gmail.com",
    url='https://github.com/MeighenBergerS/nu_isance',
    license="GNU",
    install_requires=[
        "PyYAML",
        "numpy",
        "scipy",
        "pandas",
    ],
    extras_require={
        "interactive": ["nbstripout", "matplotlib", "jupyter", "tqdm"],
        "advanced": ["mceq"],
    },
    packages=["nu_isance"],
    package_data={'nu_isance': ["data/*.pkl"]},
    include_package_data=True
)