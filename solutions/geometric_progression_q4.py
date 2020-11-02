# -*- coding: utf-8 -*-
"""
Nth Term of Harmonic Progression
====================================

Module for finding the Nth term of Geometric progression given it's first 5 terms

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations

This script contains the following function
    * get_n_geometric_term - Function to find the Nth term of Geometric progression
"""
# Standard Imports
import logging

__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def get_n_geometric_term(vector, term_number):
    """
    Nth Term Of Geometric Progression- Function
    -----------------------------------------------
    
     Function to find the Nth term of Geometric progression given it's first 5 terms

    :param vector: The first five terms as a vector
    :type vector: list

    :param term_number: The Nth term of the harmonic sequence that needs to be found
    :type term_number: int

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

        # Checking if exactly first 5 terms are given
        if not len(vector) == 5:
            raise AttributeError("The number of given terms should be 5")

        # Checking if the required Nth term is of type integer and greater than 0
        if (not issubclass(type(term_number), int)) or term_number < 1:
            raise AttributeError("The term number should be integer and greater than zero")

        # Finding the ratio between all consecutive terms
        ratio = [vector[item+1] / vector[item] for item in range(4)]

        # Checking if they all have a common ratio
        ratio_check = all([round(ratio[0], 2) == round(ratio[item], 2) for item in range(4)])

        if not ratio_check:
            # If the the arithmetic sequence doesn't have a common sequence, then it is not an arithmetic sequence
            raise AttributeError("The given sequence is not a geometric sequence")

        # Finding the a element (first element of geometric sequence) and r element (common ratio)
        element_a = vector[0]
        element_r = ratio[0]

        # Finding the Nth arithmetic term
        n_term_geometric = element_a * (element_r ** (term_number - 1))

        LOGGER.info("The %s th Term of given Geometric progression is: %s", term_number, round(n_term_geometric, 4))
    except AttributeError as err:
        LOGGER.error(err)
