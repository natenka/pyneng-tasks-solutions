# -*- coding: utf-8 -*-

from sys import argv

ignore = ["duplex", "alias", "configuration", "end", "service"]

src_file, dst_file = argv[1], argv[2]

with open(src_file) as src, open(dst_file, 'w') as dst:
    for line in src:
        words = line.split()
        words_intersect = set(words) & set(ignore)
        if not line.startswith("!") and not words_intersect:
            dst.write(line)
