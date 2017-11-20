#!/usr/bin/python3

import os
import sys
import matplotlib.pyplot as plt

HOME = os.path.expanduser('~')
DOSC_DIR = os.path.join(HOME, 'projects/DoSC/meta-data/all')

if __name__ == '__main__':
    feature_list = sorted(os.listdir(DOSC_DIR))
    for i in range(len(feature_list)):
        feature_list[i] = feature_list[i].replace('.yml', '')

    PR_Y = []
    RC_X = []
    for f in feature_list:
        fbench = open(os.path.join(DOSC_DIR, f + '.yml'), 'r')
        benchlines = fbench.readlines()
        for i in range(len(benchlines)):
            if benchlines[i].strip() == 'history slice:':
                istart = i+1
            if benchlines[i].strip() == 'developer labeled commits:':
                iend = i-1
                jstart = i+1
                if not benchlines[len(benchlines)-1].strip() == '':
                    jend = len(benchlines)-1
        history_slice = benchlines[istart : iend + 1]
        develop_labeled = benchlines[jstart : jend + 1]

        intersect = list(set(history_slice) & set(develop_labeled))

        PR = float(len(intersect) / len(history_slice))
        RC = float(len(intersect) / len(develop_labeled))

        PR_Y.append(PR)
        RC_X.append(RC)

        print(f, 'PR:' + "{0:.2f}".format(PR), 'RC:' + "{0:.2f}".format(RC))
        
        fbench.close()

    #RC_X = sorted(RC_X)

    fig, ax = plt.subplots()
    ax.scatter(RC_X, PR_Y, s=80.0, c='blue', marker='*', zorder=3)
    ax.set_xlabel(xlabel='Recall', fontsize=14)
    ax.set_ylabel(ylabel='Precision', fontsize=14)
    ax.grid(zorder=0)

    fig.savefig(os.path.join(HOME, "projects/cslicer-cloud/ICSE2018_Demo/figures/pr-rc-curve.eps"))
    plt.show()
