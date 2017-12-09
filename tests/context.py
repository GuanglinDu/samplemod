# -*- coding: utf-8 -*-

# Under title 'PYTHONPATH, and finding packages & modules during development' in
# Structuring, Testing, and Maintaining Python Programs
# https://intermediate-and-advanced-software-carpentry.readthedocs.io/en/latest/structuring-python.html
import sys
import os

this_dir = os.path.dirname(__file__)
sample_dir = os.path.abspath(os.path.join(this_dir, '..'))

# The path insert guard as the C/C++ include guard.
if sample_dir not in sys.path:
    sys.path.insert(0, sample_dir)

import sample
