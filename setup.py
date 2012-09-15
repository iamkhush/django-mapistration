#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='django-mapistration',
    version='0.1',
    description='Map integration with registration form',
    author='iamkhush',
    author_email='ankush.chadda@gmail.com',
    url='https://github.com/iamkhush/django-mapistration',
    long_description=open('README.md', 'r').read(),
    packages=find_packages(),
    package_data = {
    '': ['docs/*.txt', 'docs/*.rst'],
    },
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)