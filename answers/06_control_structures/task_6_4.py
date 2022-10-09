# -*- coding: utf-8 -*-


files = [
    "cfg_1.txt", "cfg_4.txt", "cfg_8.txt", "cfg_9.txt", "cfg_12.txt", "cfg_15.txt"
]

result = []
for file in files:
    name = file.split(".")[0]
    num = name.split("_")[-1]
    new_num = "{:02}".format(int(num))
    new_name = file.replace(num, new_num)
    result.append(new_name)
print(result)

result = []
for file in files:
    name, ext = file.split(".")
    name_part, num = name.split("_")
    new_num = f"{int(num):02}"
    new_name = f"{name_part}_{new_num}.{ext}"
    result.append(new_name)
print(result)
