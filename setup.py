# pylint: disable=missing-module-docstring
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="latae",
    version="0.0.4",
    author="shadawcraw",
    description="A simple library to parse and read robots.txt files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shadawcraw/robots.py",
    project_urls={
        "Bug Tracker": "https://github.com/shadawcraw/robots.py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "latae"},
    packages=setuptools.find_packages(where="latae"),
    python_requires=">=3.6",
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
