__author__ = 'ashwin'
__email__ = 'gashwin1@umbc.edu'

""""
Implement Standard classifiers.
"""
# Implementing the std. Naive Bayes Algorithm.
# Classification is based on Maximum-Likelihood for selecting the final class.

from lib.stdops.fileops import FileReader
from sklearn.feature_extraction import DictVectorizer
from sklearn.naive_bayes import BernoulliNB
import numpy as np
from sklearn import metrics


class NaiveBayes:
    def __init__(self):
        self.feature_vector = DictVectorizer(sparse=False)
        self.class_vector = {}
        self.nb_model = BernoulliNB()
        self.class_var = None

    # This function converts a set of class variable values to integer eq.
    # This is can then be used as the class ID.
    def data2vector(self, class_data, reset=False):
        if reset:
            self.class_vector = {}

        # The final vector of integer for the class variables.
        transform_vector = []

        # The conversion is a simple one taking values from 0 to
        # x where x+1 type of values are there for the class variable.
        idx = 0
        for data_point in class_data:
            if data_point[data_point.keys()[0]] not in self.class_vector:
                self.class_vector[data_point[data_point.keys()[0]]] = idx
                idx += 1

            transform_vector.append(self.class_vector[data_point[data_point.keys()[0]]])

        return np.array(transform_vector)

    def vectorize_data(self, var_file_name, data_file_name, data_sep, var_filter, if_train=True, class_name="Classify"):
        file_reader = FileReader(class_var_name=class_name)
        file_reader.read_col_var_file(var_file_name, data_separator=data_sep)

        # Get the data in the file.
        [file_feature_data, file_class_result] = file_reader.read_data(data_file_name, data_sep, var_filter)

        # Vectorize the training data.
        if if_train:
            transformed_feature_data = self.feature_vector.fit_transform(file_feature_data)
        else:
            transformed_feature_data = self.feature_vector.transform(file_feature_data)

        # Vectorize the training data results (that is the class results applied to the same set)
        transformed_class_data = self.data2vector(file_class_result)

        return [transformed_feature_data, transformed_class_data]

    def train_model(self, ft_data, cl_data):
        return self.nb_model.fit(ft_data, cl_data)

    def predict(self, ft_data):
        return self.nb_model.predict(ft_data)

    @staticmethod
    def get_accuracy_score(train_cl_real, test_cl_predict):
        return metrics.accuracy_score(train_cl_real, test_cl_predict)

"""
Sample Code:
Using NB Created. Use File Reader to read the file and get the data.
                  file_data is then passed to the Naive Bayes to train the model.

naive_b = NaiveBayes(file_reader.col_var, file_reader.class_var)
naive_b.train_model(file_data)
"""


class DiscreteNaiveBayes:
    def __init__(self, var_names, class_var_name):
        self.factor_freq = {}
        self.result_freq = {}
        self.class_var_name = class_var_name
        self.__reset__(var_names)

    # The __reset__ method is used to reset the trained model vector.
    # This resets all the frequency counts to 0.
    def __reset__(self, var_names):
        # Setup the factor_freq mapping.
        for var in var_names:
            if var != self.class_var_name:
                self.factor_freq[var] = {}
                for var_category in var_names[var]:
                    self.factor_freq[var][var_category] = {}
                    for class_category in var_names[self.class_var_name]:
                        self.factor_freq[var][var_category][class_category] = 0

        # Setup for the frequency mapping for the resultant categories.
        for class_category in var_names[self.class_var_name]:
            self.result_freq[class_category] = 0

    # Create the NB model basing on training data.
    def train_model(self, training_data):
        # Create a counter for each combination for a specific class value.
        # Probability is calculated as a n(X1) / n(S).
        for data_point in training_data:
            for data_point_val in data_point:
                if data_point_val != self.class_var_name:
                    self.factor_freq[data_point_val][data_point[data_point_val]][data_point[self.class_var_name]] += 1

            self.result_freq[data_point[self.class_var_name]] += 1

    """
    TBD: Using the trained model to calculate prob. for the test data.
    """
