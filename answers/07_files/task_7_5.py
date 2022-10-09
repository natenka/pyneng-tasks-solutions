# -*- coding: utf-8 -*-

from pprint import pprint
import sys

config = sys.argv[1]

interface_dict = {}
with open(config) as cfg:
    for line in cfg:
        if line.startswith("interface") and "Ethernet" in line:
            intf = line.split()[1]
            interface_dict[intf] = []
        elif line.startswith(" switchport"):
            interface_dict[intf].append(line.strip())
pprint(interface_dict, width=60)

