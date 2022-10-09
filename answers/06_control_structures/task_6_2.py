# -*- coding: utf-8 -*-


line = "Guido van Rossum began working on Python in the late 1980s"
result = ""
for letter in line:
    if letter in "aeiouyj":
        result += letter.upper()
    else:
        result += letter

print(result)

