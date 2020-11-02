# -*- coding: utf-8 -*-
"""
Dot Product Main
======================

Main Module for Finding the Dot Product of all given vectors

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations

This script contains the following function

    * main - main function to call appropriate functions to get the input vectors and find dot product of them
"""
# Standard imports
import logging

# External Imports

# User Imports
import solutions.utils as helper
import solutions

__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def main():
    """
    Main function to to get the input vectors and find dot product of them
    
    :return: Nothing
    :rtype: None
    """

    # Getting the path for logging config using arparse
    log_config_file = helper.ARGUMENTS.logfile

    # Configuring logging
    helper.configure_logging(log_config_file)

    # Extract the Input Vectors from file
    input_vectors = helper.get_matrix_from_file(helper.ARGUMENTS.inputfile)

    # Finding the Dot Product of All Given Vectors
    solutions.find_dot_product(input_vectors)


if __name__ == '__main__':
    main()
