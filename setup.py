# -*- coding: utf-8 -*-
from __future__ import with_statement

from setuptools import setup


version = '1.1.0'


setup(
    name='django-logit',
    version=version,
    keywords='Django Logging Log POST GET Query Params',
    description='Django Decorator of Logging Request Params/Response Content',
    long_description=open('README.rst').read(),

    url='https://github.com/Brightcells/django-logit',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=[],
    py_modules=['django_logit'],
    install_requires=[],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
    ],
)
