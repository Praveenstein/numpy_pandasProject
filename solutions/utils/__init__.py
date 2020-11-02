# -*- coding: UTF-8 -*-
"""
Initialization For Solutions Package
===========================================

This Initialization module imports the necessary functions from the modules within this package
"""

from solutions.utils.logger import configure_logging
from solutions.utils.cli_getter import get_input_arguments
from solutions.utils.input_extractor import get_vector_from_file, get_matrix_from_file, get_complex_matrix_from_file

ARGUMENTS = get_input_arguments()
