#!/usr/bin/env python3.6

"""Setup.py for btcince."""

from setuptools import setup

setup(
    name="btcince",
    description="Track value of a single bitcoin transaction.",
    version=0.1,
    author="Rick Valenzuela",
    author_email="rv@rickv.com",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=['transactions'],
    install_requires=['Quandl'],
    extras_require={
        "test": ['tox', 'pytest', 'pytest-watch', 'pytest-cov']
    },
)
