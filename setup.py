from setuptools import find_packages, setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='census_data',
    package_dir={"": "src"},
    packages=find_packages('src'),
    version='0.0.0',
    description='Examples for working with Census data.',
    long_description=long_description,
    author='Joel McCune',
    license='Apache 2.0',
)
