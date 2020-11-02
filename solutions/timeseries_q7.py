# -*- coding: utf-8 -*-
"""
Descriptive Stats of Time Series Data
==========================================

Module for computing the min, max, mean and median for a given time-series data:
            a. For every hour
            b. For every day
            c. For every month

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations
    * os - Os module to interact with the underlying os to check if a given file exist
    *pandas - This provides the Data structures and operations for manipulating numerical tables and time series

This script contains the following function
    * min_data - Function to Find the minimum for every hour, day and month
    * max_data - Function to Find the maximum for every hour, day and month
    * mean_data - Function to Find the mean for every hour, day and month
    * median_data - Function to Find the median for every hour, day and month
    * get_stats - Function to call appropriate functions to compute all the stats shown above
"""
# Standard Imports
import logging
import os

# External Imports
import pandas as pd

__author__ = "praveen@gyandata.com"


LOGGER = logging.getLogger(__name__)


def min_data(data):
    """
    Min Stats of Data-Function
    -------------------------------

    Function to Find the minimum for every hour, day and month for the given time series data

    :param data: The time-series dataframe to be analysed
    :type data: :class:`pandas.core.frame.DataFrame`

    :return: Nothing
    :rtype: None
    """
    try:
        if not issubclass(type(data), pd.DataFrame):
            raise AttributeError("The input data should be of type pandas.core.frame.DataFrame")

        LOGGER.info("Finding the Hourly Min")
        hourly_df = data.resample('h').min()
        LOGGER.info("The Hourly Min Values are:\n\n %s\n\n", hourly_df.head())

        LOGGER.info("Finding the Daily Min")
        daily_df = data.resample('D').min()
        LOGGER.info("The Daily Min Values are:\n\n %s\n\n", daily_df.head())

        LOGGER.info("Finding the Monthly Min")
        monthly_df = data.resample('M').min()
        LOGGER.info("The Monthly Min Values are:\n\n %s\n\n", monthly_df.head())
    except AttributeError as err:
        LOGGER.error(err)


def max_data(data):
    """
    Max Stats of Data-Function
    -----------------------------------------------

    Function to Find the maximum for every hour, day and month for the given time series data

    :param data: The time-series dataframe to be analysed
    :type data: :class:`pandas.core.frame.DataFrame`

    :return: Nothing
    :rtype: None
    """
    try:
        if not isinstance(data, pd.DataFrame):
            raise AttributeError("The input data should be of type pandas.core.frame.DataFrame")

        LOGGER.info("Finding the Hourly Max")
        hourly_df = data.resample('h').max()
        LOGGER.info("The Hourly Max Values are:\n\n %s\n\n", hourly_df.head())

        LOGGER.info("Finding the Daily Max")
        daily_df = data.resample('D').max()
        LOGGER.info("The Daily Max Values are:\n\n %s\n\n", daily_df.head())

        LOGGER.info("Finding the Monthly Max")
        monthly_df = data.resample('M').max()
        LOGGER.info("The Monthly Max Values are:\n\n %s\n\n", monthly_df.head())
    except AttributeError as err:
        LOGGER.error(err)


def mean_data(data):
    """
    Mean Stats of Data-Function
    -----------------------------------------------

    Function to Find the mean for every hour, day and month for the given time series data

    :param data: The time-series dataframe to be analysed
    :type data: :class:`pandas.core.frame.DataFrame`

    :return: Nothing
    :rtype: None
    """
    try:
        if not isinstance(data, pd.DataFrame):
            raise AttributeError("The input data should be of type pandas.core.frame.DataFrame")

        LOGGER.info("Finding the Hourly Mean")
        hourly_df = data.resample('h').mean()
        LOGGER.info("The Hourly Mean Values are:\n\n %s\n\n", hourly_df.head())

        LOGGER.info("Finding the Daily Mean")
        daily_df = data.resample('D').mean()
        LOGGER.info("The Daily Mean Values are:\n\n %s\n\n", daily_df.head())

        LOGGER.info("Finding the Monthly Mean")
        monthly_df = data.resample('M').mean()
        LOGGER.info("The Monthly Mean Values are:\n\n %s\n\n", monthly_df.head())
    except AttributeError as err:
        LOGGER.error(err)


def median_data(data):
    """
    Median Stats of Data-Function
    -----------------------------------------------

    Function to Find the median for every hour, day and month for the given time series data

    :param data: The time-series dataframe to be analysed
    :type data: :class:`pandas.core.frame.DataFrame`

    :return: Nothing
    :rtype: None
    """
    try:
        if not isinstance(data, pd.DataFrame):
            raise AttributeError("The input data should be of type pandas.core.frame.DataFrame")

        LOGGER.info("Finding the Hourly Median")
        hourly_df = data.resample('h').median()
        LOGGER.info("The Hourly Median Values are:\n\n %s\n\n", hourly_df.head())

        LOGGER.info("Finding the Daily Median")
        daily_df = data.resample('D').median()
        LOGGER.info("The Daily Median Values are:\n\n %s\n\n", daily_df.head())

        LOGGER.info("Finding the Monthly Median")
        monthly_df = data.resample('M').median()
        LOGGER.info("The Monthly Median Values are:\n\n %s\n\n", monthly_df.head())
    except AttributeError as err:
        LOGGER.error(err)


def get_stats(filepath):
    """
    Descriptive Stats of Data-Function
    -----------------------------------------------
    
    Function to call appropriate functions to compute all the stats

    :param filepath: The Path to file containing the time series data
    :type filepath: str

    :return: Nothing
    :rtype: None
    """

    file_exist = os.path.isfile(filepath)

    if not file_exist:
        raise FileExistsError("File doesn't exist")

    # Reading the Time series Data
    time_series_data = pd.read_csv(filepath, header=0, index_col=0)

    LOGGER.info("The first 5 Values from the Data are:\n\n %s\n\n", time_series_data.head())
    print("\n\n")

    # Converting the string type index of dataframe to datetime
    index_df = pd.to_datetime(time_series_data.index)

    # Again setting the index of the datafram to previously created datetime values
    time_series_data.index = index_df

    # Computing the Min Stats
    min_data(time_series_data)

    # Computing the Max Stats
    max_data(time_series_data)

    # Computing the Mean Stats
    mean_data(time_series_data)

    # Computing the Median Stats
    median_data(time_series_data)
