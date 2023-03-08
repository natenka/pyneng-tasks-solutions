# -*- coding: utf-8 -*-

import re


def get_ip_from_cfg(config):
    regex = r"ip address (\S+) (\S+)"
    with open(config) as f:
        result = [m.groups() for m in re.finditer(regex, f.read())]
    return result


def get_ip_from_cfg(config):
    regex = r"ip address (\S+) (\S+)"
    result = []
    with open(config) as f:
        for line in f:
            m = re.search(regex, line)
            if m:
                result.append(m.groups())
    return result


if __name__ == "__main__":
    print(get_ip_from_cfg("config_r1.txt"))
