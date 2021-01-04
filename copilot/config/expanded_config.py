# expanded_config.py: create the entire, expanded, currently-running
#                     httpd config file

import check_httpd_config 
import read_config 
import re

res = check_httpd_config.check_httpd_config()


def convert_to_list(res):
 return [re.sub('^\((\d|\*)*\).', "",i.lstrip().rstrip()) for i in res.stdout.split('\n')[1:] if i is not None]

configs = convert_to_list(res)

configs = configs[:-1]

[read_config.read_config(config) for config in configs]
expanded_config = [read_config.read_config(config) for config in configs]
