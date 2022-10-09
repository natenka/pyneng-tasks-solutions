# -*- coding: utf-8 -*-


mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]

result = []

for m in mac:
    result.append(m.replace(":", "."))

print(result)
