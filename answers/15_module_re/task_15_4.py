# -*- coding: utf-8 -*-

import re


def get_ints_without_description(config):
    regex = re.compile(r"!\ninterface (?P<intf>\S+)\n"
                       r"(?P<descr> description \S+)?")
    with open(config) as src:
        match = regex.finditer(src.read())
        result = [m.group('intf') for m in match if m.lastgroup == 'intf']
        return result


def get_ints_without_description(filename):
    result_list = []
    regex = r"^interface (?P<intf>\S+)|^ description (.+)\n"
    with open(filename) as f:
        for line in f:
            match_line = re.search(regex, line)
            if match_line:
                if match_line.lastgroup == "intf":
                    intf = match_line.group("intf")
                    result_list.append(intf)
                else:
                    result_list.remove(intf)
    return result_list
