


def check_ip(ip_addr):
    octets = ip_addr.split(".")

    if len(octets) != 4:
        return False
    else:
        for octet in octets:
            if not (octet.isdigit() and int(octet) in range(256)):
                return False
    return True


def prompt_user_ip(max_retry=5, ensure_unicast=False):
    for _ in range(max_retry):
        ip = input("Введите правильный IP-адрес: ")
        if check_ip(ip):
            if ensure_unicast:
                octet1 = int(ip.split(".")[0])
                if 1 <= octet1 <= 223:
                    return ip
                else:
                    print("Введите IP-адрес в диапазоне unicast: 1-223")
            else:
                return ip
        else:
            print(f"Неправильный IP-адрес")
    raise ValueError(f"После {max_retry} попыток не был введен правильный адрес")

