from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file

long_description = ''

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()


__title__ = ''
__version__ = ''
__summary__ = ''
__uri__ = ''
__author__ = ''
__author_email__ = ''
exec(open('./qface/__about__.py').read())

setup(
    name=__title__,
    version=__version__,
    description=__summary__,
    long_description=long_description,
    url=__uri__,
    author=__author__,
    author_email=__author_email__,
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Code Generators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='qt code generator framework',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'jinja2',
        'path.py',
        'pyyaml',
        'antlr4-python3-runtime==4.7',
        'typing',
        'click',
        'watchdog',
        'six',
    ],
    extras_require={
        'dev': [
            'watchdog',
            'pypandoc',
        ],
        'test': [
            'pytest',
            'watchdog',
            'ipdb',
        ],
    }
)
