#1
#with open("HW_2.txt.txt","w",encoding="utf-8")as f:
#     line = " "
#     while line != "":
#         line = input()
#         print(line,file=f)
#2
# with open("HW_1.txt","r",encoding="utf-8")as f:
#     txt = f.readlines()
#     for el, line in enumerate(txt,1):
#         word = len(line.split())
#         print(f"в {el} строке {word} слов")

# 3
# oll_bonus = 0
# oll_workers = 0
# with open("HW_3.txt","r",encoding="utf-8") as f:
#     for line in f:
#         oll_bonus += float(line.split()[1])
#         oll_workers = oll_workers + 1
#         if float(line.split()[1])< 20000:
#                 print((line.split()[0]))
# print("средняя заработная плата :",round(oll_bonus/oll_workers,2))
#
# # 4

my_f = {"One":"Один","Two":"Два","Three":"Три","Four":"Четыре"}

with open("HW_d.txt","w",encoding="utf-8") as f_write:
    with open("HW_4.txt", "r", encoding="utf-8") as f_read:
        for line in f_read:
             f_write.writelines([line.replace(line.split()[0], my_f[line.split()[0]])])

# 5
from random import randint
with open("HW_5.txt","w",encoding="utf-8") as f:
    li = [randint(1,20)]
    for el in range(50):
        f.write(" ".join(map(str,li)))
print("сумма:",sum(li))
# 6
with open("HW_6.txt","r",encoding="utf-8") as f:
    info = f.readlines()
    for line in info:
        new_line = ""
        for el in line:
                new_line = "".join([new_line,(el if el in "0123456789"else" ")])
        new_info = [int(i)for i in new_line.split()]
        print(f"{line.split()[0]}-{sum(new_info)}")
























