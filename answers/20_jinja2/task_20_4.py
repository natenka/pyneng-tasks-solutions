# -*- coding: utf-8 -*-

# templates/add_vlan_to_switch.txt
"""
vlan {{ vlan_id }}
 name {{ name }}

{% for int in access %}
interface {{ int }}
 switchport mode access
 switchport access vlan {{ vlan_id }}
{% endfor %}

{% for int in trunk %}
interface {{ int }}
 switchport trunk allowed vlan add {{ vlan_id }}
{% endfor %}
"""
