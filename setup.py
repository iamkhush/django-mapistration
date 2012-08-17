#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='django-mapistration',
    version='0.1',
    description='Map integration with registration form',
    author='iamkhush',
    author_email='ankush.chadda@gmail.com',
    url='https://github.com/iamkhush/django-mapistration',
    long_description=open('README.md', 'r').read(),
    packages=[
        'mapistration',
    ],
    package_data={
        'tastypie': ['templates/tastypie/*'],
    },
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)