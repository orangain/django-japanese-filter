#coding: utf-8

import os

from setuptools import setup, find_packages

long_description = """
django_japanese_filter
======================

Django filters for Japanese.

Installation
------------

::

    $ pip install django_japanese_filter

Insert 'django_japanese_filter' into INSTALLED_APPS in settings.py.

::

    INSTALLED_APPS = (
        ...
        'django_japanese_filter',
    )

Usage
-----

In template files,

::

    {% load japanese %}

    {{ description|truncatewidth:"20" }}

"""

setup(
    name = 'django_japanese_filter',
    version = '0.1',
    packages = find_packages(),
    install_requires = [
        'django',
    ],
    author = 'orangain',
    author_email = 'orangain@gmail.com',
    license = "MIT",
    url = 'https://github.com/orangain/django-japanese-filter',
    description = 'Django filters for Japanese',
    long_description = long_description,
    keywords = ['django', 'japanese', 'filter'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.6',
        'Topic :: Utilities',
    ],
)
