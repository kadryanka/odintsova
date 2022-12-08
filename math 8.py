import numpy as np
import matplotlib.pyplot as plt

#1. Решите линейную систему:

A = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
B = np.array([12, 2, 1])
X = np.linalg.solve(A, B)
print(f'Ответ: Х1 = {X[0]}, X2 = {X[1]}, X3 = {X[2]}')

# Ответ: Х1 = -9.200000000000001, X2 = 0.9000000000000006, X3 = 6.466666666666666

# 2. Найдите псевдорешение:
# x + 2y – z = 1
# 3x – 4y = 7
# 8x – 5y + 2z = 12
# 2x – 5z = 7
# 11x +4y – 7z = 15

A = np.array([[1, 2, -1],
              [3, -4, 0],
              [8, -5, 2],
              [2, 0, -5],
              [11, 4, -7]])
B = np.array([1, 7, 12, 7, 15])
X = np.linalg.lstsq(A, B)
print(f'Ответ: x = {X[0][0]}, y = {X[0][1]}, z = {X[0][2]}')
#Ответ: x = 1.139193526466007, y = -0.9049844399605506, z = -0.9009802999097409

import numpy as np

# 3. Сколько решений имеет линейная система:
#
#
# Если ноль – то измените вектор правой части так, чтобы система стала совместной, и решите ее.

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
BT = np.array([[3], [2], [1]])
B = np.array([3, 2, 1])

print(f'Ранг A {np.linalg.matrix_rank(A, 0.0001)}')
C = np.concatenate((A,BT), axis=1)
print(f'Ранг C {np.linalg.matrix_rank(C, 0.0001)}')

import matplotlib.pyplot as plt
import scipy
import scipy.linalg

# 4. Вычислите LU-разложение матрицы:
#
# После этого придумайте вектор правых частей и решите полученную линейную систему трех уравнений с данной матрицей.


A = np.array([[1, 2, 3], [2, 16, 21], [4, 28, 73]])
B = np.array([1, 2, 4])
P, L, U = scipy.linalg.lu(A)

print(P)
print(L)
print(U)

import scipy
import scipy.linalg
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

# 5. Найдите нормальное псевдорешение недоопределенной системы:
# x + 2y – z = 1
# 8x – 5y + 2z = 12
def Q(x, y, z):
    return np.sqrt(x**2 + y**2 + z**2)

fig2 = figure()
ax = Axes3D(fig2)
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)

ax.plot_surface(X, Y, Q(X, Y, X + 2*Y - 1))
ax.plot_surface(X, Y, Q(X, Y, 12 - 8*X+5*Y))
ax.scatter(0,0,0,'z',50,'red')
show()

A = np.array([[1, 2, -1], [8, -5, 2]])
B = np.array([1, 12])

print(f'Ответ: {np.linalg.lstsq(A,B, rcond=-1)}')
#Ответ: (array([ 1.38191882, -0.18081181,  0.0202952 ]), array([], dtype=float64), 2, array([9.65316119, 2.41173777]))

print(f'det A = {np.linalg.det(A)}')
print(f'Ответ: {np.linalg.solve(A,B)}')

# det A = 432.00000000000017
# Ответ: [ 1. -0. -0.]

print(f'Ответ: {np.linalg.solve(A,B)}')
#Ответ: [-9.66666667 15.33333333 -6.        ]

# 6. Найдите одно из псевдорешений вырожденной системы:

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([2, 5, 11])

Q, R = np.linalg.qr(A)

print(A)
print(Q)
print(R)

R1 = R[:2, :2]
B1 = np.dot(np.transpose(Q), B)[:2]

X1 = np.linalg.solve(R1, B1)
print(X1)
X=np.append(X1, 0)
print(X) #[1.50000000e+00 3.92767275e-15 0.00000000e+00]
print(np.linalg.norm(X)) #1.499999999999996
print(np.linalg.norm(np.dot(A,X) - B)) #1.224744871391589

X = np.linalg.lstsq(A,B, rcond=-1)[0]
print(f'Ответ: {X}') #Ответ: [ 1.25  0.5  -0.25]

print(np.linalg.norm(X)) #1.3693063937629126
print(np.linalg.norm(np.dot(A,X) - B)) #1.2247448713915892