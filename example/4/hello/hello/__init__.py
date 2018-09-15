import os

def _read(name):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, '..', name)) as f:
        return f.read().strip()

__version__ = _read('VERSION')

def greeting():
    """Say a simple greeting."""
    print('hello world')

