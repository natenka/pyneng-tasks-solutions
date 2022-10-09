# -*- coding: utf-8 -*-

from pprint import pprint
import sys

config = sys.argv[1]
trunk_dict = {}
with open(config) as cfg:
    for line in cfg:
        line = line.rstrip()
        if line.startswith("interface"):
            intf = line.split()[1]
        elif "trunk allowed" in line:
            trunk_dict[intf] = line.split()[-1].split(",")
pprint(trunk_dict)

