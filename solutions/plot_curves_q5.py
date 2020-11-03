# -*- coding: utf-8 -*-
"""
Nth Term of Harmonic Progression
====================================

Module for finding the Nth term of Geometric progression given it's first 5 terms

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations
    * Numpy - Package with multi-dimensional arrays and matrices, along with a large collection of high-level
              mathematical functions to operate on these arrays

This script contains the following function
    * plot_curves - Function to find the Nth term of Geometric progression
"""
# Standard Imports
import logging

# External Imports
import numpy as np
import matplotlib.pylab as plt

__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def plot_curves(vector):
    """
    Nth Term Of Geometric Progression- Function
    -----------------------------------------------
    
     Function to find the Nth term of Geometric progression given it's first 5 terms

    :param vector: The first five terms as a vector
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

        # Creating the X axis and Y axis Points for all three curves
        x_axis = np.array(vector)
        y_axis_sin = np.sin(x_axis)
        y_axis_cos = np.cos(x_axis)
        y_axis_sig = 1 / (1 + np.exp(-x_axis))

        # Creating plots for the sin function
        plt.figure(figsize=(1920 / 96, 1080 / 96), dpi=96)
        plt.plot(x_axis, y_axis_sin)
        plt.savefig("sin.jpg", dpi=96)
        plt.show()

        # Creating plots for the cos function
        plt.figure(figsize=(1920 / 96, 1080 / 96), dpi=96)
        plt.plot(x_axis, y_axis_cos)
        plt.savefig("cos.jpg", dpi=96)
        plt.show()

        # Creating plots for the sigmoid function
        plt.figure(figsize=(1920 / 96, 1080 / 96), dpi=96)
        plt.plot(x_axis, y_axis_sig)
        plt.savefig("sigmoid.jpg", dpi=96)
        plt.show()
    except AttributeError as err:
        LOGGER.error(err)
