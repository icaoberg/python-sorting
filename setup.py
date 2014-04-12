# Authors: Ivan E. Cao-Berg (icaoberg@alumni.cmu.edu) and Barbara Sanchez-Neri (bsanchez@alumni.cmu.edu)

import os
from setuptools import setup

#load the current version number of the package
exec(compile(open('VERSION').read(),'VERSION', 'exec'))

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name = 'sorting',
      version = __version__,
      description = ('Basic sorting algorithms in Python'),
      long_description=read('README.md'),
      author = ['Ivan Cao-Berg'],
      author_email = ['icaoberg@alumni.cmu.edu'],
      url = 'https://github.com/icaoberg/sorting',
      classifiers=[
      	'Programming Language :: Python', 
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Intended Audience :: Education',
        'Programming Language :: Python'],
      py_modules=['sorting.sorting'])
