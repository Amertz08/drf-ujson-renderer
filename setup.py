#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="drf_ujson2",
    version="1.3.1rc1",
    python_requires=">=2.7",
    description="Django Rest Framework UJSON Renderer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Gizmag",
    author_email="tech@gizmag.com",
    url="https://github.com/Amertz08/drf-ujson-renderer",
    packages=find_packages(exclude=["tests"]),
    install_requires=["django", "ujson>=1.35", "djangorestframework<3.10"],
    extras_require={"dev": ["pytest", "pytest-runner", "pytest-cov", "pytest-mock"]},
)
