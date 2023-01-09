#!/usr/bin/env python3

# beads_msh.py
#
# created by Hibiya Haraki
# All risks of running this script is always with you.
#
# Explanation
#  In this file, there are some functions for treating ADVENTURE .msh file (See ADVENTURE BCtool Document) in Python
#
# Functions
#  1. read_msh
#  2. write_msh
#  3. calculate_Gravity_Point
#

import os
import sys
from . import beads_log

logger = beads_log.root_logger();

## Import Mesh Data from ADVENTURE .msh file (See ADVENTURE BCtool Document)
def read_msh(filePath):
    logger.info('Start Importing {0}'.format(filePath));
    file = open(filePath,'r');
    file_all_lines = file.readlines();
    file.close();

    # Get Element Data
    reading_line = 0;
    NumOfElements = int(file_all_lines[reading_line].strip());
    Elements = [];
    for ii in range(NumOfElements):
        reading_line += 1;
        tmp_element = file_all_lines[reading_line].split();
        for jj in range(len(tmp_element)):
            tmp_element[jj] = int(tmp_element[jj].strip());
        Elements.append(tmp_element);
    logger.info('Get {0} Elements'.format(NumOfElements));

    # Get Node Data
    reading_line += 1;
    NumOfNodes = int(file_all_lines[reading_line].strip());
    Nodes = [];
    for ii in range(NumOfNodes):
        reading_line += 1;
        tmp_node = file_all_lines[reading_line].split();
        for jj in range(len(tmp_node)):
            tmp_node[jj] = float(tmp_node[jj].strip());
        Nodes.append(tmp_node);
    logger.info('Get {0} Nodes'.format(NumOfNodes));

    # Get Volume Data
    NumOfVolumes = 0;
    NumOfElementsInEachVolume = [];
    Volumes = [];
    if (len(file_all_lines) > reading_line+1):
        reading_line += 1;
        NumOfVolumes = int(file_all_lines[reading_line]);
        for ii in range(NumOfVolumes):
            reading_line += 1;
            NumOfElementsInEachVolume.append(int(file_all_lines[reading_line].strip()));
            tmp_volume_data = [];
            for jj in range(NumOfElementsInEachVolume[ii]):
                tmp_volume_data.append(int(file_all_lines[reading_line].strip()));
            Volumes.append(tmp_volume_data);
    logger.info('Get {0} Volumes'.format(NumOfVolumes));

    # Output Mesh Data
    logger.info('Finish Importing {0}'.format(filePath));
    return NumOfElements, Elements, NumOfNodes, Nodes, NumOfVolumes, NumOfElementsInEachVolume, Volumes;


## Export Mesh Data from ADVENTURE .msh file (See ADVENTURE BCtool Document)
def write_msh(filePath, Elements, Nodes, Volumes):
    logger.info('Start Exporting {0}'.format(filePath));
    file = open(filePath,'w');

    # Write Elements Data
    file.write("{0}\n".format(len(Elements)));
    for ii in range(len(Elements)):
        for jj in range(len(Elements[ii])):
            file.write("{0} ".format(Elements[ii][jj]));
        file.write("\n");
    logger.info('Export {0} Elements'.format(len(Elements)));

    # Write Nodes Data
    file.write("{0}\n".format(len(Nodes)));
    for ii in range(len(Nodes)):
        for jj in range(len(Nodes[ii])):
            file.write("{:.11f} ".format(Nodes[ii][jj]));
        file.write("\n");
    logger.info('Export {0} Nodes'.format(len(Nodes)));

    # Write Volume Data
    file.write("{0}\n".format(len(Volumes)))
    for ii in range(len(Volumes)):
        file.write("{0}\n".format(len(Volumes[ii])));
        for jj in range(len(Volumes[ii])):
            file.write("{0}\n".format(Volumes[ii][jj]));
    logger.info('Export {0} Volumes'.format(len(Volumes)));

    # Exit
    file.close();
    logger.info('Finish Exporting {0}'.format(filePath));

## Calculate Gravity Point
def calculate_gravity_point(Nodes):
    # Input Check
    if (len(Nodes) != 3):
        logger.error("Input should be 3-Nodes");
        sys.exit();
    if (len(Nodes[0]) != 3):
        logger.error("This script can apply only to 3-dimentional data");
        sys.ecit();

    # Calculate Gravity Point
    gp = [];
    for ii in range(3):
        gp.append((Nodes[0][ii] + Nodes[1][ii] + Nodes[2][ii])/3);

    # Output
    return gp;

## Delete node from element
def delete_nodes_from_elements(delete_nodes,elements):
    # Check Inputs
    num_elements = len(elements);
    num_delete_nodes = len(delete_nodes);
    max_node_id = max(list(map(lambda x: max(x), elements)));
    for ii in range(num_delete_nodes):
        if(delete_nodes[ii] > max_node_id):
            logger.error("Delete Nodes ID {0} is over max node id {1}".format(delete_nodes[ii],max_node_id));
    logger.info("Delete {0} nodes from {1} elements".format(num_delete_nodes,num_elements));
    delete_nodes.sort();
    
    # Create map for elements
    logger.info("Create Element-Node map");
    element_map = [[] for ii in range(max_node_id+1)];
    for ii in range(num_elements):
        for jj in range(len(elements[ii])):
            element_map[elements[ii][jj]].append([ii,jj]);
    
    # Revise node IDs
    logger.info("Revise node IDs");
    revise_number = [];
    for ii in range(max_node_id+1):
        revise_number.append(0);
    for ii in range(num_delete_nodes):
        for jj in range(delete_nodes[ii],max_node_id+1):
            revise_number[jj] += 1;
    for ii in range(max_node_id+1):
        for jj in range(len(element_map[ii])):
            elements[element_map[ii][jj][0]][element_map[ii][jj][1]] -= revise_number[ii];

    # Delete node ID from Elements
    logger.info("Delete nodes");
    delete_elements = [];
    for ii in range(num_delete_nodes):
        for jj in range(len(element_map[delete_nodes[ii]])):
            delete_elements.append(element_map[delete_nodes[ii]][jj][0]);
    delete_elements = list(set(delete_elements));
    delete_elements.sort(reverse=True);
    for ii in range(len(delete_elements)):
        elements.pop(delete_elements[ii]);    

    # Output
    logger.info("Number of Elements is {0}".format(len(elements)));
    return elements;


## Check the functions
if __name__ == '__main__':
    logger.info('Print info of beads_msh.py ');
    print('Functions');
    print('  1. read_msh');
    print('  2. write_msh');
    print('  3. calculate_gravity_point');
    print('  4. delete_nodes_from_elements');
