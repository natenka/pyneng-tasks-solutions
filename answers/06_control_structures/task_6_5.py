# -*- coding: utf-8 -*-


from random import randint

random_number = randint(1, 9)
print(random_number)
attempts = 5
for attempt in range(attempts):
    num = int(input("Enter the number: "))
    if random_number == num:
        print("Correct!")
        break
    elif random_number < num:
        print("Your guess is too high")
    elif random_number > num:
        print("Your guess is too low")
else:
	print("Number not guessed after 5 tries")

# второй вариант
# from random import randint
#
# random_number = randint(1, 9)
# print(random_number)
# correct_num = False
# attempts = 5
# for attempt in range(attempts):
#     num = int(input("Enter the number: "))
#     if random_number == num:
#         print("Correct!")
#         correct_num = True
#         break
#     elif random_number < num:
#         print("Your guess is too high")
#     elif random_number > num:
#         print("Your guess is too low")
# if not correct_num:
# 	print("Number not guessed after 5 tries")
