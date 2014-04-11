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
      author = ['Ivan Cao-Berg ', 'Barbara Sanchez-Neri'],
      author_email = ['icaoberg@alumni.cmu.edu','bsanchez@alumni.cmu.edu'],
      install_requires = [
        'numpy>=1.4.1',
        ],
      url = 'https://bitbucket.org/bsanchezneri/sorting',
      classifiers=[
      	'Programming Language :: Python', 
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python'],
      py_modules=['sorting.sort'])
