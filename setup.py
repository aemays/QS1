from setuptools import setup, find_packages

setup(
    name="montecarlo",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
    ],
    extras_require={
        "dev": ["pytest", "pytest-cov", "codecov"],
    },
)
