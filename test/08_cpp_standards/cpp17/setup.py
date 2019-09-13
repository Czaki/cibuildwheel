import os, sys

from setuptools import setup, Extension

import platform

if platform.system() == "Windows":
    extra_compile_args = ["/std:c++17"]
else:
    extra_compile_args = ["-std=c++17"]

setup(
    name="spam17",
    ext_modules=[Extension('spam17', sources=['spam17.cpp'], language="c++", extra_compile_args=extra_compile_args)],
    version="0.1.0",
)
