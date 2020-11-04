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
    solutions.plot_curves(helper.ARGUMENTS.x_min_cs, helper.ARGUMENTS.x_max_cs, helper.ARGUMENTS.x_min_sig,
                          helper.ARGUMENTS.x_max_sig, helper.ARGUMENTS.no_points, helper.ARGUMENTS.width,
                          helper.ARGUMENTS.height)


if __name__ == '__main__':
    main()
