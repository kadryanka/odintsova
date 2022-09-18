# 1
from sys import argv
print(f'all_time= {argv[1]},in_our = {argv[2]} , prize = {argv[3]}')
print(int(argv[1]) * int(argv[2]) + int(argv[3]))

# 2
li_1 = [30,10,50,37,4,6]
li_2 = [li_1[i] for i in range(1,len(li_1)) if li_1[i] > li_1[i] - 1]
print(li_2)

# 3
li = [el for el in range(20,241)if el % 20 == 0]
print(li)

# 4
li = [4,4,5,7,2,9,5]
new = [el for el in li if li.count(el) == 1]
print(new)
 #5
from functools import reduce
new = [i for i in range(100,1001,2)]
print(f'score: {reduce((lambda x,y:x*y),new)}')

# 6
from itertools import count,cycle
l = int(input("введите начало:"))
li = int(input("введите предел:"))
for i in count(l):
    print(i)
    if i == li:
        break


# 6/2
sp = (input("введите список:")).split()
for el in cycle(sp):
    stop = input("для выхода введите стоп:")
    if stop.title() == "стоп":
        break
    print(el)

# 7
def fact(n):
    rez = 1
    if n == 0:
        yield f'{n}! = 1'
    for i in range(1,n + 1):
        rez *= i
        yield f'{n}! = {rez}'
n = int(input('введите значение:'))
for el in fact(n):
    print(el)





