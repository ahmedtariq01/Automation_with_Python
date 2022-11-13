#!/usr/bin/env python3

import sys
import re

log_file = sys.argv[1]
with open(logfile) as f:
    for line in f:
        if 'CRON' not in line:
            continue
        pattern = r'USER \((\w+)\)$'
        result = re.search(pattern, line)
        print(line.strip())
        
        





