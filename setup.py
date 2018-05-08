"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='asciimage',
    version='1.2.1',
    description='Generate ASCII Art from an image',

    long_description=long_description,
    url='https://github.com/utnaf/asciimage',
    author='Davide Effe',
    author_email='utnaf.dev@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['asciimage'],
    test_suite='nose.collector',
    tests_require=['nose']
)
