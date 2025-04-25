import pathlib
from setuptools import setup, find_packages


with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='swb_ecco',
   version='0.0.1',
   description='Energy Modelling',
   long_description=long_description,
   packages=find_packages(),
   install_requires=pathlib.Path('requirements.txt').read_text(),  # external packages as dependencies
   scripts=[],
)
