
words = ["word1", "word2", "word3"]
index = int(input("Введіть індекс: "))
index_max = len(words) - 1
index_min = 0 - len(words)

# if index_min <= index <= index_max:
if index <= index_max and index >= index_min:
    print(words[index])
else:
    print("У списку words немає такого індексу")
