# -*- coding: utf-8 -*-
"""
Module to Digitize Plots in an Image
=======================================

Module for getting the actual points of a trend lines from a given image

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations

This script contains the following function
    * digitize_plots - Function to get the actual points of a trend lines from a given image
"""
# Standard Imports
import logging

# External Imports
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2

__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def digitize_plots(image_path, number_of_colors, x_min, x_max, y_min, y_max):
    """
    Title Function 
    -----------------------------------------------
    
    Function

    :param image_path: The path to the image
    :type image_path: str

    :param number_of_colors: The number of colors in the given graph
    :type number_of_colors: int

    :param x_min: The minimum x value
    :type x_min: int

    :param x_max: The maximum x value
    :type x_max: int

    :param y_min: The minimum y value
    :type y_min: int

    :param y_max: The maximum y value
    :type y_max: int
    """

    if not isinstance(number_of_colors, int):
        raise AttributeError("The number of colors should be of type int")

    # Reading image and converting from bgr to rgb
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    LOGGER.info("The Shape of given Image: %s", image.shape)

    plt.imshow(image)
    plt.xticks([]), plt.yticks([])
    plt.show()

    # Flattening the array to get individual points with their pixel values, which could be used in KMeans clustering
    reshaped_image = image.reshape((image.shape[0] * image.shape[1], 3))

    # Fitting the reshaped image using kmeans
    clusters = KMeans(n_clusters=number_of_colors).fit(reshaped_image)
    cluster_labels = clusters.labels_
    cluster_centers = clusters.cluster_centers_

    # Creating a bar plot, and setting the colors of the bar plot to the colors represented by the cluster centers
    bar_chart = plt.bar(["0", "1", "2"], [1, 1, 1])
    bar_chart[0].set_color(cluster_centers[0]/255)
    bar_chart[1].set_color(cluster_centers[1]/255)
    bar_chart[2].set_color(cluster_centers[2]/255)
    plt.show()

    # Getting the use input for the choice of color
    cluster_number = int(input("Please enter the Color of Graph"))

    if cluster_number not in [0, 1, 2]:
        raise AttributeError("Incorrect cluster number")

    # Getting all the indices where the point belongs to the user's cluster number
    indices = np.argwhere(cluster_labels == cluster_number)

    # Creating a new array with values equal to zero and size equal to the total number of pixels
    array_of_points = np.zeros(len(cluster_labels))

    # Setting the value to one for those values that belonged to the cluster chosen by the user
    array_of_points[indices] = 1

    # Reshaping the array_of_points
    array_of_points = array_of_points.reshape((image.shape[0], image.shape[1]))
    x_range = [x_min, x_max]
    y_range = [y_min, y_max]

    # The scale along x and y axis is found for actual graph
    x_scale_original = x_range[1] - x_range[0]
    y_scale_original = y_range[1] - y_range[0]

    # Getting the index of points that were chosen by user (which is set to 1 previously)
    index_of_points = np.argwhere(array_of_points == 1)

    # Finding the smallest and largest column index
    x_min = index_of_points[:, 1].min()
    x_max = index_of_points[:, 1].max()

    # Finding the smallest and largest row index
    y_min = index_of_points[:, 0].max()
    y_max = index_of_points[:, 0].min()

    # The scale along x and y axis is found for pixels in image
    x_scale_image = x_max - x_min
    y_scale_image = y_min - y_max

    # The unit size factor are found for x and y points of pixels
    x_factor = x_scale_original / x_scale_image
    y_factor = y_scale_original / y_scale_image

    x_pixel_mapping = {x_min: x_range[0]}
    previous_value = x_pixel_mapping[x_min]
    for x_pixel in range(x_min - 1, -1, -1):
        current_value = previous_value - x_factor
        x_pixel_mapping[x_pixel] = current_value
        previous_value = current_value

    previous_value = x_pixel_mapping[x_min]
    for x_pixel in range(x_min + 1, image.shape[1]):
        current_value = previous_value + x_factor
        x_pixel_mapping[x_pixel] = current_value
        previous_value = current_value

    y_pixel_mapping = {y_min: y_range[0]}
    previous_value = y_pixel_mapping[y_min]
    for y_pixel in range(y_min - 1, -1, -1):
        current_value = previous_value + y_factor
        y_pixel_mapping[y_pixel] = current_value
        previous_value = current_value

    previous_value = y_pixel_mapping[y_min]
    for y_pixel in range(y_min + 1, image.shape[0]):
        current_value = previous_value - y_factor
        y_pixel_mapping[y_pixel] = current_value
        previous_value = current_value

    points = np.array([[x_pixel_mapping[row[1]], y_pixel_mapping[row[0]]] for row in index_of_points])

    plt.figure(figsize=(1920 / 96, 1080 / 96), dpi=96)
    plt.scatter(points[:, 0], points[:, 1])
    plt.show()
