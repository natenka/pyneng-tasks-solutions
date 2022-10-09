# -*- coding: utf-8 -*-


import yaml
from task_20_1 import generate_config

if __name__ == "__main__":
    with open("data_files/ospf.yml") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    print(generate_config("templates/ospf.txt", data))

# templates/ospf.txt
"""
router ospf {{ process }}
 router-id  {{ router_id }}
 auto-cost reference-bandwidth {{ ref_bw }}
{% for intf in ospf_intf %}
 network {{ intf.ip}} 0.0.0.0 area {{ intf.area }}
{% if intf.passive %}
 passive-interface {{ intf.name }}
{% endif %}
{% endfor %}

{% for intf in ospf_intf if not intf.passive %}
interface {{ intf.name }}
 ip ospf hello-interval 1
{% endfor %}
"""
