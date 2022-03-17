#!/usr/bin/python3

import setuptools
from setuptools import setup
try:
    from setupext_janitor import janitor
    CleanCommand = janitor.CleanCommand
except ImportError:
    CleanCommand = None

cmd_classes = {}
if CleanCommand is not None:
   cmd_classes['clean'] = CleanCommand

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name="sumorun",
        version="0.0.1",
        scripts=['bin/sumorun'],
        setup_requires=['setupext_janitor'],
        cmdclass=cmd_classes,
        entry_points={
        # normal parameters, ie. console_scripts[]
        'distutils.commands': [
            ' clean = setupext_janitor.janitor:CleanCommand']
        },
        author="Archie Hilton",
        author_email="archie.hilton1@gmail.com",
        description="Utility for running SUMO simulations.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python 3",
            "Operating System :: OS Independent"
        ]
)