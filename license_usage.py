#!/usr/bin/python

import os, re, glob

"""
Written by Isabelle Kwan for Armour Communications Ltd
Copyright 2015-2016 Armour Communications Ltd
Please note that this is an unsupported program,
and is not meant for production use

Usage:
python license_usage.py

Output:
call_lic_consumed-v*.txt
"""


strfind = "LicenseMgr: Call license consumed"
file_name = None

logfile = input("which file would you like to open: ").strip()
#logfile = '/var/log/messages'

readfil = open(logfile, 'r')

# creates a file consecutive to maximum existing filename
versions = glob.glob('call_lic_consumed-v*.txt')
if len(versions) != 0:
    for name in versions:
        if name != '' and os.path.exists(name):
            file_name = max(versions)
            mdig = re.findall(r'\d+', file_name)
            while os.path.exists(file_name):
                for i in mdig:
                    i = int(i)+1
                    file_name = 'call_lic_consumed-v{0}.txt'.format(i)

else:
    file_name = 'call_lic_consumed-v01.txt'


writfil = open(file_name, 'w')

ls_res = []

for line in readfil:
# list occurrences of string in lines of log file
    if strfind in line:
        ls_res.append(str(line))

for el in ls_res:
    writfil.write(el)

readfil.close()
