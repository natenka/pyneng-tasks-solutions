# -*- coding: utf-8 -*-


ignore_list = ["duplex", "alias exec", "Current configuration", "service"]


def containes_line(line, ignore_lines):
    for ignore in ignore_lines:
        if ignore in line:
            return True
    return False


def clean_config(config_filename, ignore_lines=None, ignore_exclamation=True,
                 delete_empty_lines=True, strip_lines=False):
    cfg_list = []
    with open(config_filename) as f:
        for line in f:
            if ignore_exclamation and line.startswith("!"):
                continue
            if ignore_lines and containes_line(line, ignore_lines):
                continue
            if delete_empty_lines and not line.strip():
                continue
            if strip_lines:
                line = line.strip()
            cfg_list.append(line)
    return cfg_list


def clean_config(config_filename, ignore_lines=None, ignore_exclamation=True,
                 strip_lines=False, delete_empty_lines=True):
    with open(config_filename, "r") as file:
        result = []
        for line in file:
            append_line = True
            if not line.strip() and delete_empty_lines == True:
                append_line = False
            if ignore_exclamation and line.startswith("!"):
                append_line = False
            if ignore_lines and containes_line(line, ignore_lines):
                append_line = False
            if strip_lines:
                line = line.strip()
            if append_line:
                result.append(line)
    return result
