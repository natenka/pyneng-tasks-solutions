# -*- coding: utf-8 -*-


access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {
    "0/1": ["add", "10", "20", "30", "40"],
    "0/2": ["only", "11", "30"],
    "0/4": ["del", "17"],
    "0/5": ["add", "10", "21"],
    "0/7": ["only", "30"],
}

for intf, value in trunk.items():
    print(f"interface FastEthernet{intf}")
    for command in trunk_template:
        if command.endswith("allowed vlan"):
            action = value[0]
            vlans = ",".join(value[1:])

            if action == "add":
                print(f" {command} add {vlans}")
            elif action == "only":
                print(f" {command} {vlans}")
            elif action == "del":
                print(f" {command} remove {vlans}")
        else:
            print(f" {command}")


# dict instead of if/else
trunk_actions = {"add": " add", "del": " remove", "only": ""}

for intf, value in trunk.items():
    print(f"interface FastEthernet{intf}")

    for command in trunk_template:
        if command.endswith("allowed vlan"):
            action = value[0]
            vlans = ",".join(value[1:])
            print(f" {command}{trunk_actions[action]} {vlans}")
        else:
            print(f" {command}")

# replace
for intf, allowed in trunk.items():
    action = (
        allowed[0].replace("only", "").replace("del", " remove").replace("add", " add")
    )
    vlans = ",".join(allowed[1:])

    print(f"interface FastEthernet{intf}")
    for command in trunk_template:
        if command.endswith("allowed vlan"):
            print(f" {command}{action} {vlans}")
        else:
            print(f" {command}")
