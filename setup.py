try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

VERSION = "1.0"
DESCRIPTION = "My very first python package!"
LONG_DESCRIPTION = "This module can do the typography process kerning."

config = {
    'description' : DESCRIPTION,
    'long_description' : LONG_DESCRIPTION,
    'author' : 'Kento Nguyen',
    'url' : 'URL to get it at.',
    'download_url' : 'Where to download it.',
    'author_email' : 'nkento2007@gmail.com',
    'version' : VERSION,
    'packages' : find_packages(),
    'scripts' : [],
    'name' : 'kerning',

    'keywords' : ['python', 'first package'],
    'classifiers' : [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        ]
}

setup(**config)