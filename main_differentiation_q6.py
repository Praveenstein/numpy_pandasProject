# -*- coding: utf-8 -*-
"""
Find the Derivative of Some functions Main
==============================================

Main Module for Finding the Derivative of Some functions

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations

This script contains the following function

    * main - main function to call appropriate functions to Find the Derivative of Some functions
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
    Main function to Find the Derivative of Some functions
    
    :return: Nothing
    :rtype: None
    """

    # Getting the path for logging config using arparse
    log_config_file = helper.ARGUMENTS.logfile

    # Configuring logging
    helper.configure_logging(log_config_file)

    # Finding the derivatives of some functions
    solutions.find_derivatives()


if __name__ == '__main__':
    main()
