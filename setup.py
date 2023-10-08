#!/usr/bin/env python
from setuptools import (
    find_packages,
    setup,
)

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

setup(
    name="fx-py-sdk",
    version="0.5.0",
    platforms='any',
    description="Python library for fxCore",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='zakir',
    packages=find_packages(),
    url='https://github.com/functionx/fx-py-sdk',
    keywords=["fxCore", "blockchain"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    include_package_data=True
)
