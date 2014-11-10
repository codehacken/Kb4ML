__author__ = 'ashwin'
__email__ = 'gashwin1@umbc.edu'

""""
Standard File Operations.
"""


class FileReader:
    def __init__(self, column_var=None):
        self.col_var = column_var

    def read_col_var_file(self, filename, separator=","):
        """
        FILE DESIGN:
        variable name list at the start of the file.
        <var1>,<var 2>,<var 3>

        :param filename: Name of the file which contains the list of variables.
        :return: No return value.
        """
        with open(filename, "r") as file_ptr:
            self.col_var = file_ptr.readline().split("\n")[0].split(separator)

    def read_data(self, filename, separator=","):
        """
        FILE DESIGN:
        The file is a CSV file which contains data in the following format.
        <val1>,...,<valN>

        :param filename:
        :return: data map.
                 [Row Y{col(x): val(x,y)}]
        """
        file_data = []

        with open(filename, "r") as file_ptr:
            for line in file_ptr:
                col_val_map = {}
                col_val_list = line.split("\n")[0].split(separator)

                # Assign the values to each column.
                for idx, col_val in enumerate(col_val_list):
                    col_val_map[self.col_var[idx]] = col_val

                file_data.append(col_val_map)

        return file_data
