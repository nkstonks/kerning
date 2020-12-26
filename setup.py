try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

VERSION = "1.2"
DESCRIPTION = "My very first python package!"
LONG_DESCRIPTION = "This module can do the typography process kerning."

config = {
    'description' : DESCRIPTION,
    'long_description' : LONG_DESCRIPTION,
    'author' : 'Kento Nguyen',
    'url' : 'https://github.com/nkstonks/kerning',
    'download_url' : 'https://github.com/nkstonks/kerning/archive/v1.2.tar.gz',
    'author_email' : 'nkento2007@gmail.com',
    'version' : VERSION,
    'packages' : find_packages(),
    'scripts' : [],
    'name' : 'kerning',

    'keywords' : ['python', 'first package'],
    'classifiers' : [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Everyone",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        ]
}

setup(**config)