#!/usr/bin/env python3

# beads_judge.py
#
# created by Hibiya Haraki
# All risks of running this script is always with you.
#
# Explanation
#  In this file, there are some functions for finding nodes or elements that is satisfied arbitrary equations
#
# Functions
#  1. judge_nodes
#  2. judge_elemments
#

import sys
from . import beads_log

logger = beads_log.root_logger();

## Finding Nodes that is satisfying arbitrary equation
def judge_nodes(equation,Nodes):
    # Get equation and create function
    eq = eval("lambda a: (lambda x, y, z: {0})"
            "(a[0], a[1], a[2])".format(equation));
    result = [];

    # Judging by equation
    for ii in range(len(Nodes)):
        judge = 0;
        judge = eq([Nodes[ii][0],Nodes[ii][1],Nodes[ii][2]]);
        if (judge > 0):
            result.append(1);
        else:
            result.append(0);

    # Output
    return result;

## Finding Elements that is satisfying awrbitrary equation
def judge_elements(equation,Nodes,Elements):
    # Get equation and create function
    eq = eval("lambda a: (lambda x, y, z: {0})"
            "(a[0], a[1], a[2])".format(equation));
    result = [];

    # Judging by equation
    for ii in range(len(Elements)):
        # Get Nodes coordinate in the Element
        nodes_coord = [];
        for jj in range(len(Elements[ii])):
            nodes_coord.append(Nodes[Elements[ii][jj]]);

        # Judge Nodes by Equation
        nodes_result = judge_nodes(equation,nodes_coord);

        # Judge Elements by Equation
        judge = 0;
        for jj in range(len(nodes_result)):
            if (nodes_result[jj] < 1):
                judge += 1;
        if (judge < 1):
            result.append(1);
        else:
            result.append(0);

    # Output
    return result;

if __name__ == '__main__':
    logger.info('Print info of beads_judge.py ');
    print('Functions');
    print('  1. judge_nodes');
    print('  2. judge_elements');
