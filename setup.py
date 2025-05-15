from setuptools import setup, find_packages

setup(
    name='montecarlo',
    version='0.1.0',
    description='A Python package for Monte Carlo simulations.',
    author='Anthony Mays',
    packages=find_packages(where='montecarlo'),
    package_dir={'': 'montecarlo'},
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy',
    ],
)
