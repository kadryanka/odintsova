height = 170
weight = 70  #
index = height // weight  # индекс массы тела#
print(index)
height = int(input("enter height:"))
weight = int(input("enter weight:"))
print(height, weight, index)  #
# № 2
time_sec = int(input("enter time:"))
hour = time_sec // 3600
min = time_sec % 3600 // 60
sec = time_sec % 3600 % 60
print(f"{hour:02}:{min:02}:{sec:02}")

# № 3
n = input("enter number: ")
print(int(n) + int(n + n) + int(n + n + n))
# № 4
a = int(input("enter number: "))  # 67588
max = 0
while a > 0:
    surplas = a % 10
    if surplas > max:
        max = surplas
    a //= 10
    break
print("Максимальная цифра:", max)

# №4
profit = int(input("enter прибыль:"))
cost = int(input("enter издержки:"))
ind = profit - cost
if ind < 0:
    print("bad")
if ind > 0:
    print("cool!!")
    rent = profit / cost
    work_man = int(input("enter количество рабоников: "))
    profit_each_work = rent / work_man
    print("прибыль из расчета на одного сотрудника", profit_each_work)

# № 5
a = int(input("enter distance:"))
b = int(input("enter right distance"))
day = 1
while a < b:
    a *= 1.1
    day += 1
print(f"на {day}-й день спортсмен пробежал {b}км")