# -*- coding: utf-8 -*-


nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
nat_gig = nat.replace("Fast", "Gigabit")
print(nat_gig.lower())

# version 2
# nat_gig = nat.lower().replace("fast", "gigabit")
# print(nat_gig)
