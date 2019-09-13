import os, sys

from setuptools import setup, Extension

setup(
    name="spam11",
    ext_modules=[Extension('spam11', sources=['spam11.cpp'], language="c++", extra_compile_args=["-std=c++11"])],
    version="0.1.0",
)
