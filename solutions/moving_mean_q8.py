# -*- coding: utf-8 -*-
"""
Module to find SMA, EM of Given Array
==========================================

Module for finding the simple moving average(SMA), expanding window average(EM) of Given Array

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations
    *pandas - This provides the Data structures and operations for manipulating numerical tables and time series

This script contains the following function
    * find_sma_em - Function to find the simple moving average(SMA), expanding window average(EM) of Given Array
"""
# Standard Imports
import logging

# External Imports
import pandas as pd
import numpy as np

__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def find_sma_em(array, strides=3, window_length=4):
    """
    Find SMA & EM-Function
    ------------------------------
    
    Function to find the simple moving average(SMA), expanding window average(EM) of Given Array

    :param array: The array for which the SMA & EM are to be found
    :type array: list

    :param strides: The stride length
    :type strides: Union[int, list]

    :param window_length: The window length
    :type window_length: int

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

        if (not isinstance(window_length, int)) or window_length < 2:
            raise AttributeError("window length should be of type integer and greater than 1")

        if (not isinstance(strides, int)) and (not isinstance(strides, list)):
            raise AttributeError("Stride Should be given as int or list ")

        # Creating a Dataframe from the given array
        given_array = pd.DataFrame(array)

        # Calculating the simple moving average
        given_array['SMA'] = given_array.iloc[:, 0].rolling(window=window_length).mean()

        if isinstance(strides, int):
            created_strides = [strides] * len(given_array)
        else:
            created_strides = strides

        # Creating the list of indices for which the moving average needs to be found
        # With first value equal to window_length -1
        indices = [window_length-1]

        for stride in created_strides:
            # The next index would be previous index + stride
            new_inde = indices[-1] + stride
            if new_inde > len(given_array) - 1:
                # If the new index exceeds the length of data, then the loop is broken
                break
            indices.append(new_inde)

        given_array.loc[given_array.index.isin(indices), 'SMA_WITH_STRIDE'] = \
            given_array.iloc[:, 0].rolling(window=window_length).mean()

        # Calculating the expanding window mean
        given_array['EM'] = given_array.iloc[:, 0].expanding().mean()

        LOGGER.info("The SMA and EM for the given array are: \n%s\n", given_array.iloc[:25, :])
    except AttributeError as err:
        LOGGER.error("AttributeError: %s", err)
