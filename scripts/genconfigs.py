#!/usr/bin/python3

import sys
import os

HOME = os.path.expanduser('~')
DOWNLOADS_DIR = os.path.join(HOME, 'projects/demo/_downloads')
DEFINER_CONFIGS_DIR = os.path.join(HOME, 'projects/demo/configs/definer')
CSLICER_CONFIGS_DIR = os.path.join(HOME, 'projects/demo/configs/cslicer')
DEFINER_BUILDSCRIPTS_DIR = os.path.join(HOME, 'projects/demo/buildscripts/definer')
DOSC_META_DIR = os.path.join(HOME, 'projects/DoSC/meta-data')

def extractInfoFromYml(filepath):
    f = open(filepath, 'r')
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i].strip()
        if line.startswith('name:'):
            repo_name = line.split(': ')[1].lower()
        if line.startswith('id:'):
            feature_id = line.split(': ')[1]
        if line.startswith('history start:'):
            start_sha = line.split(': ')[1]
        if line.startswith('history end:'):
            end_sha = line.split(': ')[1]
        if line.startswith('test suite:'):
            test_start_idx = i+1
        if line.startswith('history slice:'):
            test_end_idx = i-1
    f.close()
    test_methods = [ l.strip().split('\"')[1].replace('.', '#') for l in lines[test_start_idx : test_end_idx + 1] ]
    return repo_name, feature_id, start_sha, end_sha, test_methods

def genDefinerConfig(filepath):
    repo_name, feature_id, start_sha, end_sha, test_methods = extractInfoFromYml(filepath)
    if not os.path.isdir(os.path.join(DEFINER_CONFIGS_DIR, repo_name)):
        os.makedirs(os.path.join(DEFINER_CONFIGS_DIR, repo_name))
    fw = open(os.path.join(DEFINER_CONFIGS_DIR, repo_name + '/' + feature_id + '.properties'), 'w')
    fw.write('repoPath = ' + DOWNLOADS_DIR + '/' + repo_name + '/' + '.git\n')
    fw.write('startCommit = ' + start_sha + '\n')
    fw.write('endCommit = ' + end_sha + '\n')
    fw.write('buildScriptPath = ' + DEFINER_BUILDSCRIPTS_DIR + '/' + repo_name + '/' + 'comp_test_' + feature_id + '.py\n')
    fw.close()

def genCSlicerConfig(filepath):
    repo_name, feature_id, start_sha, end_sha, test_methods = extractInfoFromYml(filepath)
    if not os.path.isdir(os.path.join(CSLICER_CONFIGS_DIR, repo_name)):
        os.makedirs(os.path.join(CSLICER_CONFIGS_DIR, repo_name))
    fw = open(os.path.join(CSLICER_CONFIGS_DIR, repo_name + '/' + feature_id + '.properties'), 'w')
    fw.write('repoPath = ' + DOWNLOADS_DIR + '/' + repo_name + '/' + '.git\n')
    #fw.write('sourceRoot = ' + DOWNLOADS_DIR + '/' + repo_name + '/src/main/java\n')
    #fw.write('classRoot = ' + DOWNLOADS_DIR + '/' + repo_name + '/target/classes\n')
    #fw.write('execPath = ')
    fw.write('startCommit = ' + start_sha + '\n')
    fw.write('endCommit = ' + end_sha + '\n')
    fw.write('buildScriptPath = ' + DOWNLOADS_DIR + '/' + repo_name + '/' + 'pom.xml\n')
    fw.write('testScope = ' + ','.join(test_methods))
    fw.close()

if __name__ == '__main__':
    tool = sys.argv[1]
    for dir_path, subpaths, files in os.walk(DOSC_META_DIR, False):
        for f in files:
            if f.endswith('.yml'):
                filepath = os.path.join(dir_path, f)
                if tool == 'definer':
                    genDefinerConfig(filepath)
                elif tool == 'cslicer':
                    genCSlicerConfig(filepath)
