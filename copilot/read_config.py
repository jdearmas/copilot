#!/bin/env python

import sys

for data in sys.stdin:
        sys.stdout.write(data)

print(data[2:-3])

with open(data[2:-3], 'r') as f:
    for line in f:
        print(line)
    

