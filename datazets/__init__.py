from datazets.datazets import get


__author__ = 'Erdogan Tasksen'
__email__ = 'erdogant@gmail.com'
__version__ = '0.1.2'

# module level doc-string
__doc__ = """
datazets
=====================================================================

Description
-----------
Datazets is a python package to import well known example data sets.

Example
-------
>>> # Import library
>>> import datazets as dz
>>> #
>>> # Import data set
>>> df = dz.get('titanic')
>>> #
>>> # Import from url
>>> url='https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'
>>> df = dz.get(url=url, sep=',')

References
----------
https://github.com/erdogant/datazets

"""
