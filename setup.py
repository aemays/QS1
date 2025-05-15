from setuptools import setup, find_packages

setup(
    name="montecarlo",
    version="0.1.0",
    packages=find_packages(where="montecarloPackage"),
    package_dir={"": "montecarloPackage"},
    install_requires=[
        # Add your dependencies here
    ],
    extras_require={
        "dev": ["pytest", "pytest-cov", "codecov"],
    },
)