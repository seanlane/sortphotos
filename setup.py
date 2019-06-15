#!/usr/bin/env python3
# encoding: utf-8

from setuptools import setup, find_packages

setup(
    name='sortphotos',
    version='1.0',
    description='Organizes photos and videos into folders using date/time information ',
    author='Andrew Ning',
    packages=find_packages('src'),
    include_package_data=True,
    license='MIT License',
    install_requires=[
        'exifread',
        'future',
        'reverse_geocode'
    ],
    entry_points={
        'console_scripts': [
          'sortphotos = src.sortphotos:main',
        ]
      }
)

