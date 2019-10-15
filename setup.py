#!/usr/bin/env python
from setuptools import setup

__title__ = 'mailgun'
__version__ = '0.0.4'
__author__ = 'Stephen Hamer'
__license__ = 'Apache 2.0'

setup(
    name=__title__,
    packages=[__title__],
    version=__version__,
    description='A python shim for using the for Mailgun API v2 using the old python client methods',
    author=__author__,
    author_email='stephen.hamer@upverter.com',
    url='https://github.com/Upverter/mailgun-compat-shim',
    keywords=['mailgun', 'email'],
    install_requires=[
        'mailgun2',
    ],
    license='Apache',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Communications :: Email',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
)
