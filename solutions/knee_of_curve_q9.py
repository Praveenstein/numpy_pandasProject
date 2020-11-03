# -*- coding: utf-8 -*-
"""
Module to Find the Knee of Curve
=================================

Module for Finding Knee of Curve

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations

This script contains the following function
    * find_knee_index - Function to Find the Knee of given data points
    * find_knee_index - Function to
    * find_knee_index - Function to
"""
# Standard Imports
import logging

# External Imports
import numpy as np
import matplotlib.pylab as plt

__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def find_knee_index(data, theta):
    """
    Find Knee-Function
    --------------------------
    
    Function which rotate the given points by angle theta and then finds the min / max to get the
    Knee of the curve

    :param data: The array consisting of 2D points of the curve
    :type data: :class:`numpy.ndarray`

    :param theta: The angle in radians to rotate the given points
    :type theta: float

    :return: knee index
    :rtype: int
    """
    try:
        if not isinstance(data, np.ndarray):
            raise AttributeError("The given data should be of type numpy array")

        if not isinstance(theta, float) or not isinstance(theta, np.float64):
            raise AttributeError("The given angle should be of type float or np.float64")

        data_shape = data.shape

        # make rotation matrix
        cos_fun = np.cos(theta)
        sin_fun = np.sin(theta)
        rotation_matrix = np.array(((cos_fun, -sin_fun), (sin_fun, cos_fun)))

        # rotate data vector
        rotated_vector = data.dot(rotation_matrix)

        LOGGER.info("Plotting the Data Before Finding The Index")
        plt.scatter(rotated_vector[:, 0], rotated_vector[:, 1])
        plt.show()

        # Setting knee to be the index where the Y- Axis values are minimum
        knee = np.argmin(rotated_vector[:, 1])

        # If the knee is set to the last or first index, then it should have been a convex curve
        if knee == 0 or knee == (data_shape[0] - 1):
            # Hence we find the index where the values are max
            knee = np.argmax(rotated_vector[:, 1])

        return knee
    except AttributeError as err:
        LOGGER.error(err)


def get_data_radiant(data):
    """
    Function to get the angel in radians such that the slope of line joining the two extremes of the curve is zero,
    when rotated by this angle

    :param data: The array consisting of 2D points of the curve
    :type data: :class:`numpy.ndarray`

    :return: Angle in radians
    :rtype: :class:`numpy.float64`
    """
    try:
        if not isinstance(data, np.ndarray):
            raise AttributeError("The given data should be of type numpy array")

        return np.arctan2(data[:, 1].max() - data[:, 1].min(),
                          data[:, 0].max() - data[:, 0].min())
    except AttributeError as err:
        LOGGER.error(err)


def plot_knee(data_points):
    """
    Function to get input data, and find the corresponding angle of rotation, and then get the knee value and plot it

    :param data_points: List of data points for which the knee has to be found
    :type data_points: list

    :return: Nothing
    :rtype: None
    """

    # Checking if the Given Vectors is of Type List
    if not issubclass(type(data_points), list):
        # If not, an error is raised
        raise AttributeError("Vectors Should be Given as a List of Vector")

    # Checking if each vector within the list of vectors are of type list and their elements
    # are of type int or float
    for vector in data_points:

        # Checking if the Given Vector is of Type List
        if not issubclass(type(vector), list):
            # If not, an error is raised
            raise AttributeError("Vector Should be Given a List")

        if len(vector) != 2:
            raise AttributeError("The points should be from a 2D Plane")

        # Creating a map object with values either true (if the corresponding item is either integer or float)
        # or false
        type_check = map(lambda arg: issubclass(type(arg), int) or issubclass(type(arg), float), vector)

        # Checking if all the elements of the list is of type integer or float
        if not all(type_check):
            # If not, an error is raised
            raise AttributeError("The Vector Elements Should be Integer or Float")

    # Creating numpy array from given list
    data = np.array(data_points)

    LOGGER.info("Plotting the Data Before Finding The Index")

    plt.scatter(data[:, 0], data[:, 1])
    plt.show()

    # Finding the Knee Index
    knee_index = find_knee_index(data, get_data_radiant(data))

    LOGGER.info(" The Index of Knee For the Given Data Points is: %s", knee_index)
    LOGGER.info(" The Data Points at Knee Index are: %s", data[knee_index])

    LOGGER.info("Plotting the Data After Finding the Knee")

    plt.scatter(data[:, 0], data[:, 1])
    plt.vlines(data[knee_index, 0], ymin=data[:, 1].min(), ymax=data[:, 1].max(), colors='red', linestyles='--')
    plt.show()
