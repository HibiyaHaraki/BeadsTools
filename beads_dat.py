#!/usr/bin/env python3

# beads_dat.py
#
# created by Hibiya Haraki
# All risks of running this script is always with you.
#
# Explanation
#  In this file, there are some functions for treating .dat file in Python
#
# Functions
#  1. read_dat
#  2. write_dat
#  3. compare_dat
#

import sys
from . import beads_log

logger = beads_log.root_logger();

## Import .dat file
def read_dat(filePath):
    logger.info('Start Importing {0}'.format(filePath));
    file = open(filePath,'r');
    file_all_lines = file.readlines();
    file.close();

    # Get Data Label
    reading_line = 0;
    tmp_data_label = file_all_lines[reading_line].split("=");
    dataLabel = tmp_data_label[1].strip();
    logger.info('Import {0} Data'.format(dataLabel));

    # Get Number of Data
    reading_line += 1;
    tmp_num_data = file_all_lines[reading_line].split("=");
    NumOfData = int(tmp_num_data[1].strip());
    logger.info('Import {0} Data'.format(NumOfData));

    # Get Data
    reading_line += 1;
    Data = [];
    for ii in range(NumOfData):
        reading_line += 1;
        tmp_data_line = file_all_lines[reading_line].split();
        tmp_data = [];
        for jj in range(len(tmp_data_line)-1):
            tmp_data.append(float(tmp_data_line[jj+1].strip()));
        Data.append(tmp_data);

    # Output
    logger.info('Finish Importing {0}'.format(filePath));
    return dataLabel, NumOfData, Data

## Export .dat file
def write_dat(filePath, dataLabel, Data):
    logger.info('Start Exporting {0}'.format(filePath));
    file = open(filePath,'w');

    # Write Data Label
    file.write('label={0}\n'.format(dataLabel));
    logger.info('Export {0} Data'.format(dataLabel));

    # Write Number of data
    file.write('num_items={0}\n\n'.format(len(Data)));
    logger.info('Export {0} Data'.format(len(Data)));

    # Write Data
    for ii in range(len(Data)):
        file.write("{0}: ".format(ii));
        for jj in range(len(Data[ii])):
            file.write("{:.8f} ".format(Data[ii][jj]));
        file.write("\n");

    # Exit
    file.close();
    logger.info('Finish Exporting {0}'.format(filePath));

## Compare two Data
def compare_dat(InfilePath1, InfilePath2, OutfilePath, method):
    logger.info('Start Comparing {0} and {1}'.format(InfilePath1,InfilePath2));

    # Get Data
    dataLabel1, NumData1, Data1 = read_dat(InfilePath1);
    dataLabel2, NumData2, Data2 = read_dat(InfilePath2);

    # Check Data
    if (NumData1 != NumData2):
        sys.exit("{0} and {1} should have same size Data!!".format(InfilePath1,InfilePath2));
    else:
        for ii in range(NumData1):
            if (len(Data1[ii]) != len(Data2[ii])):
                sys.exit("{0} and {1} should have same size Data ({3} Data)!!".format(InfilePath1,InfilePath2),ii);

    # Comapare data
    NewData = [];
    if (method == "0"):
        for ii in range(NumData1):
            tmp_newdata = [];
            for jj in range(len(Data1[ii])):
                tmp_newdata.append(Data1[ii][jj]-Data2[ii][jj]);
            NewData.append(tmp_newdata);
    elif (method == "1"):
        for ii in range(NumData1):
            tmp_newdata = [];
            for jj in range(len(Data1[ii])):
                tmp_newdata.append(abs(Data1[ii][jj]-Data2[ii][jj]));
            NewData.append(tmp_newdata);
    else:
        sys.exit("Please choose correct method.");

    # Output data
    write_dat(OutfilePath,"{0}Error".format(dataLabel1),NewData);
    logger.info('Finish Comparing and export {0}'.format(OutfilePath));

## Judge same dat file or not
def issamedat(InfilePath1, InfilePath2):
    # Get Data
    dataLabel1, NumData1, Data1 = read_dat(InfilePath1);
    dataLabel2, NumData2, Data2 = read_dat(InfilePath2);

    # Check Data
    if (NumData1 != NumData2):
        sys.exit("{0} and {1} should have same size Data!!".format(InfilePath1,InfilePath2));
    else:
        for ii in range(NumData1):
            if (len(Data1[ii]) != len(Data2[ii])):
                sys.exit("{0} and {1} should have same size Data ({3} Data)!!".format(InfilePath1,InfilePath2),ii);

    # Output
    return Data1 == Data2

## Check the functions
if __name__ == '__main__':
    logger.info('Print info of beads_dat.py ');
    print('Functions');
    print('  1. read_dat');
    print('  2. write_dat');
    print('  3. compare_dat');
    print('  4. issamedat')
