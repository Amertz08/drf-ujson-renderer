#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="drf_ujson",
    version="1.2.1",
    description="Django Rest Framework UJSON Renderer",
    author="Gizmag",
    author_email="tech@gizmag.com",
    url="https://github.com/Amertz08/drf-ujson-renderer",
    packages=find_packages(),
    install_requires=["django", "ujson", "djangorestframework<3.10"],
    extras_require={"dev": ["pytest", "pytest-runner"]},
)
