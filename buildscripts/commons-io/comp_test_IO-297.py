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
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=CharSequenceInputStreamTest#testUTF8WithSingleByteRead'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=CharSequenceInputStreamTest#testLargeUTF8WithSingleByteRead'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=CharSequenceInputStreamTest#testUTF8WithBufferedRead'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=CharSequenceInputStreamTest#testLargeUTF8WithBufferedRead'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=CharSequenceInputStreamTest#testUTF16WithSingleByteRead'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=CharSequenceInputStreamTest#testReadZero'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=CharSequenceInputStreamTest#testCharsetMismatchInfiniteLoop'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=CharSequenceInputStreamTest#testSkip'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=CharSequenceInputStreamTest#testMarkReset'])
        print ret      
        if ret == 0:
            sys.exit(0)
        else:
            sys.exit(1)
