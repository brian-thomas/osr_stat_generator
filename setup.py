'''
Project setup module code. 

Created on Oct 27, 2019

@author:     brian thomas
@license:    MIT
@contact:    galactictaco@gmail.com
'''

from os.path import dirname, join

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    reqs = f.read().splitlines()

with open(join(dirname(__file__), 'README.md'), 'rb') as f:
    long_description = f.read().decode('ascii').strip()

import os
scripts = [os.path.join("bin",file) for file in os.listdir("bin")]

import osr_stat_generator
version=osr_stat_generator.version

setup (

    name='osr-stat-generator',
    description='Python package to generate stats for OSR characters', 
    url='https://github.com/brian-thomas/osr_stat_generator',
    version=version,

    keywords = 'OSR character stat generator',
    long_description=long_description,

    scripts=scripts,

    maintainer='Brian Thomas',
    maintainer_email='galactictaco@gmail.com',

    packages=find_packages(exclude=('tests', 'test.*')),
    license='MIT',

    include_package_data=True,

    setup_requires=[''],

    install_requires=reqs,

)

