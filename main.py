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

# Vectorize the training data for Naive Bayes.
[train_ft_data, train_cl_data] = naive_bayes.vectorize_data("dataset/adult_data/adult.var",
                                                            "dataset/adult_data/adult.data",
                                                            ",", ['$continuous$'])

# Train the model.
model = naive_bayes.train_model(train_ft_data, train_cl_data)

# Vectorize the test data.
[test_ft_data, test_cl_data] = naive_bayes.vectorize_data("dataset/adult_data/adult.var",
                                                          "dataset/adult_data/adult.test",
                                                          ",", ['$continuous$'], False)

# Test the data.
test_results = model.predict(test_ft_data)
score = naive_bayes.get_accuracy_score(test_cl_data, test_results)
print score
