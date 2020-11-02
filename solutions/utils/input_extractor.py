# -*- coding: utf-8 -*-
"""
Vector Extractor Module
=================================

Module for extracting the input vector from a file and convert them to float

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations

This script contains the following function
    * get_vector_from_file - Function to extract the input vector from a file and convert them to float
    * get_matrix_from_file - Function to extract the input vectors (matrix of vector) from a file and convert them to
                             float
"""
# Standard Imports
import logging

__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def get_vector_from_file(filepath):
    """
    Function to Extract the Vector from a file and convert them to type float

    :param filepath: The path of input file consisting of the vectors
    :type filepath: str

    :return: The vectors as a list of float
    :rtype: list
    """

    try:
        with open(filepath, 'r') as file_object:
            input_data = file_object.read()

        input_data = input_data.split(",")
        input_data = list(map(lambda arg: float(arg), input_data))
        return input_data
    except FileNotFoundError as err:
        LOGGER.error("FileNotFoundError: %s", err)
        raise
    except ValueError as err:
        # This will be raised if the elements of the list cannot be converted to float, such as a conversion from
        # String to float
        LOGGER.error("ValueError: %s", err)
        raise


def get_matrix_from_file(filepath):
    """
    Function to extract the input vectors (matrix of vector) from a file and convert their elements to float

    :param filepath: The path of input file consisting of the vectors
    :type filepath: str

    :return: The vectors as a list of list
    :rtype: list
    """

    try:
        with open(filepath, 'r') as file_object:
            input_data = []
            for lines in file_object:
                input_line = lines
                input_line = input_line.split(",")
                input_line = list(map(lambda arg: float(arg.rstrip("\n")), input_line))
                input_data.append(input_line)
        return input_data
    except FileNotFoundError as err:
        LOGGER.error("FileNotFoundError: %s", err)
        raise
    except ValueError as err:
        # This will be raised if the elements of the list cannot be converted to float, such as a conversion from
        # String to float
        LOGGER.error("ValueError: %s", err)
        raise
