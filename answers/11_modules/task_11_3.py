# -*- coding: utf-8 -*-



def parse_cdp_neighbors(command_output):
    """
    Тут мы передаем вывод команды одной строкой потому что именно в таком виде будет
    получен вывод команды с оборудования. Принимая как аргумент вывод команды,
    вместо имени файла, мы делаем функцию более универсальной: она может работать
    и с файлами и с выводом с оборудования.
    Плюс учимся работать с таким выводом.
    """
    result = {}
    for line in command_output.split("\n"):
        line = line.strip()
        columns = line.split()
        if ">" in line:
            hostname = line.split(">")[0]
        # 3 индекс это столбец holdtime - там всегда число
        elif len(columns) >= 5 and columns[3].isdigit():
            r_host, l_int, l_int_num, *other, r_int, r_int_num = columns
            result[(hostname, l_int + l_int_num)] = (r_host, r_int + r_int_num)
    return result


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))
