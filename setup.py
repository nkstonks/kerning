try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup
import os

with open("README.md", encoding="utf-8") as file:
    long_description = file.read()

VERSION = "1.4"
DESCRIPTION = "My very first python package!"

config = {
    'description' : DESCRIPTION,
    'long_description' : long_description,
    'long_description_content_type' : 'text/markdown',
    'author' : 'Kento Nguyen',
    'url' : 'https://github.com/nkstonks/kerning',
    'download_url' : 'https://github.com/nkstonks/kerning/archive/v1.3.tar.gz',
    'author_email' : 'nkento2007@gmail.com',
    'version' : VERSION,
    'packages' : find_packages(),
    'scripts' : [],
    'name' : 'kerning',

    'keywords' : ['python', 'first package'],
    'classifiers' : [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Other Audience",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        ]
}

setup(**config)