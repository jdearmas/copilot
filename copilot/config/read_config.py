#!/bin/env python

def read_config(pathname):
    with open(pathname, 'r') as f:
       return [line for line in f]
    

