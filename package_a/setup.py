#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import os
import sys
from setuptools import setup, find_packages

source_root = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(source_root, "install"))
from test_version import geos_check  # NOQA

geos_check()

# with open("README.md", encoding="utf-8") as readme_file:
#     readme = readme_file.read()


readme = "does not exist"

requirements = []
install_requires = [
    "cartopy",
    "scipy"
    # "matplotlib",  # see #4773
]

test_requirements = ["pytest==5.2.2"]

setup(
    author="Me",
    author_email="dummy@test.com",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="demo package",
    extras_require={},
    setup_requires=[],
    install_requires=install_requires,
    tests_require=test_requirements,
    license="BSD license",
    long_description=readme,
    include_package_data=True,
    keywords="demo package",
    name="package-a",
    packages=find_packages(exclude=["test"]),
    test_suite="test",
    version="0.1.0",
    zip_safe=False,
)
