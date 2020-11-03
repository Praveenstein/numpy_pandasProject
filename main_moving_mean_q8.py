# -*- coding: utf-8 -*-
"""
Find SMA, EM of Given Array Main
==========================================

Main Module for finding the simple moving average(SMA), expanding window average(EM) of Given Array

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations

This script contains the following function

    * main - main function to call appropriate functions for finding the simple moving average(SMA), expanding window
             average(EM) of Given Array
"""
# Standard imports
import logging
import random

# User Imports
import solutions.utils as helper
import solutions

__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def main():
    """
    Main function for finding the simple moving average(SMA), expanding window  average(EM) of Given Array
    
    :return: Nothing
    :rtype: None
    """

    # Getting the path for logging config using arparse
    log_config_file = helper.ARGUMENTS.logfile

    # Configuring logging
    helper.configure_logging(log_config_file)

    input_vector = [random.randint(100, 500) for _ in range(100)]

    # Finding the SMA and EM of the given vector
    solutions.find_sma_em(input_vector, 4)


if __name__ == '__main__':
    main()
