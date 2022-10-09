# -*- coding: utf-8 -*-


data = ["a", "100", "30", 10.5, 20, "test", "15", 100]
result = []
for item in data:
    try:
        item_int = int(item)
    except ValueError:
        pass
    else:
        result.append(item_int)

print(result)
