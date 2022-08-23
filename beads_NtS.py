#!/usr/bin/env python3

# beads_NtS.py
#
# created by Hibiya Haraki
# All risks of running this script is always with you.
#
# Explanation
#  In this file, there is a function for Node-to-Surface Algorithm.
#
# Functions
#  1. beads_NtS
#

import os
import sys
from . import beads_log
from . import beads_judge
from . import beads_vector
from . import beads_NN

logger = beads_log.root_logger();

## Node-to-Surface Algorithm
def beads_NtS(Points,Elements,Nodes):
    logger.info('Start Node-to-Surface Algorithm');

    # Check Inputs
    if (len(Points[0]) != 3):
        logger.error('This script can only treat 3-dimentional data');
        sys.exit();
    if (len(Nodes[0]) != 3):
        logger.error('This script needs 3-dimentional Mesh data');

    # NN-Calculation
    NN_IDs, _ = beads_NN.beads_kNN(Points,Nodes,1);

    # Perpendicular Check
    NtS_result = [-1] * len(Points);
    for ii in range(len(Points)):
        tmp_element = [];
        elementID = [];

        # Find Element including NN Nodes
        for jj in range(Elements):
            if (NN_IDs[ii] in Elements[jj]):
                tmp_element.append(Elements[jj]);
                elementID.append(jj);

        ## Calculate Parpendicular Leg
        for jj in range(len(tmp_element)):
            tmp_node = [];
            tmp_dist = -1;
            for kk in range(len(tmp_element[jj])):
                tmp_node.append(Nodes[tmp_element[jj][kk]]);
            tmp_perpendicular_leg = beads_vector.calc_perpendicular_leg(Points[ii],tmp_node);

            ## Judge the parpendicular leg is in the element or not
            if (beads_vector.judge_inout(tmp_perpendicular_leg,tmp_node) > 0):
                dist = 0;
                for ll in range(3):
                    dist += (Points[ii][ll] - tmp_perpendicular_leg[ii][ll])**2;
                if (tmp_dist < 0 or tmp_dist > math.sqrt(dist)):
                    tmp_dist = math.sqrt(dist);
                    NtS_result[ii] = elementID[jj];

    # Output
    return NtS_result;
