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
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=ArrayUtilsTest#testIsSorted'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=ArrayUtilsTest#testIsSortedComparator'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=ArrayUtilsTest#testIsSortedNullComparator'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=ArrayUtilsTest#testIsSortedInt'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=ArrayUtilsTest#testIsSortedFloat'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=ArrayUtilsTest#testIsSortedLong'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=ArrayUtilsTest#testIsSortedDouble'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=ArrayUtilsTest#testIsSortedChar'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=ArrayUtilsTest#testIsSortedByte'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=ArrayUtilsTest#testIsSortedShort'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=ArrayUtilsTest#testIsSortedBool'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=BooleanUtilsTest#testCompare'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=CharUtilsTest#testCompare'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=NumberUtilsTest#compareInt'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=NumberUtilsTest#compareLong'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=NumberUtilsTest#compareShort'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=NumberUtilsTest#compareByte'])
        print ret
        if ret == 0:
            sys.exit(0)
        else:
            sys.exit(1)
