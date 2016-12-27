"""
Babelian
--------

Babelian is a dictionary of a Terminal.
You can search some words/phrases/examples without Browser.
This program will help Developers/Students/Teachers,
or who is learning 2nd languages.
glosbe provides the API of dictionary.
Thanks **glosbe**!

Links
`````
* Guide  : https://github.com/memnoth/babelian
* Github : https://github.com/memnoth/babelian
"""
# -*- coding: utf-8 -*-
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

ext_path = os.path.join(os.path.dirname(__file__), 'bin/td')
ver_line = [line for line in open(ext_path) if line.startswith('__version__')]
__ver__ = ver_line[0].split('=')[1].strip().replace('\'', '')

setup(
    name='Babelian',
    version=__ver__,
    url='https://github.com/memnoth/babelian',
    license='MIT',
    author='Yi Soo, (Jeff) An',
    author_email='yisooan@gmail.com',
    description='Babelian is a dictionary of a Terminal.',
    long_description=__doc__,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    packages=['babelian'],
    scripts=['bin/td'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Education',
    ],
)
