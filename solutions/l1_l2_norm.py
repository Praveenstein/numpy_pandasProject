# -*- coding: utf-8 -*-
"""
Module to Find the L1 Norm and L2  Norm of a Given Vector
=============================================================

Module for

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations

This script contains the following function
    * find_l1_norm - Function to Find the L1 Norm, also called as Manhattan Norm
    * find_l2_norm - Function to Find the L2 Norm, also called as the Euclidean Norm
"""
# Standard Imports
import logging

# External Imports
import numpy as np
from numpy.linalg import norm

# User Imports

__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def find_l1_norm(vector):
    """
    Function to Find the L1 Norm of a given Vector
    -----------------------------------------------

    The L1 norm is calculated as the sum of the absolute vector values

    Eg:         vector = [1, 2, -3]
                l1_norm(vector) = 1 + 2 + 3
                                =6

    :param vector: The Vector elements as a list
    :type vector: list

    :return: Nothing
    :rtype: None
    """
    try:
        # Checking if the Given Vector is of Type List
        if not issubclass(type(vector), list):
            # If not, an error is raised
            raise AttributeError("Vector Should be Given a List")

        # Creating a map object with values either true (if the corresponding item is either integer or float) or false
        type_check = map(lambda arg: issubclass(type(arg), int) or issubclass(type(arg), float), vector)

        # Checking if all the elements of the list is of type integer or float
        if not all(type_check):
            # If not, an error is raised
            raise AttributeError("The Vector Elements Should be Integer or Float")

        vector_array = np.array(vector)
        l1_norm = norm(vector_array, ord=1)
        LOGGER.info("The L1 Norm of given vector %s is: %s", vector, l1_norm)
    except AttributeError as err:
        LOGGER.error("AttributeError: %s", err)


def find_l2_norm(vector):
    """
    Function to Find the L2 Norm of a given Vector
    -----------------------------------------------

    The L2 norm is calculated as the square root of the sum of the squared vector values

    Eg:         vector = [1, 2, -3]
                l2_norm(vector) = sqrt(1^2 + 2^2 + 3^2)
                                = sqrt(1 + 4 + 9)
                                = sqrt(14)
                                = 3.7416

    :param vector: The Vector elements as a list
    :type vector: list

    :return: Nothing
    :rtype: None
    """
    try:
        # Checking if the Given Vector is of Type List
        if not issubclass(type(vector), list):
            # If not, an error is raised
            raise AttributeError("Vector Should be Given as a List")

        # Creating a map object with values either true (if the corresponding item is either integer or float) or false
        type_check = map(lambda arg: issubclass(type(arg), int) or issubclass(type(arg), float), vector)

        # Checking if all the elements of the list is of type integer or float
        if not all(type_check):
            # If not, an error is raised
            raise AttributeError("The Vector Elements Should be Integer or Float")

        vector_array = np.array(vector)
        l2_norm = norm(vector_array)
        LOGGER.info("The L2 Norm of given vector %s is: %s", vector, round(l2_norm, 4))
    except AttributeError as err:
        LOGGER.error("AttributeError: %s", err)