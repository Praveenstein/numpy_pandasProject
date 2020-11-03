# -*- coding: utf-8 -*-
"""
Module to Find the Derivative of Some functions
====================================================

Module for Finding the Derivative of Some functions

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations

This script contains the following function
    * derivative - Function to find the derivative using the passed function
    * complex_function - A complex function for which a derivative will be found
    * find_derivatives - Function to find derivative of some common functions and complex function
"""
# Standard Imports
import logging

# External Imports
import numpy as np
import matplotlib.pylab as plt


# User Imports

__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def derivative(function, point, method='central', step_size=0.01):
    """Compute the difference formula for f'(a) with step size = step_size.
            Difference formula:
                central: f(a+h) - f(a-h))/2h
                forward: f(a+h) - f(a))/h
                backward: f(a) - f(a-h))/h

    :param function: Vectorized function of one variable
    :type function: object

    :param point: Compute derivative at x = point
    :type point: Union[float, :class:`numpy.ndarray`]

    :param method: Difference formula: 'forward', 'backward' or 'central'
    :type method: str

    :param step_size: Step size in difference formula
    :type step_size: float

    :return: The derivative of function at given point
    :rtype: float

    """
    if not isinstance(point, float) and not isinstance(point, np.ndarray) and not isinstance(point, int):
        raise AttributeError("The Input Parameter Point is of incorrect type")
    if not isinstance(method, str):
        raise AttributeError("The Input Parameter Method should be string")

    if not isinstance(step_size, float):
        raise AttributeError("The Input Parameter Method should be float")

    if not callable(function):
        raise AttributeError("The given function parameter is not callable")

    if method == 'central':
        return (function(point + step_size) - function(point - step_size)) / (2 * step_size)
    elif method == 'forward':
        return (function(point + step_size) - function(point)) / step_size
    elif method == 'backward':
        return (function(point) - function(point - step_size)) / step_size
    else:
        raise ValueError("Method must be 'central', 'forward' or 'backward'.")


def complex_function(x_value):
    """
    A complex function to be used to find the derivative
                    y =    4x^2 + 2x + 1
                       ( ---------------   )^ x
                            x + 2e^x
    :param x_value: The point or array of points for which the function has to be computed
    :type x_value: Union[float, :class:`numpy.ndarray`]

    :return: The value of function at given point
    :rtype: float
    """
    return ((4 * x_value ** 2 + 2 * x_value + 1) / (x_value + 2 * np.exp(x_value))) ** x_value


def find_derivatives():
    """
    Finding derivative of some functions-Function
    -----------------------------------------------
    
     Function to find derivative of some common functions and complex function

    :return: Nothing
    :rtype: None
    """

    # Finding derivate of cos function at 0
    der = derivative(np.cos, 0)
    LOGGER.info("The derivative of cos function at 0 is: %s", der)

    # Finding the derivative of exponential function at 0 with step size 0.0001
    der = derivative(np.exp, 0, step_size=0.0001)
    LOGGER.info("The derivative of exponential function at 0 , with step size: 0.0001 is: %s", der)

    # Finding the derivative of exponential function at 0 with step size 0.0001 using backward scheme
    der = derivative(np.exp, 0, method='backward', step_size=0.0001)
    LOGGER.info("The derivative of exp function at 0 , with step size: 0.0001, with backward scheme is: %s", der)

    # Creating 100 evenly spaved points between 0 and 6
    x_axis = np.linspace(0, 6, 100)

    # Setting the Y axis to be the complex function
    y_axis = complex_function(x_axis)

    # Finding the derivative of complex function using central, backward and forward methods
    der_central = derivative(complex_function, x_axis)
    der_back = derivative(complex_function, x_axis, method='backward')
    der_forward = derivative(complex_function, x_axis, method='forward')

    # Plotting the results
    plt.figure(figsize=(12, 5))
    plt.plot(x_axis, y_axis, "b", label='y=f(x)')
    plt.plot(x_axis, der_central, "g", label="Central Difference y=f'(x)")
    plt.plot(x_axis, der_back, "y", label="Backward Difference y=f'(x)")
    plt.plot(x_axis, der_forward, "r", label="Forward Difference y=f'(x)")
    plt.legend()
    plt.grid(True)

    plt.show()
