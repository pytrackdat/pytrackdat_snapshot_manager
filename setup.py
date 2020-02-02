#!/usr/bin/env python

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pytrackdat_snapshot_manager",
    version="0.1.0",

    python_requires="~=3.6",
    install_requires=["Django>=2.2.9,<3.0"],

    description='Snapshot manager Django app for PyTrackDat sites.',
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/pytrackdat/pytrackdat_snapshot_manager",
    license="GPLv3",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"  # Maybe should be refined
    ],

    author="David Lougheed",
    author_email="david.lougheed@gmail.com",

    packages=find_packages(),
    include_package_data=True
)
