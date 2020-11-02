# -*- coding: utf-8 -*-
"""
Find Eigen Values and Eigen Vectors Main
==============================================

Main Module for Finding Eigen Values and Eigen Vectors of given matrix

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations

This script contains the following function

    * main - main function to call appropriate functions to Find the Eigen Values and Eigen Vectors of given matrix
"""
# Standard imports
import logging

# User Imports
import solutions.utils as helper
import solutions

__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def main():
    """
    Main function to 
    
    :return: Nothing
    :rtype: None
    """

    # Getting the path for logging config using arparse
    log_config_file = helper.ARGUMENTS.logfile

    # Configuring logging
    helper.configure_logging(log_config_file)

    # Extract the Input Vector from file
    input_matrix = helper.get_complex_matrix_from_file(helper.ARGUMENTS.inputfile)

    solutions.find_eigen_value_vector(input_matrix)


if __name__ == '__main__':
    main()
