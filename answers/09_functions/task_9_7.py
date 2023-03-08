# -*- coding: utf-8 -*-

ignore = ["duplex", "alias", "configuration"]


def ignore_command(command, ignore_list):
    for word in ignore_list:
        if word in command:
            return True
    return False


def convert_config_to_dict(config_filename, ignore_lines):
    config_dict = {}
    with open(config_filename) as f:
        for line in f:
            line = line.rstrip()
            if line and not (
                line.startswith("!") or ignore_command(line, ignore_lines)
            ):
                if line[0].isalnum():
                    section = line
                    config_dict[section] = []
                else:
                    config_dict[section].append(line.strip())
    return config_dict
