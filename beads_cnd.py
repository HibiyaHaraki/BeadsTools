#!/usr/bin/env python3

# beads_cnd.py
#
# created by Hibiya Haraki
# All risks of running this script is always with you.
#
# Explanation
#  In this file, there are some functions for treating ADVENTURE .cnd file (See ADVENTURE BCtool Document) in Python
#
# Functions
#  1. read_cnd
#

import sys
from . import beads_log

logger = beads_log.root_logger();

## Import .cnd file (See ADVENTURE BCtool) and get surface ID of arbitrary Transient Temperature ID
def read_cnd(filePath,transientID):
    logger.info('Start Importing {0}'.format(filePath));
    file = open(filePath,'r');
    file_all_lines = file.readlines();
    file.close();

    # Search and get Surface ID from inputted Transient ID
    logger.info('Searching Transinet ID {0}'.format(transientID));
    ans = [];
    for ii in range(len(file_all_lines)):
        tmp = file_all_lines[ii].split();
        if (tmp[0] == 'Transient' and int(tmp[1]) == transientID):
            ans.append(int(tmp[3]));

    # Check Output
    if (ans == []):
        logger.error('Please input correct Transient Temperature ID');
        sys.exit();

    # Output
    logger.info('Finish Importing {0}'.format(filePath));
    return ans

if __name__ == '__main__':
    logger.info('Print info of beads_cnd.py ');
    print('Functions');
    print('  1. read_cnd');
