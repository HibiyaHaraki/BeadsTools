#!/usr/bin/env python3

# beads_log.py
#
# created by Hibiya Haraki
# All risks of running this script is always with you.
#
# Explanation
#  In this file, there setting of logging for BeadsTools. This script needs Package 'logging'.
#
# Function
#  1. root_logger
#

import os
import sys
import logging

def root_logger():
    logger = logging.getLogger('BeadsTools_Log');
    logger.setLevel(10);
    if not logger.hasHandlers():
        sh = logging.StreamHandler();
        logger.addHandler(sh);
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d %(message)s');
        sh.setFormatter(formatter);
    return logger;

if __name__ == '__main__':
    logger.info('Print info of beads_log.py ');
    print('Functions');
    print('  1. root_logger');
