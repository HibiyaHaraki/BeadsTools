#!/usr/bin/env python3

# beads_msh.py
#
# created by Hibiya Haraki
# All risks of running this script is always with you.
#
# Explanation
#  In this file, there are some functions for writing .atx file
#
# Functions
#  1. write_DSC_atx
#  2. write_NVC_atx
#  3. write_transientID_atx
#

import sys
from . import beads_log

logger = beads_log.root_logger();

## Writing deformed_surfaces.atx
def write_DSC_atx(filePath,Elements,Nodes,IDs):
    logger.info('Start Expoting deformed_surfaces.atx as {0}'.format(filePath));
    # Input Check
    if (len(Elements) != len(Nodes) or len(Elements) != len(IDs)):
        logger.error('This script needs same size Element, Node, and, transientID');
        sys.exit();

    # Open File
    file = open(filePath,'w');

    # Write Data
    for ii in range(len(Elements)):
        # Write Element Data
        file.write("###############################################\n");
        file.write("DeformedSurfaceElement {0}\n".format(len(Elements[ii])));
        file.write("###############################################\n");
        file.write("content_type=FEGenericAttribute\n");
        file.write("fega_type=Void\n");
        file.write("format=i4i4i4\n");
        file.write("deformed_surface_id={0}\n".format(IDs[ii]));
        file.write("\n");
        for jj in range(len(Elements[ii])):
            for kk in range(len(Elements[ii][jj])):
                file.write("{0} ".format(Elements[ii][jj][kk]));
            file.write("\n");
        file.write("\n");

        # Write Node Data
        file.write("###############################################\n");
        file.write("DeformedSurfaceNode {0}\n".format(len(Nodes[ii])));
        file.write("###############################################\n");
        file.write("content_type=FEGenericAttribute\n");
        file.write("fega_type=Void\n");
        file.write("format=f8f8f8\n");
        file.write("deformed_surface_id={0}\n".format(IDs[ii]));
        for jj in range(len(Nodes[ii])):
            for kk in range(len(Nodes[ii][jj])):
                file.write("{:.11E} ".format(Nodes[ii][jj][kk]));
            file.write("\n");
        file.write("\n");

    # Close file
    file.close();
    logger.info('Finish Exporting {0}'.format(filePath));

## Write nv_constraint.atx
def write_NVC_atx(filePath,Elements,faceID,normalVector):
    logger.info("Start Exporting nv_constraint.atx as {0}".format(filePath));
    # Input Check
    if (len(Elements) != len(faceID) or len(Elements) != len(normalVector)):
        logger.error("The input should have same size");
        sys.exit();
    if (len(normalVector[0]) != 3):
        logger.error("Normal Vector should be 3-dimentional data");
        sys.exit();

    # Create file
    file = open(filePath,"w");

    # Write Normal Vector data
    file.write("###############################################\n");
    file.write("NormalVectorConstraint {0}\n".format(len(Elements)));
    file.write("###############################################\n");
    file.write("content_type=FEGenericAttribute\n");
    file.write("fega_type=ElementVariable\n");
    file.write("format=i4f8f8f8\n");
    file.write("\n");
    for ii in range(len(Elements)):
        file.write("{0} {1} {2} {3} {4}\n".format(Elements[ii],faceID[ii],normalVector[ii][0],normalVector[ii][1],normalVector[ii][2]));

    #Colose file
    file.close();
    logger.info("Finish Exporting {0}".format(filePath));

## Import nv_constraint.atx
def read_NVC_atx(filePath):
    logger.info("Start Importing {0}".format(filePath));
    # Open File
    file = open(filePath,"r");
    file_all_lines = file.readlines();
    file.close();

    # Get data
    numNVC = 0; ElementID = []; FaceID = []; NVC = [];
    tmp = file_all_lines[1].split();
    numNVC = int(tmp[1].strip());

    for ii in range(numNVC):
        tmp = file_all_lines[ii+7].split();
        ElementID.append(int(tmp[0].strip()));
        FaceID.append(int(tmp[1].strip()));
        tmp_NVC = [];
        for jj in range(3):
            tmp_NVC.append(float(tmp[jj+2].strip()));
        NVC.append(tmp_NVC);

    # Output
    return numNVC, ElementID, FaceID, NVC;

## Write transientID.atx
def write_transientID_atx(filePath, NodeID, transientID):
    logger.info("Start Exporting transientID.atx as {0}".format(filePath));
    # Open file
    file = open(filePath,"w");

    # Write transientID.atx
    file.write("###############################################\n");
    file.write("TransientTemperature {0}\n".format(len(NodeID)));
    file.write("###############################################\n");
    file.write("content_type=FEGenericAttribute\n");
    file.write("fega_type=NodeVariable\n");
    file.write("format=i4i4f8\n");
    for ii in range(len(NodeID)):
        file.write("{0} {1} 0 0.000000e+00\n".format(NodeID[ii],transientID[ii]));

    # Close file
    file.close();
    logger.info("Finish Exporting {0}".format(filePath));

## Write NormalVector.atx
def write_normalVector_atx(filePath, NVs, IDs):
    logger.info("Start Exporting deformed_surface_nv.atx as {0}".format(filePath));
    # Check Input
    if (len(NVs) != len(IDs)):
        logger.error("The input should have same size");
        sys.exit();
    if (len(NVs[0][0]) != 3):
        logger.error("The normal vector should be 3-dimensional data");
        sys.exit();

    # Open file
    file = open(filePath,"w");

    # Write deformed surface normal vector data
    for ii in range(len(NVs)):
        file.write("###############################################\n");
        file.write("DeformedSurfaceNormalVector {0}\n".format(len(NVs[ii])));
        file.write("###############################################\n");
        file.write("content_type=FEGenericAttribute\n");
        file.write("fega_type=Void\n");
        file.write("format=f8f8f8\n");
        file.write("deformed_surface_id={0}\n".format(IDs[ii]));
        file.write("\n");
        for jj in range(len(NVs[ii])):
            file.write("{0} {1} {2}\n".format(NVs[ii][jj][0],NVs[ii][jj][1],NVs[ii][jj][2]));

    # Close file
    file.close();
    logger.info("Finish Exporting {0}".format(filePath));


if __name__ == '__main__':
    logger.info('Print info of beads_atx.py ');
    print('Functions');
    print('  1. write_DSC_atx');
    print('  2. write_NVC_atx');
    print('  3. write_transientID_atx');
    print('  4. write_normalVector_atx');
