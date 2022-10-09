# -*- coding: utf-8 -*-


ignore_list = ["duplex", "alias exec", "Current configuration", "service"]

def ignore_line(line, ignore_lines):
    for ignore in ignore_lines:
        if ignore in line:
            return True
    return False


def clean_config(config_filename, ignore_lines):
    cfg_list = []
    with open(config_filename) as f:
        for line in f:
            if "!" not in line and not ignore_line(line, ignore_lines):
                cfg_list.append(line.rstrip())
    return cfg_list

