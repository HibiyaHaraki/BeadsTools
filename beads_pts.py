#!/usr/bin/env python3

# beads_pts.py
#
# created by Hibiya Haraki
# All risks of running this script is always with you.
#
# Explanation
#  In this file, there are some functions for treating .pts file (Point Cloud Data) in Python
#
# Functions
#  1. read_pts
#  2. write_pts
#  3. transform_coordinates_pts
#

import sys
from . import beads_log

logger = beads_log.root_logger();

## Import .pts file (Point Cloud Data)
def read_pts(filePath):
    logger.info('Start Importing {0}'.format(filePath));
    file = open(filePath,'r');
    file_all_lines = file.readlines();
    file.close();

    # Get Number of Points
    reading_line = 0;
    NumOfPoints = int(file_all_lines[reading_line].strip());
    logger.info('Importing {0} Points data'.format(NumOfPoints));

    # Get Point Cloud Coordinates
    PointData = [];
    for ii in range(NumOfPoints):
        reading_line += 1;
        tmp_point_data = file_all_lines[reading_line].split();
        for jj in range(len(tmp_point_data)):
            tmp_point_data[jj] = float(tmp_point_data[jj].strip());
        PointData.append(tmp_point_data);

    # Output
    logger.info('Finish Importing {0}'.format(filePath));
    return NumOfPoints, PointData

## Export .pts file (Point Cloud Data)
def write_pts(filePath,pointData):
    logger.info('Start Exporting {0}'.format(filePath));
    file = open(filePath,'w');

    # Write Number of Points
    file.write("{0}\n".format(len(pointData)));
    logger.info('Export {0} data'.format(len(pointData)));

    # Write Points Coordinates
    for ii in range(len(pointData)):
        for jj in range(len(pointData[ii])):
            file.write("{:.15E} ".format(pointData[ii][jj]));
        file.write("\n");

    # Exit
    file.close();
    logger.info('Finish Exporting {0}'.format(filePath));

## Check the functions
if __name__ == '__main__':
    logger.info('Print info of beads_pts.py ');
    print('Functions');
    print('  1. read_pts');
    print('  2. write_pts');
