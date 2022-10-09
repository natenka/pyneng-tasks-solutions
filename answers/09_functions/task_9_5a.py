# -*- coding: utf-8 -*-



trunk_cmd_list = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_dict = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

def generate_trunk_config(intf_vlan_dict, trunk_template):
    trunk_conf = {}
    for port, vlans in intf_vlan_dict.items():
        commands = []
        for command in trunk_template:
            if command.endswith("allowed vlan"):
                vlans_str = ",".join([str(vl) for vl in vlans])
                commands.append(f"{command} {vlans_str}")
            else:
                commands.append(command)
        trunk_conf[port] = commands
    return trunk_conf
