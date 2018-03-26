#!/usr/bin/python3

import os
import sys

HOME = os.path.expanduser('~')
CSLICER_LOGS_DIR = os.path.join(HOME, 'projects/demo/_results/cslicer')

if __name__ == '__main__':
    logs = [os.path.join(CSLICER_LOGS_DIR, log) for log in os.listdir(CSLICER_LOGS_DIR)]
    for log in logs:
        f = open(log, 'r')
        for l in f.readlines():
            if l.strip() == '[STATS] reduction.hunk : 100.0':
                print(log.split('/')[-1] + ': WRONG')
