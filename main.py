#!/usr/bin/python

__author__ = 'ashwin'
__email__ = 'gashwin1@umbc.edu'

"""
This project tries to look at methods to unify knowledge bases with Machine
Learning Algorithms.

HYPOTHESIS: Can Knowledge base information (in this case the semantic web), improve
            the performance of Machine Learning Algorithms, given that the relation
            between variables is known?
"""

from lib.stdops.fileops import FileReader

file_reader = FileReader()
file_reader.read_col_var_file("dataset/winequality/winesquality.var")

# Get the data in the file.
file_data = file_reader.read_data("dataset/winequality/winequality.csv", ";")
