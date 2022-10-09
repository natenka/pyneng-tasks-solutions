# -*- coding: utf-8 -*-


from random import randint

random_number = randint(1, 9)
print(random_number)
attempts = 5
for attempt in range(attempts):
    num = int(input("Введите число: "))
    if random_number == num:
        print("Правильно!")
        break
    elif random_number < num:
        print("Задуманное число меньше")
    elif random_number > num:
        print("Задуманное число больше")
else:
	print("Число не угадано после 5 попыток")

# второй вариант
# from random import randint
#
# random_number = randint(1, 9)
# print(random_number)
# correct_num = False
# attempts = 5
# for attempt in range(attempts):
#     num = int(input("Введите число: "))
#     if random_number == num:
#         print("Правильно!")
#         correct_num = True
#         break
#     elif random_number < num:
#         print("Задуманное число меньше")
#     elif random_number > num:
#         print("Задуманное число больше")
# if not correct_num:
# 	print("Число не угадано после 5 попыток")
