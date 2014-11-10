__author__ = 'ashwin'
__email__ = 'gashwin1@umbc.edu'

""""
Standard File Operations.
"""


class FileReader:
    def __init__(self):
        col_var = {}
        data = {}

    def read_col_var_file(self, filename):
        """
        FILE DESIGN:
        variable name list at the start of the file.
        <var1>,<var 2>,<var 3>

        :param filename: Name of the file which contains the list of variables.
        :return: No return value.
        """
        with open(filename, "r") as file_ptr:
            col_var_list = file_ptr.readline().split("\n")[0]
            print col_var_list
