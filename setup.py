#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="drf_ujson2",
    version="1.2.1",
    description="Django Rest Framework UJSON Renderer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Gizmag",
    author_email="tech@gizmag.com",
    url="https://github.com/Amertz08/drf-ujson-renderer",
    packages=find_packages(),
    install_requires=["django", "ujson", "djangorestframework<3.10"],
)
