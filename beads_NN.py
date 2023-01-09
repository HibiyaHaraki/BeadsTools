#!/usr/bin/env python3

# beads_msh.py
#
# created by Hibiya Haraki
# All risks of running this script is always with you.
#
# Explanation
#  In this file, there is a function for doing kNN by using NMSLIB Package.
#
# Functions
#  1. beads_kNN
#

import os
import sys
from . import beads_log
import numpy as np
import nmslib

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

logger = beads_log.root_logger();

## kNN
def beads_kNN(Points,Nodes,Num):
    # Check Inputs
    if (len(Points[0]) != len(Nodes[0])):
        logger.error('The input vectors should be same size');
        sys.exit();
    if (Num < 1):
        logger.error('The k in kNN should be positive integer');
        sys.exit();

    # Create Data
    NumPoints = len(Points);
    points = np.array(Points, dtype=np.float32);
    nodes = np.array(Nodes, dtype=np.float32);

    # Build Index
    index = nmslib.init(method="hnsw",space='l2');
    index.addDataPointBatch(nodes);
    index.createIndex({}, print_progress=True);

    # NN-calculation
    resultIDs = []; resultDist = [];
    ids = index.knnQueryBatch(points, k=Num, num_threads=4);

    for ii in range(NumPoints):
        resultIDs.append(ids[ii][0]);
        resultDist.append(ids[ii][1]);

    # Output
    return resultIDs, resultDist;

if __name__ == '__main__':
    logger.info('Print info of beads_NN.py ');
    print('Functions');
    print('  1. beads_kNN');
