# -*- coding: utf-8 -*-


ignore_list = ["duplex", "alias exec", "Current configuration", "service"]



def ignore_line(line, ignore_lines):
    for ignore in ignore_lines:
        if ignore in line:
            return True
    return False


def clean_config(
    config_filename,
    ignore_lines=None,
    ignore_exclamation=True,
    delete_empty_lines=True,
    strip_lines=False,
):
    cfg_list = []
    with open(config_filename) as f:
        for line in f:
            if ignore_exclamation and line.startswith("!"):
                continue
            if ignore_lines and ignore_line(line, ignore_lines):
                continue
            if delete_empty_lines and not line.strip():
                continue
            if strip_lines:
                line = line.strip()
            cfg_list.append(line)
    return cfg_list
