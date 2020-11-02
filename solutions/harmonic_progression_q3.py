# -*- coding: utf-8 -*-
"""
Nth Term of Harmonic Progression
====================================

Module for finding the Nth term of harmonic progression given it's first 5 terms

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations

This script contains the following function
    * get_n_harmonic_term - Function to find the Nth term of harmonic progression
"""
# Standard Imports
import logging

__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def get_n_harmonic_term(vector, term_number):
    """
    Nth Term Of Harmonic Progression- Function
    -----------------------------------------------
    
     Function to find the Nth term of harmonic progression given it's first 5 terms

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

        # Creating an arithemetic sequenc from the given harmonic sequence
        arth_sequence = list(map(lambda arg: 1/arg, vector))

        # Finding the difference between all consecutive terms
        difference = [arth_sequence[item+1] - arth_sequence[item] for item in range(4)]

        # Checking if they all have a common difference
        difference_check = all([round(difference[0], 2) == round(difference[item], 2)
                                for item in range(len(difference))])

        if not difference_check:
            # If the the arithmetic sequence doesn't have a common sequence, then it is not an arithmetic sequence
            raise AttributeError("The given sequence is not a harmonic sequence")

        # Finding the a element (first element of arithmetic sequence) and d element (common difference)
        element_a = arth_sequence[0]
        element_d = difference[0]

        # Finding the Nth arithmetic term
        n_term_arithmetic = element_a + ((term_number - 1) * element_d)

        # Finding the Nth Harmonic Term by taking reciprocal of the Nth arithmetic term
        n_term_harmonic = 1/n_term_arithmetic
        LOGGER.info("The %s th Term of given harmonic progression is: %s", term_number, round(n_term_harmonic, 4))
    except AttributeError as err:
        LOGGER.error(err)
