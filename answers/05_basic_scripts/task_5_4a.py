# -*- coding: utf-8 -*-


network = input("Enter network address: ")

ip, mask = network.split()
ip_list = ip.split(".")
mask_list = mask.split(".")

oct1, oct2, oct3, oct4 = [
    int(ip_list[0]),
    int(ip_list[1]),
    int(ip_list[2]),
    int(ip_list[3]),
]

m1, m2, m3, m4 = [
    int(mask_list[0]),
    int(mask_list[1]),
    int(mask_list[2]),
    int(mask_list[3]),
]
bin_mask = "{:08b}{:08b}{:08b}{:08b}".format(m1, m2, m3, m4)
mask = bin_mask.count("1")

ip_output = """
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}"""

mask_output = """
Mask:
/{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
"""

print(ip_output.format(oct1, oct2, oct3, oct4))
print(mask_output.format(mask, m1, m2, m3, m4))
