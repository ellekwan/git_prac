#!/usr/bin/python

import os, re, glob

logfile = '/home/ellekwan/Envs/messages'
#logfile = input("Which file would you like to open? \n ==>").strip()
#or create menu from os.listdir()



########creates a file consecutive to maximum existing filename

init_file = 'call_lic_consumed-v01.txt'

#create list of glob filenames = versions
versions = glob.glob('call_lic_consumed-v*.txt')

#prevent iteration over empty list if init_file does not exist.
if len(versions) != 0:
    for name in versions:
        if os.path.exists(name):
            filename = max(versions)
#select maximum existing version (digits in filename) +1
            mdig = re.findall(r'\d+', filename)
            while os.path.exists(filename):
                for i in mdig:
                    i = int(i)+1
                    filename = 'call_lic_consumed-v{0}.txt'.format(i)
else: 
    filename = init_file


strfind = "LicenseMgr: Call license consumed"
###(change string search)
#    "ERROR: LicenseMgr - License <"
#    "EchoServer: ECHO client <13>"

###list occurences of string in lines of log file
ls_res = []

###open and close the read/write files asap to prevent corruption
readfil = open(logfile , 'r')

for line in readfil:
    if strfind in line: 
        ls_res.append(str(line))

writfil = open(filename, 'w')
###print list, add list of string occurences to new file
for el in ls_res:
    print(str(el))
    writfil.write(el)

readfil.close
writfil.close

print(str("New file "+filename+" has been created."))
print("Complete.")
exit(0)
