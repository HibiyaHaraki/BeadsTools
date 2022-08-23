#!/usr/bin/env python3

# beads_txt.py
#
# created by Hibiya Haraki
# All risks of running this script is always with you.
#
# Explanation
#  In this file, there is a function for reading constraint of surface area in .txt file
#
# Functions
#  1. read_txt
#

import os
import sys
from . import beads_log

logger = beads_log.root_logger();

## Reading .txt file
def read_txt(filePath):
    logger.info('Start Importing {0}'.format(filePath));
    # Open File and get data
    file = open(filePath,"r");
    file_all_lines = file.readlines();
    file.close();

    # Import Data
    surfID = []; surfConst = [];
    numData = int(file_all_lines[0].strip());
    for ii in range(numData):
        surfID.append(int(file_all_lines[2*ii+1].strip()));
        surfConst.append(file_all_lines[2*ii+2].strip());

    # Output
    return surfID, surfConst;
