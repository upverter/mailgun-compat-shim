#!/usr/bin/env python
from setuptools import setup
import mailgun

setup(
    name=mailgun.__title__,
    packages=[mailgun.__title__],
    version=mailgun.__version__,
    description='A python shim for using the for Mailgun API v2 using the old python client methods',
    author=mailgun.__author__,
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
