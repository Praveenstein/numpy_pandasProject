# -*- coding: utf-8 -*-
"""
Command Line Input Getter
============================

Main Module for getting the command line arguments

This script requires the following modules be installed in the python environment
    * argparse - to handle command line arguments

This script contains the following function
    * get_input_arguments - to get the command line arguments
"""
# Built-in imports
import argparse


def get_input_arguments():
    """
    Function to get the input arguments from command line

    :return: args - arguments from the command line
    :rtype: argparse.Namespace
    """

    my_parser = argparse.ArgumentParser(allow_abbrev=False)

    my_parser.add_argument('--logfile', action='store', type=str, required=True)
    my_parser.add_argument('--inputfile', action='store', type=str, required=False)
    my_parser.add_argument('--number', action='store', type=int, required=False)
    my_parser.add_argument('--x_min_cs', action='store', type=float, required=False)
    my_parser.add_argument('--x_max_cs', action='store', type=float, required=False)
    my_parser.add_argument('--x_min_sig', action='store', type=float, required=False)
    my_parser.add_argument('--x_max_sig', action='store', type=float, required=False)
    my_parser.add_argument('--x_min', action='store', type=float, required=False)
    my_parser.add_argument('--x_max', action='store', type=float, required=False)
    my_parser.add_argument('--y_min', action='store', type=float, required=False)
    my_parser.add_argument('--y_max', action='store', type=float, required=False)
    my_parser.add_argument('--no_points', action='store', type=int, required=False)
    my_parser.add_argument('--width', action='store', type=int, required=False)
    my_parser.add_argument('--height', action='store', type=int, required=False)

    args = my_parser.parse_args()
    return args
