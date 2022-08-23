#!/usr/bin/env python3

# beads_vector.py
#
# created by Hibiya Haraki
# All risks of running this script is always with you.
#
# Explanation
#  In this file, there are some functions for treating vector in Python
#
# Functions
#  1. vector_norm
#  2. normalize_vector
#  3. cross_product
#  4. normal_vector
#  5. inner_product
#  6. cosine_similarity
#  7. beads_pca
#  8. calc_perpendiculat_leg
#  9. judge_inout
#

import sys
import math
from . import beads_log
import numpy as np
import numpy.linalg as LA

logger = beads_log.root_logger();
DIM = 3;

## Calculate Vector Norm
def vector_norm(vector,n):
    # Check Inputs
    if (n < 1):
        logger.error('Norm need positive integer for calculation');
        sys.exit();
    elif (len(vector) < 1):
        logger.error('Input Vector do not have element');
        sys.exit();

    # Calculate Norm
    norm = 0;
    for ii in range(len(vector)):
        norm += vector[ii]**n;

    # Output
    return norm**(1/n);

## Normalize Vector
def normalize_vector(vector):
    # Calculate Normalize Vector
    normalize_vector = [];
    norm = vector_norm(vector,2);
    for ii in range(len(vector)):
        if (norm > 0):
            normalize_vector.append(vector[ii]/norm);

    return normalize_vector;

## Calculate cross-product
def cross_product(vector1,vector2):
    # Check Input
    if (len(vector1) != 3 or len(vector2) != 3):
        logger.error("This script can apply only to 3-dimentional data");
        sys.exit();

    cross_product = [];
    cross_product.append(vector1[1]*vector2[2] - vector1[2]*vector2[1]);
    cross_product.append(vector1[2]*vector2[0] - vector1[0]*vector2[2]);
    cross_product.append(vector1[0]*vector2[1] - vector1[1]*vector2[0]);

    # Output
    return cross_product;


## Calculate normal vector from three coordinates
def normal_vector(Nodes):
    # Check Input
    if (len(Nodes) != 3):
        logger.error('Calculating Normal Vector needs 3 Nodes');
        sys.exit();
    elif (len(Nodes[0]) != 3):
        logger.error('Soory, This code only apply to 3-dimentional data');
        sys.exit();

    # Calculate Normal Vector
    vector1 = []; vector2 = [];
    for ii in rnage(DIM):
        vector1.append(Nodes[1][ii] - Nodes[0][ii]);
        vector2.append(Nodes[2][ii] - Nodes[0][ii]);

    normal_vector = cross_procuct(vector1,vector2);
    normal_vector = normalize_vector(normal_vector);

    # Output
    return normal_vector;

## Calculate Inner Product
def inner_product(vector1,vector2):
    # Check Input
    if (len(vector1) != len(vector2)):
        logger.error('Input Vectors should have same length');
        sys.exit();

    # Calculate Inner Product
    inner_product = 0;
    for ii in range(len(vector1)):
        inner_product += vector1[ii]*vector2[ii];

    # Output
    return inner_product;

## Calculate Cosine Similarity
def cosine_similarity(vectors1, vectors2):
    # Check Inputs
    if (len(vectors1) != 3 or len(vectors2) != 3):
        logger.error('Sorry, this code can apply to only 3-dimentional Vector');
        sys.exit();

    cosine_similarity = inner_product(normalize_vector(vector1),normalize_vector(vector2));

    # Output
    return cosine_similarity;

## Calculate PCA (Primary Component Analysis)
def beads_pca(Nodes):
    # Input Check
    if (len(Nodes[0]) != 3):
        logger.error('Sorry, this function can apply to only 3-dimentional data');
        sys.ecit();

    NumData = len(Nodes);

    # Normalize Data
    x_ave = 0; y_ave = 0; z_ave = 0;
    for ii in range(NumData):
        x_ave += Nodes[ii][0];
        y_ave += Nodes[ii][1];
        z_ave += Nodes[ii][2];
    x_ave /= NumData; y_ave /= NumData; z_ave /= NumData;
    for ii in range(len(Nodes)):
        Nodes[ii][0] -= x_ave;
        Nodes[ii][1] -= y_ave;
        Nodes[ii][2] -= z_ave;

    # Create covariance-matrix
    covariance_matrix = [[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]];
    for ii in range(3):
        for jj in range(3):
            for kk in range(NumData):
                covariance_matrix[ii][jj] += Nodes[kk][ii]*Nodes[kk][jj];

    # Calculate PCA
    covariance_matrix = np.array(covariance_matrix);
    w, v = LA.eig(covariance_matrix);

    # Output
    return w.tolist(), v.tolist();

## Calculate Perpendicular Leg
def calc_perpendicular_leg(point,Nodes):
    # Check Input
    if(len(point) != 3 or len(Nodes[0]) != 3):
        logger.error("This script can only apply to 3-dimentional data");
        sys.exit();
    if (len(Nodes) != 3):
        logger.error("Calculating Perpendicular Leg needs 3 Point on a plane");
        sys.exit();

    # Normalize
    for ii in range(3):
        for jj in range(3):
            Nodes[ii][jj] -= point[jj];

    # Calculate Plane Equation from Origin Point
    vector1 = []; vector2 = [];
    for ii in range(3):
        vector1.append(Nodes[1][ii] - Nodes[0][ii]);
        vector2.append(Nodes[2][ii] - Nodes[0][ii]);
    cross = cross_procuct(vector1,vector2);
    const = cross[0]*point[0] + cross[1]*point[1] + cross[2]*point[2];

    # Calculate Intersection
    intersetion = [cross[0]*const/vector_norm(cross,2)**2,cross[1]*const/vector_norm(cross,2)**2,cross[2]*const/vector_norm(cross,2)**2];

    # Unnormalize
    for ii in range(3):
        intersection[ii] += point[ii];

    # Output
    return intersection;

## Inside / Outside Judgement
def judge_inout(point,Nodes):
    # Check Input
    if(len(point) != 3 or len(Nodes[0]) != 3):
        logger.error("This script can only apply to 3-dimentional data");
        sys.exit();
    if (len(Nodes) != 3):
        logger.error("Calculating Perpendicular Leg needs 3 Point on a plane");
        sys.exit();

    # Calculate Necessary Vector
    vector1 = []; vector2 = []; vector3 = [];
    vector1p = []; vector2p = []; vector3p = [];
    for ii in range(3):
        vector1.append(Nodes[1][ii] - Nodes[0][ii]);
        vector2.append(Nodes[2][ii] - Nodes[1][ii]);
        vector3.append(Nodes[0][ii] - Nodes[2][ii]);

        vector1p.append(point[ii] - Nodes[1][ii]);
        vector2p.append(point[ii] - Nodes[2][ii]);
        vector3p.append(point[ii] - Nodes[0][ii]);

    # Calculate Cross Product
    cross1 = cross_product(vector1,vector1p);
    cross2 = cross_product(vector2,vector2p);
    cross3 = cross_product(vector3,vector3p);

    # Calculate inner product
    inner1 = inner_product(cross1,cross2);
    inner2 = inner_product(cross1,cross3);

    # Judge Sign
    if (inner1/math.abs(inner1) == inner2/math.abs(inner2)):
        return 1;
    else:
        return 0;

if __name__ == '__main__':
    print('beads_log.py');
