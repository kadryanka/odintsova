# lesson 2
# 1)
a = ["dog", 43, 34.8]
for word in a:
    print(type(word))

# 2)
li = input("введите несколько слов: ").split()
for i in range(0, len(li) - 1, 2):
    li[i], li[i - 1] = li[i - 1], li[i]
print(li)
# 3)
d = {"зима": [12, 1, 2], "весна": [3, 4, 5], "лето": [6, 7, 8], "осень": [9, 10, 11]}
m = int(input("введите номер: "))
for el in d:
    if m in d[el]:
        break
print(m)
# второй вариант
m = int(input("введите номер месяца: "))
if (m == 12) or (m <= 2):
    print("зима")
elif (m == 3) or (m <= 5):
    print("весна")
elif (m == 6) or (m <= 8):
    print("лето")
elif (m == 9) or (m <= 11):
    print("осень")
if m < 1 or m > 12:
    print("погугли сколько месяцев в году")

# 4
word = input("введите слова:").split()
for i, el in enumerate(word, 1):
    print(i, el[0:10])
# 5
li = [7, 5, 3, 3, 2]
n = int(input("enter new score: "))
i = 0
for el in li:
    if n <= el:
        i += 1
li.insert(i, n)
print(li)



