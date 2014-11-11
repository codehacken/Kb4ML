__author__ = 'ashwin'
__email__ = 'gashwin1@umbc.edu'

""""
Implement Standard classifiers.
"""
# Implementing the std. Naive Bayes Algorithm.
# Classification is based on Maximum-Likelihood for selecting the final class.


class NaiveBayes:
    def __init__(self, var_names, class_var_name):
        self.factor_freq = {}
        self.result_freq = {}
        self.__reset__(var_names, class_var_name)

    # The __reset__ method is used to reset the trained model vector.
    # This resets all the frequency counts to 0.
    def __reset__(self, var_names, class_var_name):
        # Setup the factor_freq mapping.
        for var in var_names:
            if var != class_var_name:
                self.factor_freq[var] = {}
                for var_category in var_names[var]:
                    self.factor_freq[var][var_category] = {}
                    for class_category in var_names[class_var_name]:
                        self.factor_freq[var][var_category][class_category] = 0

        # Setup for the frequency mapping for the resultant categories.
        for class_category in var_names[class_var_name]:
            self.result_freq[class_category] = 0

    @staticmethod
    def train_model(training_data):
        # Create a counter for each combination for a specific class value.
        # Probability is calculated as a n(X1) / n(S).
        for data_point in training_data:
            for data_point_val in data_point:
                #self.factor_freq[data_point_val][data_point[data_point_val]][data_point[]]
                print data_point_val