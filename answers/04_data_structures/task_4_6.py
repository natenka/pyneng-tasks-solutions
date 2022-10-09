# -*- coding: utf-8 -*-


ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""
route = ospf_route.replace(",", " ").replace("[", "").replace("]", "")
route = route.split()

print(template.format(route[0], route[1], route[3], route[4], route[5]))
