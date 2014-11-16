__author__ = 'ashwin'
__email__ = 'gashwin1@umbc.edu'

"""
All Test Code.
"""
from lib.models.classify import NaiveBayes
data_sep = ","
elim_var = ['$continuous$']


def test_naive_bayes(train_file_reader, test_file_reader):
    # Create a Bernoulli NB.
    naive_bayes = NaiveBayes()

    # Vectorize the training data for Naive Bayes.
    [train_ft_data, train_cl_data] = naive_bayes.vectorize_data(train_file_reader.file_feature_data,
                                                                train_file_reader.file_class_result)

    # Train the model.
    model = naive_bayes.train_model(train_ft_data, train_cl_data)

    # Vectorize the test data.
    [test_ft_data, test_cl_data] = naive_bayes.vectorize_data(test_file_reader.file_feature_data,
                                                              test_file_reader.file_class_result,
                                                              False)

    # Test the data.
    test_results = model.predict(test_ft_data)
    score = naive_bayes.get_accuracy_score(test_cl_data, test_results)

    return score


def test_nb_cross_product(train_file_reader, test_file_reader, cross_prod_columns):
    # Create a Bernoulli NB.
    naive_bayes = NaiveBayes()

    # Create a Cross-product between two columns.
    cross_train_ft_data = train_file_reader.cross_prod_var(train_file_reader.file_feature_data,
                                                           cross_prod_columns)

    # Vectorize the training data for Naive Bayes.
    [train_ft_data, train_cl_data] = naive_bayes.vectorize_data(cross_train_ft_data,
                                                                train_file_reader.file_class_result)

    # Train the model.
    model = naive_bayes.train_model(train_ft_data, train_cl_data)

    cross_test_ft_data = test_file_reader.cross_prod_var(test_file_reader.file_feature_data,
                                                         cross_prod_columns)
    # Vectorize the test data.
    [test_ft_data, test_cl_data] = naive_bayes.vectorize_data(cross_test_ft_data,
                                                              test_file_reader.file_class_result,
                                                              False)

    # Test the data.
    test_results = model.predict(test_ft_data)
    score = naive_bayes.get_accuracy_score(test_cl_data, test_results)

    return score
