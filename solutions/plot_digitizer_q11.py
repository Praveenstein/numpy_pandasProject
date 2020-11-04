# -*- coding: utf-8 -*-
"""
Module to 
=================================

Module for 

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations

This script contains the following function
    * new_func - Function to
"""
# Standard Imports
import logging
from collections import Counter

# External Imports
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2

# User Imports

__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def rgb2hex(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


def get_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


def new_func(number_of_colors, show_chart):
    """
    Title Function 
    -----------------------------------------------
    
    Function

    :param parameter:
    :type parameter:

    :return: rgb_colors
    :rtype: list
    """
    image = get_image("input\\sigmoid.jpg")

    modified_image = cv2.resize(image, (600, 400), interpolation=cv2.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0] * modified_image.shape[1], 3)

    clf = KMeans(n_clusters=number_of_colors)
    labels = clf.fit_predict(modified_image)

    counts = Counter(labels)

    center_colors = clf.cluster_centers_
    # We get ordered colors by iterating through the keys
    ordered_colors = [center_colors[i] / 255 for i in counts.keys()]
    hex_colors = [rgb2hex(ordered_colors[i] * 255) for i in counts.keys()]
    rgb_colors = [ordered_colors[i] * 255 for i in counts.keys()]

    if show_chart:
        plt.figure(figsize=(8, 6))
        plt.pie(counts.values(), labels=hex_colors, colors=ordered_colors,
                wedgeprops={"edgecolor": "0", 'linewidth': 1, 'antialiased': True})
        plt.show()

    return rgb_colors
