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

from lib.models.classify import NaiveBayes

naive_bayes = NaiveBayes()

# Vectorize the data for Naive Bayes.
[train_ft_data, train_cl_data] = naive_bayes.vectorize_data("dataset/adult_data/adult.var",
                                                            "dataset/adult_data/adult.data.temp",
                                                            ",", ['$continuous$'])

# Train the model.
model = naive_bayes.train_model(train_ft_data, train_cl_data)

print model.class_count_
print model.feature_count_
