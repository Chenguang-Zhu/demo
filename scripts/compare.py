#!/usr/bin/python3

import os
import sys

HOME = os.path.expanduser('~')
DEFINER_LOGS_DIR = os.path.join(HOME, 'projects/demo-deps/logs')
DOSC_META_DIR = os.path.join(HOME, 'projects/DoSC/meta-data/all')

FEATURE_LIST = ['CALCITE-1003','COMPRESS-374','IO-148','LANG-906',
                 'CALCITE-1028','COMPRESS-375','IO-153','LANG-944',
                 'CALCITE-1168','CONFIGURATION-466','IO-173','LANG-993',
                 'CALCITE-1200','CONFIGURATION-624','IO-275','LANG-999',
                 'CALCITE-1288','CONFIGURATION-626','IO-288','MNG-4904',
                 'CALCITE-1309','CSV-159','IO-290','MNG-4909',
                 'CALCITE-1337','CSV-175','IO-291','MNG-4910',
                 'CALCITE-627','CSV-179','IO-297','MNG-4953',
                 'CALCITE-655','CSV-180','IO-305','MNG-5159',
                 'CALCITE-674','FLUME-1710','LANG-1006','MNG-5530',
                 'CALCITE-718','FLUME-2052','LANG-1015','MNG-5549',
                 'CALCITE-758','FLUME-2056','LANG-1021','MNG-5754',
                 'CALCITE-767','FLUME-2130','LANG-1033','MNG-5755',
                 'CALCITE-803','FLUME-2206','LANG-1050','MNG-5767',
                 'CALCITE-811','FLUME-2498','LANG-1074','MNG-5805',
                 'CALCITE-925','FLUME-2628','LANG-1080','NET-436',
                 'CALCITE-991','FLUME-2955','LANG-1088','NET-525',
                 'CALCITE-996','FLUME-2982','LANG-1093','NET-527',
                 'COMPRESS-295','IO-126','LANG-1119','PDFBOX-3069',
                 'COMPRESS-296','IO-129','LANG-536','PDFBOX-3262',
                 'COMPRESS-313','IO-130','LANG-825','PDFBOX-3307',
                 'COMPRESS-327','IO-135','LANG-834','PDFBOX-3418',
                 'COMPRESS-368','IO-138','LANG-839','PDFBOX-3461',
                 'COMPRESS-369','IO-144','LANG-841',
                 'COMPRESS-373','IO-145','LANG-883']

if __name__ == '__main__':
    for feature in FEATURE_LIST:
        fbench = open(os.path.join(DOSC_META_DIR, feature + '.yml'), 'r')
        benchlines = fbench.readlines()
        for i in range(len(benchlines)):
            if benchlines[i].strip() == 'history slice:':
                istart = i+1
            if benchlines[i].strip() == 'developer labeled commits:':
                iend = i-1
        history_slice = benchlines[istart : iend + 1]
        for idx in range(len(history_slice)):
            history_slice[idx] = history_slice[idx].strip().split('\"')[1]
        fbench.close()

        #print (history_slice)
                
        flog = open(os.path.join(DEFINER_LOGS_DIR, feature + '.log'), 'r')
        loglines = flog.readlines()
        hstar = []
        for j in range(len(loglines)):
            if loglines[j].startswith('[OUTPUT] H*: '):
                hstar.append(loglines[j].split(': ')[1].strip())
        flog.close()

        #print (hstar)

        if history_slice == hstar:
            print (feature + ': ' + 'YES')
        else:
            print (feature + ': ' + 'NO')
