# -*- coding: utf-8 -*-
"""
Module to find SMA, EM of Given Array
==========================================

Module for finding the simple moving average(SMA), expanding window average(EM) of Given Array

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations

This script contains the following function
    * find_sma_em - Function to find the simple moving average(SMA), expanding window average(EM) of Given Array
"""
# Standard Imports
import logging

# External Imports
import pandas as pd

__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def find_sma_em(array, stride_length):
    """
    Find SMA & EM-Function
    -----------------------------------------------
    
    Function to find the simple moving average(SMA), expanding window average(EM) of Given Array

    :param array: The array for which the SMA & EM are to be found
    :type array: list

    :param stride_length: The fixed window length
    :type stride_length: int

    :return: Nothing
    :rtype: None
    """
    try:
        # Checking if the Given Vector is of Type List
        if not issubclass(type(array), list):
            # If not, an error is raised
            raise AttributeError("Array Should be Given as a List")

        # Creating a map object with values either true (if the corresponding item is either integer or float) or false
        type_check = map(lambda arg: issubclass(type(arg), int) or issubclass(type(arg), float), array)

        # Checking if all the elements of the list is of type integer or float
        if not all(type_check):
            # If not, an error is raised
            raise AttributeError("The Array Elements Should be Integer or Float")

        if (not isinstance(stride_length, int)) or stride_length < 2:
            raise AttributeError("Stride length should be of type integer and greater than 1")

        # Creating a Dataframe from the given array
        given_array = pd.DataFrame(array)

        # Calculating the simple moving average
        given_array['SMA'] = given_array.iloc[:, 0].rolling(window=stride_length).mean()

        # Calculating the expanding window mean
        given_array['EM'] = given_array.iloc[:, 0].expanding().mean()

        LOGGER.info("The SMA and EM for the given array are: \n%s\n", given_array)
    except AttributeError as err:
        LOGGER.error("AttributeError: %s", err)
