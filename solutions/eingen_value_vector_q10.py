# -*- coding: utf-8 -*-
"""
Module to Find Eigen Values and Eigen Vectors
=================================================

Module for Finding Eigen Values and Eigen Vectors of given matrix

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations
    * Numpy - Package with multi-dimensional arrays and matrices, along with a large collection of high-level
              mathematical functions to operate on these arrays

This script contains the following function
    * find_eigen_value_vector - Function to Find Eigen Values and Eigen Vectors of given matrix
"""
# Standard Imports
import logging

# External Imports
import numpy as np
from numpy import linalg as la


__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def find_eigen_value_vector(matrix):
    """
    Find Eigen Value and Eigen Vector-Function
    -----------------------------------------------
    
    Function Find Eigen Values and Eigen Vectors of given matrix

    :param matrix: Matrix as list of elements
    :type matrix: list

    :return: Nothing
    :rtype: None
    """
    try:
        # Checking if the Given matrix is of Type List
        if not issubclass(type(matrix), list):
            # If not, an error is raised
            raise AttributeError("Matrix Should be Given as a List of (list of) Vectors")

        # Checking if each vector within matrix are of type list and their elements
        # are of type int or float or complex
        for vector in matrix:

            # Checking if the Given Vector is of Type List
            if not issubclass(type(vector), list):
                # If not, an error is raised
                raise AttributeError("Vector Should be Given a List")

            if len(vector) != len(matrix[0]):
                raise AttributeError("The Vectors should be of same length")

            # Creating a map object with values either true (if the corresponding item is either integer or float or
            # complex) or false
            type_check = map(lambda arg: issubclass(type(arg), int) or issubclass(type(arg), float) or
                             issubclass(type(arg), complex), vector)

            # Checking if all the elements of the list is of type integer or float or complex
            if not all(type_check):
                # If not, an error is raised
                raise AttributeError("The Vector Elements Should be Integer or Float or complex")

        given_matrix = np.array(matrix)

        shape = given_matrix.shape

        if not (shape[0] == shape[1]):
            raise AttributeError("A non-square matrix is given")

        eigen_value, eigen_vector = la.eig(given_matrix)

        for value in range(len(eigen_value)):
            LOGGER.info("For the eigen value: %s, \n\nThe eigen vector is:\n\n%s\n\n", eigen_value[value],
                        eigen_vector[:, value])
    except AttributeError as err:
        LOGGER.error("AttributeError: %s", err)
