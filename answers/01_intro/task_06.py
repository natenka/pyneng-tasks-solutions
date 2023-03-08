

from pprint import pprint

number_as_str = input("Enter a number greater than 10: ")
number = int(number_as_str)
pprint(number_as_str)
pprint(number)

if number <= 10:
    print("wrong")
else:
    print("correct")
