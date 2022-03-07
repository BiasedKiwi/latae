import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="robots.py",
    version="0.0.1",
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
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)