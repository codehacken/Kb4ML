__author__ = 'ashwin'
__email__ = 'gashwin1@umbc.edu'

""""
Implement Standard classifiers.
"""
# Implementing the std. Naive Bayes Algorithm.
# Classification is based on Maximum-Likelihood for selecting the final class.

from lib.stdops.fileops import FileReader
from sklearn.feature_extraction import DictVectorizer


class NaiveBayes:
    def __init__(self):
        self.feature_vector = None
        self.class_vector = None

    def vectorize_data(self, var_file_name, data_file_name, data_sep, var_filter, class_name="Classify"):
        file_reader = FileReader(class_var_name=class_name)
        file_reader.read_col_var_file(var_file_name, data_separator=data_sep)

        # Get the data in the file.
        [file_feature_data, file_class_result] = file_reader.read_data(data_file_name, data_sep, var_filter)

        self.feature_vector = DictVectorizer(sparse=False)
        transformed_feature_data = self.feature_vector.fit_transform(file_feature_data)

        return transformed_feature_data


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
