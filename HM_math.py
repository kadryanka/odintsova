import random

# import numpy as np
#
# np.random.uniform()
# bonus = 0
# while True:
#     bonus = input("введите ставку:")
#     try:
#
#         bonus = int(bonus)
#         if bonus > 36:
#             print("не более 36 или 0")
#             break
#         bonus_1 = round(np.random.uniform(0,36))
#         if bonus == bonus_1:
#             print(bonus_1,"поздравляем ,Вы выиграли")
#         else:
#             print(bonus_1,"вы проиграли")
#     except ValueError:
#         if bonus == "красное" or bonus == "черное":
#             bonus_2 = round(np.random.uniform(0, 36))
#             if bonus_2 %2!=0 and bonus == "черное":
#                     print(bonus_2,"черное!!вы выиграли!!!")
#             elif bonus_2%2== 0 and bonus =="красное" and bonus_2!=0:
#                 print(bonus_2,"красное , Вы выиграли")
#             else:
#                 print(bonus_2,"Вы проиграли")
#         else:
#             print("неверный ввод")
#             break
# 2
# Вероятность выпадения красного
Pn_red = 18/37
# Вероятность черного
Pn_black = 18/37
# Вероятность зеро
Pn_0 = 1/37
#Вероятность выпадения любого числа
P = Pn_red+Pn_black+Pn_0
print (P)

#3
import random
import matplotlib. pyplot as plt
x=[]
for i in range (0,9):
    x.append(sum(random.sample(range(100), 10)))
print(x)
plt.hist(x, bins='auto')
plt.show()

#4
import random
import matplotlib.pyplot as plt
import numpy as np
import math
for n in range (70, 130, 15):
    print()
    k, m = 0, 0
    for i in range(0, n):
        x = np.random.uniform(0, 10)
        if x<5:
            k = k + 1
        else:
            m = m + 1
    print (f'Количество выпадания орлов {k} и {m} решек при {n} попыток')
p =0.5 #успех
q = (1-p)
for n in range (70, 130, 15):
    print()
    for k in range (35, 60, 5):
        P=(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))*(p**k)*(q**(n-k))*100
        print (f'Вероятность выпадения {k} орлов при {n} попыток - {P:.5f} %')

#5
X=[]
Y=[]
for n in range (75, 115):
    x, y = 0, 0
    for i in range(0, 30):
        k = np.random.uniform(0, 10)
        if k<5:
            x += 1
        else:
            y += 1
    X.append(x)
    Y.append(y)
print('\n',X,Y)
plt.hist(X, bins='auto')
plt.show()
#R = np.corrcoef (X,Y)
#print('\n', f'Kоэффициент корреляции равен {R}')
for i in range (1, len(X)):
    R1 = np.sum((X[i]-X[i-1])*(Y[i]-Y[i-1]))/np.sqrt((np.sum(X[i]-X[i-1])**2)*np.sum((Y[i]-Y[i-1])**2))
    print('\n',f'Kоэффициент корреляции равен {R1}')