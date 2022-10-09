# -*- coding: utf-8 -*-

from task_22_1 import parse_command_output


if __name__ == "__main__":
    with open("output/sh_ip_dhcp_snooping.txt") as show:
        output = show.read()
    result = parse_command_output("templates/sh_ip_dhcp_snooping.template", output)
    print(result)

# templates/sh_ip_dhcp_snooping.template
"""
Value mac (\S+)
Value ip (\S+)
Value vlan (\d+)
Value intf (\S+)


Start
  ^${mac}\s+${ip}\s+\d+\s+\S+\s+${vlan}\s+${intf} -> Record
"""
