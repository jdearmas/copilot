import subprocess

import os

# test_if_running: tests to see if Apache HTTP is running
def test_if_running():

    cmd = "systemctl status httpd"

    returned_value = os.system(cmd)
