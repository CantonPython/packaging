from setuptools import setup
from os import getcwd

with open('VERSION') as f:
    version = f.read().strip()

with open('README.rst') as f:
    long_description = f.read().strip()

setup(
    name='hello',
    version='1.1.0',
    author='Michael Meffie',
    author_email='mike@meffie.org',
    description='A tiny example package',
    long_description=long_description,
    url='https://github.com/CantonPython/packaging',
    install_requires=[
        'six',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Environment :: Console',
    ],
)
