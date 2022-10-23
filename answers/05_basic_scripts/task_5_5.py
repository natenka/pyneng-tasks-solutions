# -*- coding: utf-8 -*-


access_template = """switchport mode access
switchport access vlan {}
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
"""

trunk_template = """switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan {}
"""
template = {"access": access_template, "trunk": trunk_template}

mode = input("Enter interface mode (access/trunk): ")
interface = input("Enter interface type and number: ")
vlans = input("Enter VLAN(s) number: ")

print(f"interface {interface}")
print(template[mode].format(vlans))
