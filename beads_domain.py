#!/usr/bin/env python3

# beads_domain.py
#
# created by Hibiya Haraki
# All risks of running this script is always with you.
#
# Explanation
#  In this file, there are some functions for calculating volume or area of surface of input Mesh
#
# Functions
#  1. calculate_Volume
#  2. calculate_Volume_Volume
#  3. calculate_triangle_area
#  4. calculate_surface_area
#

import sys
import math
from . import beads_log
from . import beads_vector as bv
import numpy as np
import numpy.linalg as LA

logger = beads_log.root_logger();
DIM = 3;

## Calculate Volume
def calculate_Volume(Nodes):
    # Input Check
    if (len(Nodes) != 4 and len(Nodes) != 8):
        logger.error("Illegal Element Type");
        sys.exit();

    # Calculate Volume
    vector1 = []; vector2 = []; vector3 = [];
    for ii in range(3):
        vector1.append(Nodes[1][ii] - Nodes[0][ii]);
        vector2.append(Nodes[2][ii] - Nodes[0][ii]);
        vector3.append(Nodes[3][ii] - Nodes[0][ii]);

    volume = bv.inner_product(vector1,bv.cross_product(vector2,vector3))/6;

    # Output
    return volume;

## Calculate Volume of Each Volume
def calculate_Volume_Volume(Elements,Nodes,Volumes):
    # Input Check
    judge = 0;
    for ii in range(len(Elements)):
        if (len(Elements[ii]) != 4 and len(Elements[ii]) != 10):
            judge += 1;

    if (judge > 0):
        logger.error("Illegal Element Type");
        sys.exit();

    # Calculate Volume
    volumeValue = [];
    if (Volumes == []):
        Volumes = range(len(Elements));

    for ii in range(len(Volumes)):
        tmp_volume = 0;
        for jj in range(len(Volumes[ii])):
            tmp_nodes = [];
            for kk in range(len(Elements[Volumes[jj]])):
                tmp_nodes.append(Nodes[Elements[Volumes[jj]][kk]]);
            tmp_volume += calculate_Volume(tmp_nodes);
        volumeValue.append(tmp_volume);

    # Output
    return volumeValue;

## Calculate Triangle Area
def calculate_triangle_area(Nodes):
    # Check Input
    if (len(Nodes) != 3):
        logger.error("This script can only apply to Triangle");
        sys.exit();
    if (len(Nodes[0]) != 3):
        logger.error("This script can only apply to 3-dimentional data");
        sys.exit();

    #Calculate Triangle Area
    vector1 = []; vector2 = [];
    for ii in range(3):
        vector1.append(Nodes[1][ii] - Nodes[0][ii]);
        vector2.append(Nodes[2][ii] - Nodes[0][ii])

    cross_product = bv.cross_product(vector1,vector2);
    area = bv.inner_product(cross_product,cross_product);

    # Output
    return area;

## Calculate Surface Area
def calculate_surface_area(Elements,Nodes):
    # Check Input
    if (len(Nodes[0]) != 3):
        logger.error("This script can only apply to 3-dimentional data");
        sys.exit();

    # Calculate Surface Area
    surface_area = 0;
    for ii in range(len(Elements)):
        tmp_nodes = [];
        for jj in range(3):
            tmp_nodes.append(Nodes[Elements[ii][jj]]);
        surface_area += calculate_triangle_area(tmp_nodes);

    # Output
    return surface_area;

if __name__ == '__main__':
    logger.info('Print info of beads_domain.py ');
    print('Functions');
    print('  1. calculate_Volume');
    print('  2. calculate_Volume_Volume');
    print('  3. calculate_triangle_area');
    print('  4. calculate_surface_area');
