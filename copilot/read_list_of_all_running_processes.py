#!/bin/env python

OS = 'posix'

if OS is 'win32':

   import wmi

   # Initializing the wmi constructor
   f = wmi.WMI()
   
   # Printing the header for the later columns
   print("pid   Process name")

   # Iterating through all the running processes
   for process in f.Win32_Process():
       # Displaying the P_ID and P_Name of the process
       print(f"{process.ProcessId:<10} {process.Name}") 

elif OS == 'posix':

    import subprocess

    pl = subprocess.Popen(['ps', '-aux'], stdout=subprocess.PIPE).communicate()[0]

    print(pl)
