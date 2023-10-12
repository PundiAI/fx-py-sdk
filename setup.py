#!/usr/bin/env python
from setuptools import (
    find_packages,
    setup,
)

requires = [
    "grpcio>=1.59.0",
    "google-api-python-client>=2.102.0",
    "bech32>=1.2.0",
    "ecdsa>=0.18.0",
    "hdwallets>=0.1.2",
    "mnemonic>=0.20",
    "eth-utils>=2.2.2",
    "coincurve>=18.0.0",
    "pycryptodome>=3.19.0"
]

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

setup(
    name="fx-py-sdk",
    version="0.6.10",
    platforms='any',
    description="Python library for FunctionX",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='zakir',
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=requires,
    url='https://github.com/functionx/fx-py-sdk',
    keywords=["FunctionX", "blockchain"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.11",
    ],
    include_package_data=True
)
