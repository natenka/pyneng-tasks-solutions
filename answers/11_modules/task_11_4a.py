# -*- coding: utf-8 -*-


infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]


def unique_network_map(topology_dict):
    network_map = {}
    for key, value in topology_dict.items():
        if not network_map.get(value) == key:
            network_map[key] = value
    return network_map


# второй вариант решения
def unique_network_map(topology_dict):
    network_map = {}
    for key, value in topology_dict.items():
        key, value = sorted([key, value])
        network_map[key] = value
    return network_map

