import os

from setuptools import setup, Extension, find_packages


setup(    
    packages=find_packages('./src'),
    package_dir={'': 'src'},
    ext_modules=[Extension('spam.spam', sources=['src/spam/spam.c'])],
)
