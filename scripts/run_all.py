#!/usr/bin/python3

import sys
import os
import shutil
import time
import subprocess as sub

HOME = os.path.expanduser('~')
DOWNLOADS_DIR = os.path.join(HOME, 'projects/demo/_downloads')
RESULTS_DIR = os.path.join(HOME, 'projects/demo/_results')
DEFINER_CONFIGS_DIR = os.path.join(HOME, 'projects/demo/configs/definer')
CSLICER_CONFIGS_DIR = os.path.join(HOME, 'projects/demo/configs/cslicer')
BUILDSCRIPTS_DIR = os.path.join(HOME, 'projects/demo/buildscripts')

DEFINER_JAR_DIR = os.path.join(HOME, 'projects/gitslice/target/cslicer-1.0.0-jar-with-dependencies.jar')
DOSC_META_DIR = os.path.join(HOME, 'projects/DoSC/meta-data')

REPO_LIST=[
    'https://github.com/MSR-2017/commons-lang',
    'https://github.com/MSR-2017/calcite',
    'https://github.com/MSR-2017/commons-compress',
    'https://github.com/MSR-2017/commons-configuration',
    'https://github.com/MSR-2017/commons-csv',
    'https://github.com/MSR-2017/commons-io',
    'https://github.com/MSR-2017/commons-net',
    'https://github.com/MSR-2017/flume',
    'https://github.com/MSR-2017/maven',
    'https://github.com/MSR-2017/pdfbox'
]

# Utility functions
def isexec(fpath):
    if fpath == None: return False
    return os.path.isfile(fpath) and os.access(fpath, os.X_OK) 

def which(program):
    fpath, fname = os.path.split(program)
    if fpath:
        if isexec (program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if isexec (exe_file):
                return exe_file
    return None

git = which('git')
mvn = which('mvn')
java = which('java')

def extarctConfig(configfilepath):
    f = open(configfilepath, 'r')
    feature_id = configfilepath.split('/')[-1].split('.')[0]
    for line in f.readlines():
        line = line.strip()
        if line.startswith('repoPath ='):
            repo_name = line.split('/')[-2]
        if line.startswith('endCommit ='):
            end_sha = line.split(' = ')[1]
        #if line.startswith('buildScriptPath ='):
        #    feature_id = line.split('/')[-1].replace('comp_test_', '').replace('.py', '')
    f.close()
    return repo_name, end_sha, feature_id

def runOneFeature(configfilepath):
    repo_name, end_sha, feature_id = extarctConfig(configfilepath)
    # Build at the end version
    os.chdir(DOWNLOADS_DIR + '/' + repo_name)
    sub.run([git, 'checkout', end_sha],
                  stdout=open(RESULTS_DIR + '/mvn/' + feature_id + '.mvnlog', 'w'),
                  stderr=open(RESULTS_DIR + '/mvn/' + feature_id + '.mvnlog', 'w')
    )
    sub.run([mvn, 'clean', 'install', '-DskipTests'],
                  stdout=open(RESULTS_DIR + '/mvn/' + feature_id + '.mvnlog', 'a'),
                  stderr=open(RESULTS_DIR + '/mvn/' + feature_id + '.mvnlog', 'a')
    )
    
    start_time = time.time()
    try:
        p = sub.run([java, '-jar', DEFINER_JAR_DIR, '-c', configfilepath, '-e', 'refiner', '-l', 'noinv'],
                  stdout=open(RESULTS_DIR + '/definer/' + feature_id + '.log', 'w'),
                  stderr=open(RESULTS_DIR + '/definer/' + feature_id + '.log', 'w'),
                  timeout=7200
        )
    except sub.TimeoutExpired:
        print('SUBPROCESS KILLED')
        p.kill()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('Definer: Feature ' + feature_id + ', Starts at ' + str(start_time) + ', Ends at ' + str(end_time) + ', Elapsed time ' + str(elapsed_time))

    if not p.returncode == 0:
        print('TIMEOUT!\n')

def runCSlicerOneFeature(configfilepath):
    repo_name, end_sha, feature_id = extarctConfig(configfilepath)
    #print (repo_name, end_sha, feature_id)

    start_time = time.time()

    sub.run([java, '-jar', DEFINER_JAR_DIR, '-c', configfilepath, '-e', 'slicer'],
            stdout=open(RESULTS_DIR + '/cslicer/' + feature_id + '.log', 'w'),
            stderr=open(RESULTS_DIR + '/cslicer/' + feature_id + '.log', 'w'),
    )
    
    end_time = time.time()
    elapsed_time = end_time - start_time

    print('CSlicer: Feature ' + feature_id + ', Starts at ' + str(start_time) + ', Ends at ' + str(end_time) + ', Elapsed time ' + str(elapsed_time))

if __name__ == '__main__':
    tool = sys.argv[1]
    '''
    clean projects
    clone projects
    for each properties file
        get project name
        get end sha
        go to project dir
        checkout end sha
        mvn clean install -DskipTests
        gitslice -c properties -e refiner -l noinv > log file
    '''
    if os.path.isdir(DOWNLOADS_DIR):
        shutil.rmtree(DOWNLOADS_DIR)
        
    os.makedirs(DOWNLOADS_DIR)    
    os.chdir(DOWNLOADS_DIR)
    for repo in REPO_LIST:
        sub.call([git, 'clone', repo])

    if tool == 'definer':
        for dir_path, subpaths, files in os.walk(DEFINER_CONFIGS_DIR, False):
            for f in files:
                configfilepath = os.path.join(dir_path, f)
                runOneFeature(configfilepath)

    elif tool == 'cslicer':
        for dir_path, subpaths, files in os.walk(CSLICER_CONFIGS_DIR, False):
            for f in files:
                configfilepath = os.path.join(dir_path, f)
                runCSlicerOneFeature(configfilepath)
