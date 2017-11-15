import os
import os.path
import sys
import csv
import subprocess as sub

def isexec (fpath):
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

if __name__ == '__main__':
    option = sys.argv[1]
    repopath = sys.argv[2]
    mvn = which('mvn')
    os.chdir(repopath)
    
    if option == 'compile':
        rm = which('rm')
        sub.call ([rm, '-rf', os.path.join(repopath, 'target/classes')])
        ret = sub.call ([mvn, 'compiler:compile'])
        if ret == 0:
            sys.exit(0)
        else:
            sys.exit(1)
    elif option == 'test':
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=FieldUtilsTest#testGetFieldsWithAnnotation'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=FieldUtilsTest#testGetFieldsWithAnnotationIllegalArgumentException1'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=FieldUtilsTest#testGetFieldsWithAnnotationIllegalArgumentException2'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=FieldUtilsTest#testGetFieldsWithAnnotationIllegalArgumentException3'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=FieldUtilsTest#testGetFieldsListWithAnnotation'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=FieldUtilsTest#testGetFieldsListWithAnnotationIllegalArgumentException1'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=FieldUtilsTest#testGetFieldsListWithAnnotationIllegalArgumentException2'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=FieldUtilsTest#testGetFieldsListWithAnnotationIllegalArgumentException3'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=MethodUtilsTest#testGetMethodsWithAnnotation'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=MethodUtilsTest#testGetMethodsWithAnnotationIllegalArgumentException1'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=MethodUtilsTest#testGetMethodsWithAnnotationIllegalArgumentException2'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=MethodUtilsTest#testGetMethodsWithAnnotationIllegalArgumentException3'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=MethodUtilsTest#testGetMethodsListWithAnnotation'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=MethodUtilsTest#testGetMethodsListWithAnnotationIllegalArgumentException1'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=MethodUtilsTest#testGetMethodsListWithAnnotationIllegalArgumentException2'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=MethodUtilsTest#testGetMethodsListWithAnnotationIllegalArgumentException3'])
        print ret
        if ret == 0:
            sys.exit(0)
        else:
            sys.exit(1)
