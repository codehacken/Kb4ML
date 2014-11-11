__author__ = 'ashwin'
__email__ = 'gashwin1@umbc.edu'

""""
Implement Standard classifiers.
"""


class NaiveBayes:
    def __init__(self):
        self.factor_freq = {}
        self.result_freq = {}

    def train_model(self, var_names, training_data):
