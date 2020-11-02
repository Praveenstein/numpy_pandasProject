# -*- coding: utf-8 -*-
"""
Nth Geometric Term Main
==========================================

Main Module for finding the Nth term of Geometric progression given it's first 5 terms

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations

This script contains the following function

    * main - main function to call appropriate functions to find the Nth term of Geometric progression given it's first
             5 terms

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
    Main function to find the Nth term of Geometric progression given it's first 5 terms

    :return: Nothing
    :rtype: None
    """

    # Getting the path for logging config using arparse
    log_config_file = helper.ARGUMENTS.logfile

    # Configuring logging
    helper.configure_logging(log_config_file)

    # Extract the Input Vector from file
    input_vector = helper.get_vector_from_file(helper.ARGUMENTS.inputfile)

    # Finding the L1 Norm of given vector
    solutions.get_n_geometric_term(input_vector, 6)


if __name__ == '__main__':
    main()
