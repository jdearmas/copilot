#!/usr/bin/env python

from subprocess import PIPE, run


def check_httpd_config():
    command = ["httpd", "-t", "-D", "DUMP_INCLUDES"]
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    return result
