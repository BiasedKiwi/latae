from setuptools import find_packages, setup

setup(
    name="robots.py",
    packages=find_packages(include=["robotspy"]),
    version='0.1.0',
    description="A simple library to parse robots.txt files.",
    author="shadawcraw",
    license="MIT",
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite="tests",
)
