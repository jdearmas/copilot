#!/usr/bin/env python

import subprocess

command = " httpd -t -D DUMP_INCLUDES " 

res = subprocess.call(command, shell = True)
#the method returns the exit code

print("{}", res)
