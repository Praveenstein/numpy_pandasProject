# -*- coding: utf-8 -*-
"""
L1 & L2 Norm of a Vector Main
=================================

Main Module for Finding the L1 and L2 norm of a given vector

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations

This script contains the following function

    * main - main function to call appropriate functions to Find the L1 and L2 Norm of a given vector
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
    Main function to

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
    solutions.find_l1_norm(input_vector)

    # Finding the L2 Norm of given vector
    solutions.find_l2_norm(input_vector)


if __name__ == '__main__':
    main()
