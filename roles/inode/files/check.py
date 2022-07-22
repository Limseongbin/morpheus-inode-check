#!/usr/bin/python3

import sys

inventoryHostname = sys.argv[1]

f = open('/tmp/inode_check/'+inventoryHostname+'.log', 'r')
lines = f.readline()
for i in lines:
   print(i)
