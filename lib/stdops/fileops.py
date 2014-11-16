__author__ = 'ashwin'
__email__ = 'gashwin1@umbc.edu'

""""
Standard File Operations.
"""


class FileReader:
    def __init__(self, column_var={}, idx2var=[], class_var_name="Classify"):
        self.col_var = column_var
        self.idx2var = idx2var
        self.class_var = class_var_name

        # Dispatch table to convert words to idx positions.
        self.class_pos = {
            'last': lambda: len(self.col_var) - 1,
            'first': 0
        }

        # Store the file data.
        self.file_feature_data = None
        self.file_class_result = None

    def read_col_var_file(self, filename, var_separator=":", data_separator=","):
        """
        FILE DESIGN:
        variable name list at the start of the file.
        <var1>:<value1>,<value2>,
        <var 2>:
        <var 3>:

        :param filename: Name of the file which contains the list of variables.
        :return: No return value.
        """
        with open(filename, "r") as file_ptr:
            for line in file_ptr:
                var_list = line.split("\n")[0].split(var_separator)
                self.col_var[var_list[0]] = var_list[1].split(data_separator)
                self.idx2var.append(var_list[0])

    def read_data(self, filename, separator=",", var_filter=None, class_result_pos="last"):
        """
        FILE DESIGN:
        The file is a CSV file which contains data in the following format.
        <val1>,...,<valN>

        :param filename:
        :return: data map.
                 [Row Y{col(x): val(x,y)}]
        """

        # 1. var_filter contains the variable type which are having a $<name>$.
        # 2. filtered_var_idx is the filtered variable list that contains only the variables that
        #    are to be filtered out.

        if type(class_result_pos) == str:
            class_idx = self.class_pos[class_result_pos]()
        elif type(class_result_pos) == int:
            class_idx = class_result_pos

        filtered_var_idx = []
        for idx, var in enumerate(self.idx2var):
            for filter_item in var_filter:
                if self.col_var[var][0] == filter_item:
                    filtered_var_idx.append(idx)

        # read and filter the data.
        file_feature_data = []
        file_class_result = []

        with open(filename, "r") as file_ptr:
            for line in file_ptr:
                col_val_map = {}
                col_val_list = line.split("\n")[0].split(separator)

                # Assign the values to each column.
                for idx in range(0, len(col_val_list) - 1):
                    if not(filtered_var_idx.__contains__(idx)):
                        col_val_map[self.idx2var[idx]] = col_val_list[idx]

                file_feature_data.append(col_val_map)
                file_class_result.append({self.class_var: col_val_list[class_idx]})

        self.file_feature_data = file_feature_data
        self.file_class_result = file_class_result

    # cross_col_list contains the list of column names which need to be concatenated
    # so that a cross product can be calculated.

    # The current cross product method works mainly for discrete data.
    def cross_prod_var(self, file_feature_data, cross_col_list):
        # Construct the set of cross product columns.
        # cross_product_col is the name of the new cross product column (AxB).
        cross_product_col_list = []
        cross_prod_col_idx = []

        for col_list in cross_col_list:
            cross_product_col = "_"
            for col in col_list:
                cross_product_col += col + "_"
                cross_prod_col_idx.append(self.idx2var.index(col))
            cross_product_col_list.append(cross_product_col)

        cross_ft_data = []
        for data_point in file_feature_data:
            # Construct the cross product variables.
            new_data_point = {}
            for idx, col_list in enumerate(cross_col_list):
                data_point_cross_prod = "_"
                for col in col_list:
                    data_point_cross_prod += data_point[col] + "_"

                # Add the cross product to the new data point.
                new_data_point[cross_product_col_list[idx]] = data_point_cross_prod

            # Add the other variables.
            for var in data_point:
                if self.idx2var.index(var) not in cross_prod_col_idx:
                    new_data_point[var] = data_point[var]

            # Add the new data point to the data set.
            cross_ft_data.append(new_data_point)

        return cross_ft_data
