# -*- coding: utf-8 -*-

access_dict = {"FastEthernet0/12": 10, "FastEthernet0/14": 11}
access_dict_2 = {
    "FastEthernet0/3": 100,
    "FastEthernet0/7": 101,
    "FastEthernet0/9": 107,
    "FastEthernet0/10": 111,
}

access_cmd_list = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]
cmd_list = ["switchport mode access", "switchport access vlan"]



def generate_access_config(intf_vlan_dict, access_template):
    access_list = []
    for intf, vlan in intf_vlan_dict.items():
        access_list.append(f"interface {intf}")
        for command in access_template:
            if command.endswith("access vlan"):
                access_list.append(f"{command} {vlan}")
            else:
                access_list.append(command)
    return access_list
