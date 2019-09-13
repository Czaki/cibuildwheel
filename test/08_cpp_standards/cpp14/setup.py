import os, sys

from setuptools import setup, Extension

setup(
    name="spam14",
    ext_modules=[Extension('spam14', sources=['spam14.cpp'], language="c++", extra_compile_args=["-std=c++14"])],
    version="0.1.0",
)
