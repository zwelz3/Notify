#!/usr/bin/env python
import setuptools
import re
from pathlib import Path


__version__ = re.match(
    r'''__version__\s*=\s*['"](.*)['"]''',
    (Path(__file__).parent / "_version.py").read_text()
).groups()[0]


setup_args = dict(
    name='notify',
    version=__version__,
    description='A library to support email notifications in Python.',
    long_description=open('README.md').read(),
    download_url='',
    keywords='notification',
    author='zwelz3',
    url='',
    license='',
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    install_requires=[],
    classifiers=[]
)


if __name__ == "__main__":
    setuptools.setup(**setup_args)
