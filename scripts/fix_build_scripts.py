#!/usr/bin/python3

import os
import sys

HOME = os.path.expanduser('~')
DEFINER_BUILDSCRIPTS_DIR = os.path.join(HOME, 'projects/demo/buildscripts')

if __name__ == '__main__':
    for dir_path, subpaths, files in os.walk(DEFINER_BUILDSCRIPTS_DIR, False):
            for f in files:
                buildscriptpath = os.path.join(dir_path, f)
                fp = open(buildscriptpath, 'r')
                lines = fp.readlines()
                fp.close()
                fw = open(buildscriptpath, 'w')
                for i in range(len(lines)):
                    if lines[i].strip().startswith('if option == \'compile\':'):
                        rm_line = lines[i+1]
                        if not rm_line.strip() == 'rm = which(\'rm\')':
                            print ('Fix ' + f)
                            lines.insert(i+1, '        rm = which(\'rm\')\n')
                            lines.insert(i+2, '        sub.call ([rm, \'-rf\', os.path.join(repopath, \'target/classes\')])\n')
                            break
                fw.write("".join(lines))
                fw.close()
