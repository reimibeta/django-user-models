#!/usr/bin/env python


import os

# allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# if __name__ == "__main__":
import setuptools

setuptools.setup(
    name='user_models',
    version='1.1.7',
    packages=setuptools.find_packages(),
    # scripts=['makemigrations.py','migrate.py']
)
