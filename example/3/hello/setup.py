from setuptools import setup

setup(
    name='hello',
    version='1.3.0',
    author='Michael Meffie',
    author_email='mike@meffie.org',
    description='A tiny example package',
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
