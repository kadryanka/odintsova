def div():
    try:
        a = int(input('введите делимое:'))
        b = int(input("введите делитель:"))
        print(a/b)
        return (a / b)
    except ZeroDivisionError:
        return "деление на ноль невозможно"
    except ValueError:
        return 'only number'
print(div())
div()
# № 2
def info(name,surname,birthday,sity,email,tel):
    return f'{name},surname:{surname},birthday:{birthday},sity:{sity},email:{email},tel:{tel}'

print(info(name = input("Name:"),surname = input("Surname:"),birthday=input("Birthday:"),sity=input("Sity:"),email=input("Email:"),tel=input("Tel:")))

#№ 3
def my_func(a,b,c):
    li = [a, b, c]
    try:
        li.remove(min(li))
        return sum(li)
    except ValueError:
        return 'only number'
print(my_func(4,25,9))

# № 4
def my_func(x,y):
    try:
        rez = x ** y
        return rez
    except ValueError:
        return 'only number'
print(my_func(7,-9))
#№ 4.2
def my_func(x,y):
    try:
        x,y = float(x),int(y)
        rez = 1
        for i in range(abs(y)):
            rez /= x
        return round(rez,5)
    except ValueError:
        return 'only number'
num_1 = input("x:")
num_2 = input("y:")
print(my_func(num_1,num_2))
# № 5
def sum():
    rez = 0
    while True :
        li = input("введите числа.для выхода - @:")
        for num in li:
            if num == " @ ":
                return rez
            else:
                try:
                    rez = rez + int(num)
                except  ValueError:
                    return "для выхода введите @"
                print("сумма = :",rez)
sum()
# № 6
def int_func():
   li = input("введите слова через пробел:").split()
   for word in li:
    n = 0
    for ch in word:
        if 97 <= ord(ch) <= 122:
         n+=1
        if n == len(word):
                print(word.title())
        else:
            print("error")
int_func()








































