#!/usr/bin/python

import sys
import os

HOME = os.path.expanduser('~')
DOWNLOADS_DIR = os.path.join(HOME, 'projects/demo/_downloads')
CONFIGS_DIR = os.path.join(HOME, 'projects/demo/configs')
BUILDSCRIPTS_DIR = os.path.join(HOME, 'projects/demo/buildscripts')
DOSC_META_DIR = os.path.join(HOME, 'projects/DoSC/meta-data')

def genConfigFromYml(filepath):
    f = open(filepath, 'r')
    for line in f.readlines():
        line = line.strip()
        if line.startswith('name:'):
            repo_name = line.split(': ')[1].lower()
        if line.startswith('id:'):
            feature_id = line.split(': ')[1]
        if line.startswith('history start:'):
            start_sha = line.split(': ')[1]
        if line.startswith('history end:'):
            end_sha = line.split(': ')[1]
    f.close()

    #print repo_name, feature_id, start_sha, end_sha
            
    if not os.path.isdir(os.path.join(CONFIGS_DIR, repo_name)):
        os.makedirs(os.path.join(CONFIGS_DIR, repo_name))
    fw = open(os.path.join(CONFIGS_DIR, repo_name + '/' + feature_id + '.properties'), 'w')
    fw.write('repoPath = ' + DOWNLOADS_DIR + '/' + repo_name + '/' + '.git\n')
    fw.write('startCommit = ' + start_sha + '\n')
    fw.write('endCommit = ' + end_sha + '\n')
    fw.write('buildScriptPath = ' + BUILDSCRIPTS_DIR + '/' + repo_name + '/' + 'comp_test_' + feature_id + '.py\n')
    fw.close()

if __name__ == '__main__':
    for dir_path, subpaths, files in os.walk(DOSC_META_DIR, False):
        for f in files:
            if f.endswith('.yml'):
                filepath = os.path.join(dir_path, f)
                genConfigFromYml(filepath)
