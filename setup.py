VERSION = '0.4'

import os
from setuptools import setup, find_packages


setup(
    namespace_packages = ['tiddlywebplugins'],
    name = 'tiddlywebplugins.lazy',
    version = VERSION,
    description = 'A TiddlyWeb plugin that makes tiddlywebwiki load lazy.',
    long_description = open(os.path.join(os.path.dirname(__file__), 'README')).read(),
    author = 'Chris Dent',
    author_email = 'cdent@peermore.com',
    platforms = 'Posix; MacOS X; Windows',
    packages = find_packages(exclude=['test']),
    install_requires = [
        'tiddlywebwiki>=0.57.0',
        'tiddlyweb',
        ],
    include_package_data = True,
    zip_safe = False
    )
