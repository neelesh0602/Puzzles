# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 16:04:14 2018

@author: neelesh
"""

#!/usr/bin/python

import os, sys
import os.path
import csv
import requests
import subprocess
from datetime import datetime
import time
import json

input_file='test1_csv'
out_file='test2.csv'

"""<<<Real code of the program starts here >>>"""

if not os.path.exists (out_file):
    open(out_file, 'w').close()

## Now read the details of all assets with high loudness levels
with open('input_file', 'r') as fin:
    data = fin.read().splitlines(True)
with open('input_file', 'w') as fout:
    fout.writelines(data[1:])