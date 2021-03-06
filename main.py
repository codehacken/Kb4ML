#!/usr/bin/python

__author__ = 'ashwin'
__email__ = 'gashwin1@umbc.edu'

"""
This project tries to look at methods to unify knowledge bases with Machine
Learning Algorithms.

HYPOTHESIS: Can Knowledge base information (in this case the semantic web),
            improve the performance of Machine Learning Algorithms, given that
            the relation between variables is known?
"""

from lib.stdops.fileops import FileReader
import lib.test as test

# Preliminaries.
data_sep = ","
elim_var = ['$continuous$']
class_name = "Classify"

# Training and Test data files.
train_f_name = "dataset/adult_data/adult.data"
test_f_name = "dataset/adult_data/adult.test"

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

"""
This is the test using Naive Bayes.
The cross product is applied for the following attribute combinations:
a. workclass, education, marital-status
b. education, marital-status
c. marital-status, relationship
d. education, marital-status, relationship.

This method tries to apply cross product to attributes that are not likely
to be conditionally independent.
"""
# Test Naive Bayes with cross product.
cross_prod_list = [[['workclass', 'education', 'marital-status']],
                   [['education', 'marital-status']],
                   [['marital-status', 'relationship']],
                   [['education', 'marital-status', 'relationship']]]

for cross_prod_columns in cross_prod_list:
    score = test.test_nb_cross_product(train_file_reader, test_file_reader,
                                       cross_prod_columns)
    print cross_prod_columns
    print score

"""
This is a test using a modified 'RandomForest' method.
"""
# Test Random Forest implementation.
