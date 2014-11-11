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

    def read_data(self, filename, separator=",", var_filter=None):
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

        filtered_var_idx = []
        for idx, var in enumerate(self.idx2var):
            for filter_item in var_filter:
                if self.col_var[var][0] == filter_item:
                    filtered_var_idx.append(idx)

        # read and filter the data.
        file_data = []

        with open(filename, "r") as file_ptr:
            for line in file_ptr:
                col_val_map = {}
                col_val_list = line.split("\n")[0].split(separator)

                # Assign the values to each column.
                for idx, col_val in enumerate(col_val_list):
                    if not(filtered_var_idx.__contains__(idx)):
                        col_val_map[self.idx2var[idx]] = col_val

                file_data.append(col_val_map)

        return file_data
