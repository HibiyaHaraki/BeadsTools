#!/usr/bin/env python3

# beads_fgr.py
#
# created by Hibiya Haraki
# All risks of running this script is always with you.
#
# Explanation
#  In this file, there are some functions for treating ADVENTURE .fgr file (See ADVENTURE BCtool Document) in Python
#
# Functions
#  1. read_fgr
#  2. convert_face2node
#

import sys
from . import beads_log

logger = beads_log.root_logger();

## Import Number of Surface from ADVENTURE .fgr file (See ADVENTURE BCtool Document)
def read_numSurf_from_fgr(filePath):
    logger.info('Start Importing Surfaces');
    file = open(filePath,'r');
    file_all_lines = file.readlines();
    file.close();
    NumSurfaces = int(file_all_lines[1].strip());
    return NumSurfaces


## Import ADVENTURE .fgr file (See ADVENTURE BCtool Document)
def read_fgr(filePath,surfaceID):
    logger.info('Start Importing Surfaces');
    file = open(filePath,'r');
    file_all_lines = file.readlines();
    file.close();

    # Get Element Type and Number of Nodes in a element
    tmp = int(file_all_lines[0]);
    NumNodes = 0;
    if (tmp == 4):
        NumNodes = 3;
    elif (tmp == 10):
        NumNodes = 6;
    elif (tmp == 8):
        NumNodes = 4;
    elif (tmp == 20):
        NumNodes = 8;
    logger.info('Import {0} Nodes Element'.format(NumNodes));

    # Check Input
    NumSurfaces = int(file_all_lines[1].strip());
    for ii in range(len(surfaceID)):
        if (NumSurfaces < surfaceID[ii]):
            sys.exit("{0} includes only {1} surfaces!!".foramts(filePath,NumSurfaces));

    # Set Output List
    NumElements = 0;  ElementID = []; FaceID = []; Elements = [];

    for jj in range(len(surfaceID)):
        # Move to the data
        ii = 0; reading_line = 2;
        while (ii < surfaceID[jj]):
            tmp_NumElements = int(file_all_lines[reading_line].strip());
            reading_line += tmp_NumElements + 1;
            ii = ii+1;
        logger.info('Import Surface ID is {0}'.format(surfaceID[jj]));

        # Read Elements Number
        tmp_numElements = int(file_all_lines[reading_line].strip());
        NumElements += tmp_numElements;
        logger.info('Surface ID {0} includes {1} Elements'.format(surfaceID[jj],NumElements));

        # Read Data
        for i in range(NumElements):
            reading_line += 1;
            tmp_element_line = file_all_lines[reading_line].split();
            ElementID.append(int(tmp_element_line[0].strip()));
            FaceID.append(int(tmp_element_line[1].strip()));
            tmp_element = [];
            for j in range(NumNodes):
                tmp_element.append(int(tmp_element_line[2+j].strip()));
            Elements.append(tmp_element);

    # Output
    logger.info('Finish Importing Surface');
    return ElementID, FaceID, Elements;

## Convert Node iD in Element by inputting face ID
def convert_face2node(FaceID):
    if (FaceID == 0):
        return [1,2,3];
    elif (FaceID == 1):
        return [0,3,2];
    elif (FaceID == 2):
        return [0,1,3];
    elif (FaceID == 3):
        return [0,2,1];
    else:
        logger.error("FaceID should be 0, 1, 2, or 3");
        sys.exit();



## Check the functions
if __name__ == '__main__':
    logger.info('Print info of beads_fgr.py ');
    print('Functions');
    print('  1. read_fgr');
