# -*- coding: utf-8 -*-
"""
Module to Plot, sine, cosine and sigmoid functions
======================================================

Module for to Plotting, sine, cosine and sigmoid functions

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations
    * Numpy - Package with multi-dimensional arrays and matrices, along with a large collection of high-level
              mathematical functions to operate on these arrays

This script contains the following function
    * plot_curves - Function to to Plot, sine, cosine and sigmoid functions
"""
# Standard Imports
import logging

# External Imports
import numpy as np
import matplotlib.pylab as plt

__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def plot_curves(x_min_cs, x_max_cs, x_min_sig, x_max_sig, no_points=100, width=1920, height=1080):
    """
    Plot, sine, cosine and sigmoid functions- Function
    ------------------------------------------------------
    
     Function to to Plot, sine, cosine and sigmoid functions

    :param x_min_cs: The minimum value of x axis for cos and sine function
    :type x_min_cs: Union[int, float]

    :param x_max_cs: The Maximum value of x axis for cos and sine function
    :type x_max_cs: Union[int, float]

    :param x_min_sig: The minimum value of x axis for Sigmoid function
    :type x_min_sig: Union[int, float]

    :param x_max_sig: The Maximum value of x axis for Sigmoid function
    :type x_max_sig: Union[int, float]

    :param no_points: The Number of points between given range
    :type no_points: int

    :param width: The width of figure in pixels
    :type width: int

    :param height: The height of figure in pixels
    :type height: int

    :return: Nothing
    :rtype: None
    """
    try:
        # Checking if the Given Vector is of Type List
        if (not isinstance(x_min_cs, int)) and (not isinstance(x_min_cs, float)):
            raise AttributeError("The Minimum Values of cos, sine function should be int or float")

        if (not isinstance(x_max_cs, int)) and (not isinstance(x_max_cs, float)):
            raise AttributeError("The Maximum Values of cos, sine function should be int or float")

        if (not isinstance(x_min_sig, int)) and (not isinstance(x_min_sig, float)):
            raise AttributeError("The Minimum Values of Sigmoid function should be int or float")

        if (not isinstance(x_max_sig, int)) and (not isinstance(x_max_sig, float)):
            raise AttributeError("The Maximum Values of Sigmoid function should be int or float")

        if not isinstance(no_points, int):
            raise AttributeError("The number of points should be of type int")

        if not isinstance(width, int):
            raise AttributeError("The width should be of type int")

        if not isinstance(height, int):
            raise AttributeError("The height should be of type int")

        # Creating the X axis and Y axis Points for all three curves
        x_axis_cs = np.linspace(x_min_cs, x_max_cs, no_points)
        y_axis_sin = np.sin(x_axis_cs)
        y_axis_cos = np.cos(x_axis_cs)

        x_axis_sigmoid = np.linspace(x_min_sig, x_max_sig, no_points)
        y_axis_sig = 1 / (1 + np.exp(-x_axis_sigmoid))

        # Creating plots for the sin function
        plt.figure(figsize=(width / 96, height / 96), dpi=96)
        plt.plot(x_axis_cs, y_axis_sin)
        #plt.savefig("sin.jpg", dpi=96)
        plt.show()

        # Creating plots for the cos function
        plt.figure(figsize=(width / 96, height / 96), dpi=96)
        plt.plot(x_axis_cs, y_axis_cos)
        #plt.savefig("cos.jpg", dpi=96)
        plt.show()

        # Creating plots for the sigmoid function
        plt.figure(figsize=(width / 96, height / 96), dpi=96)
        plt.plot(x_axis_sigmoid, y_axis_sig)
        #plt.savefig("sigmoid.jpg", dpi=96)
        plt.show()
    except AttributeError as err:
        LOGGER.error(err)
