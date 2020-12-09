#!/bin/env python
# locate_main_configuration_file.py: locate apache's main configuration file

import os

filename = "httpd.conf"

# determine what os were are on
roots = {
    "posix":"/",
    "nt":"c:/"
}

root = roots[os.name]



def find_files(filename, search_path):
    result = []

    # Walking top-down from the root
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
            return result

print(find_files(filename,root))
