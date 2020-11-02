# -*- coding: utf-8 -*-
"""
Descriptive Stats of Time Series Data Main
==========================================

Main Module for Module for computing the min, max, mean and median for a given time-series data:
                        a. For every hour
                        b. For every day
                        c. For every month

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations

This script contains the following function

    * main - main function to call appropriate functions to compute all the stats
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
    Main function to call appropriate functions to compute all the stats
    
    :return: Nothing
    :rtype: None
    """

    # Getting the path for logging config using arparse
    log_config_file = helper.ARGUMENTS.logfile

    # Configuring logging
    helper.configure_logging(log_config_file)

    solutions.get_stats(helper.ARGUMENTS.inputfile)


if __name__ == '__main__':
    main()
