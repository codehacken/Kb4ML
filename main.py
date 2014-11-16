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
import lib.test as test

# Preliminaries.
data_sep = ","
elim_var = ['$continuous$']
class_name = "Classify"

# Training and Test data files.
train_f_name = "dataset/adult_data/adult.data.temp"
test_f_name = "dataset/adult_data/adult.test.temp"

# File with column names and variable types.
var_f_name = "dataset/adult_data/adult.var"

# Create File Reader to read the data from a file and process it.
# This section the file reader only extracts the column values.
train_file_reader = FileReader(class_var_name=class_name)
train_file_reader.read_col_var_file(var_f_name, data_separator=data_sep)

# Get the data in the file.
train_file_reader.read_data(train_f_name, data_sep, elim_var)

# File Reader for test data set.
test_file_reader = FileReader(class_var_name=class_name)
test_file_reader.read_col_var_file(var_f_name, data_separator=data_sep)

# Get the data in the file.
test_file_reader.read_data(test_f_name, data_sep, elim_var)

# Test Naive Bayes.
score = test.test_naive_bayes(train_file_reader, test_file_reader)
print score

# Test Naive Bayes with cross product.
cross_prod_columns = [['education', 'marital-status'], ['sex', 'race']]
score = test.test_nb_cross_product(train_file_reader, test_file_reader, cross_prod_columns)
print score
