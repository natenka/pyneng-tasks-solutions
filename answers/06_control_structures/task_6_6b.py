# -*- coding: utf-8 -*-


while True:
    ip_address = input("Введите адрес: ")
    octets = ip_address.split(".")
    correct_ip = True

    if len(octets) != 4:
        correct_ip = False
        continue
    for octet in octets:
        if not (octet.isdigit() and int(octet) in range(256)):
            correct_ip = False
            break
    if correct_ip:
        break
    print("Неправильный IP-адрес")

first_octet = int(octets[0])

if 1 <= first_octet <= 223:
    print("unicast")
elif 224 <= first_octet <= 239:
    print("multicast")
elif ip_address == "0.0.0.0":
    print("unassigned")
elif ip_address == "255.255.255.255":
    print("local broadcast")
else:
    print("unused")

# еще один вариант
#
# while True:
#     ip = input("Введите IP-адрес в формате x.x.x.x: ")
#     octets = ip.split(".")
#     valid_ip = len(octets) == 4
#
#     for i in octets:
#         valid_ip = i.isdigit() and 0 <= int(i) <= 255 and valid_ip
#
#     if valid_ip:
#         break
#     print("Неправильный IP-адрес")
#
# if 1 <= int(octets[0]) <= 223:
#     print("unicast")
# elif 224 <= int(octets[0]) <= 239:
#     print("multicast")
# elif ip == "255.255.255.255":
#     print("local broadcast")
# elif ip == "0.0.0.0":
#     print("unassigned")
# else:
#     print("unused")
