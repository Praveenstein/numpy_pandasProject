# -*- coding: utf-8 -*-
"""
Title Main
==========================================

Main Module for 

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations

This script contains the following function

    * main - main function to call appropriate functions to
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

    # Plotting the Curves
    colors = solutions.new_func(3, True)
    LOGGER.info(colors)


if __name__ == '__main__':
    main()
