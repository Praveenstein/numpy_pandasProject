# -*- coding: utf-8 -*-
"""
Dot Product Of All Given Vectors
====================================

Module to Find the Dot Product Of all Given Vectors

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations

This script contains the following function
    * find_dot_product - Function to find the dot product of given vectors
"""
# Standard Imports
import logging

# External Imports
import numpy as np

__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def find_dot_product(vectors):
    """
    Dot Product Function
    ------------------------
    
    Function to find the dot product of all given vectors

    Eg: let, a = [1, 2], b = [2, 4], c = [1, 3]
    Then,
            find_dot_product([[1, 2],
                              [2, 4],
                              [1, 3]])
    Would Result In: (1*2*1) + (2*4*3) = 26

    :param vectors: List of Vectors for which the dot product needs to found out
    :type vectors: list

    :return: Nothing
    :rtype: None
    """
    try:
        # Checking if the Given Vectors is of Type List
        if not issubclass(type(vectors), list):
            # If not, an error is raised
            raise AttributeError("Vectors Should be Given as a List of Vector")

        # Checking if each vector within the list of vectors are of type list and their elements
        # are of type int or float
        for vector in vectors:

            # Checking if the Given Vector is of Type List
            if not issubclass(type(vector), list):
                # If not, an error is raised
                raise AttributeError("Vector Should be Given a List")

            # Creating a map object with values either true (if the corresponding item is either integer or float)
            # or false
            type_check = map(lambda arg: issubclass(type(arg), int) or issubclass(type(arg), float), vector)

            # Checking if all the elements of the list is of type integer or float
            if not all(type_check):
                # If not, an error is raised
                raise AttributeError("The Vector Elements Should be Integer or Float")

        # Checking If all vectors are of same length
        len_of_vector = all([len(vectors[0]) == len(item) for item in vectors])
        if not len_of_vector:
            raise AttributeError("All vectors should be of equal length")

        vector_matrix = np.array(vectors)

        dot_product = np.sum(np.prod(vector_matrix, axis=0))

        LOGGER.info(" The Dot Product of all given vectors \n %s is: %s", vector_matrix, dot_product)
    except AttributeError as err:
        LOGGER.error("AttributeError: %s", err)
