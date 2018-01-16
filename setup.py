# Standard library imports
from setuptools import setup


def get_lines(filename):
    with open(filename) as fileobj:
        return list(map(str.strip, fileobj))


setup(**{
    "name": "pipin-req",
    "author": "Shir0kamii",
    "author_email": "shir0kamii@gmail.com",
    "version": "0.1.4",
    "url": "https://github.com/Shir0kamii/pipin",
    "license": "MIT",
    "description": "Pin versions in requirements file",
    "classifiers": [
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Documentation"
    ],
    "keywords": "pip requirements requirement pin versions version",
    "install_requires": get_lines("requirements.txt"),
    "py_modules": ["pipin"],
    "entry_points": {
        "console_scripts": [
            "pipin = pipin:entry_point"
        ]
    }
})
