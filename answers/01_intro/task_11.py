
colors = ["Green", 'RED', 'Pink', 'YELLOW', 'white', 'Black']

# 1
user_color = input('Введіть колір: ')
found_color = False
for color in colors:
    if user_color.lower() == color.lower():
        found_color = True

if found_color:
    print('Такий колір є')
else:
    print('У списку colors немає такого кольору')


# 2
colors = ["Green", 'RED', 'Pink', 'YELLOW', 'white', 'Black']
colors_lower = []
for color in colors:
    colors_lower.append(color.lower())

user_color = input('Введіть колір: ')
if user_color.lower() in colors_lower:
    print("Такий колір є")
else:
    print("У списку colors немає такого кольору")

# 3

colors = ["Green", 'RED', 'Pink', 'YELLOW', 'white', 'Black']
user_color = input("Введіть колір: ")
message = "У списку colors немає такого кольору"
for color in colors:
    if user_color.lower() == color.lower():
        message = "Такий колір є"
print(message)

