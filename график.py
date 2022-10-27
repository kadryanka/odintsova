import math

try:
   x = int(input(f"введите координату X:"))

   y = int(input(f"введите координату y:"))
   z = int(input(f"введите координату z:"))
   print(f"vect ({x},{y},{z})")
   vect = np.sqrt(x*x + y*y + z*z)
   print(round(vect,2))
except ValueError:
   print("error:enter only namber!!!!!")

import numpy as np
import matplotlib.pyplot as plt
import numpy as np


def elips(a,b,x_1 = 0,y_1 = 0):
   x = []
   y = []
   for el in np.linspace(0,360,361):
      x.append(a * math.cos((np.pi * el)/ 180) + x_1)
      y.append(b * math.sin((np.pi * el)/ 180) + y_1)


   plt.plot(x,y)
   plt.plot(x_1,y_1,marker = "o")
   plt.xlim(-20,20)
   plt.ylim(-20,20)

   plt.show()
elips(15,15,-2,2)

def giperbola (a,b,x_0,y_o):
   x_1 = []
   x_2 = []
   y = []
   for el in np.linspace(-2,2,100):
      x_1.append((a*math.cosh(el)+x_0))
      x_2.append(-a*math.cosh(el)+x_0)
      y.append(b*math.sinh(el)+y_o)
   plt.plot (x_1,y)
   plt.plot(x_2,y)
   plt.plot(x_0,y_o,marker = 'o')
   plt.show()
giperbola(3,5,-5,5)

x = np.linspace( -1 , 1 , 150 )
y = np.linspace( -1 , 1 , 150 )
a, b = np.meshgrid(x, y)

C = a ** 2 + b ** 2 - 0.5

figure, axes = plt.subplots()

axes.contour(a, b, C, [0])
axes.set_aspect(1)
plt.title('окружность по центру и радиусу')
plt.show()

fig = plt.figure()


f = lambda x, y: 30*x + y
f2 = lambda x,y: 30 * x + y - 100

fig = plt.figure(figsize = (10, 10))

ax = fig.add_subplot(1, 1, 1, projection = '3d')

xval = np.arange(-5,5,1)
yval = np.arange(-5, 5, 0.5)

x, y = np.meshgrid(xval, yval)

z = f(x, y)
z2 = f2(x,y)

surf = ax.plot_surface(x, y, z,rstride = 10,cstride = 10,cmap = cm.plasma)
surf1 = ax.plot_surface(x, y, z2,rstride = 10,cstride = 10,cmap = cm.plasma)
plt.show()


f = lambda x, y: x ** 2 + y ** 2 - 0.5
f2 = lambda x,y: 3 * x**2 - y**2 + 10

fig = plt.figure(figsize = (10, 10))

ax = fig.add_subplot(1, 1, 1, projection = '3d')

xval = np.arange(-5,5,1)
yval = np.arange(-5, 5, 0.5)

x, y = np.meshgrid(xval, yval)

z = f(x, y)
z2 = f2(x,y)

surf2 = ax.plot_surface(x, y, z,rstride = 10,cstride = 10,cmap = cm.plasma)
surf3 = ax.plot_surface(x, y, z2,rstride = 10,cstride = 10,cmap = cm.viridis)
plt.show()


def my_func(k, a, b):
   x = np.linspace(-2 * np.pi, 2 * np.pi, 301)
   y = k * np.cos(x - a) + b
   plt.plot(x, y)
plt.grid(True)
my_func(3, 0, 0)
my_func(1, 0, 0)
my_func(3, 0, -5)
plt.show()


def pol_to_dec(r, a):
   return (r * np.cos((np.pi * a) / 180), r * math.sin((np.pi * a) / 180))

print(pol_to_dec(1, 90))


def dec_to_pol(x, y):
   rho = np.sqrt(x ** 2 + y ** 2)
   phi = (np.arctan2(y, x) * 180) / np.pi
   return (rho, phi)

print(dec_to_pol(0, 1))

x = np.linspace(0, 2*np.pi, 100)
r = np.linspace(10,10,100)
plt.polar(x, r)
plt.show()


from scipy.optimize import fsolve
r = [2,2]
a = [1*np.pi, 2*np.pi]

plt.polar(a, r)
plt.show()

#y = x2 – 1
#exp(x) + x∙(1 – y) = 1

#выразим y
# exp(x) + x∙(1 – y) = 1
# exp(x) + x - x*y - 1 = 0
# exp(x) + x - 1 = x*y
# y = (exp(x) + x - 1) / x

x = np.linspace(-2,3,201)
plt.plot(x, (np.exp(x) + x - 1) / x)
plt.plot(x, x**2 - 1)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()


def equations(p):
   x, y = p
   return (y - x ** 2 + 1, np.exp(x) + x - x * y - 1)


x1, y1 = fsolve(equations, (-1, 1))
x2, y2 = fsolve(equations, (2, 6))

print(x1, y1)
print(x2, y2)


#y = x2 – 1
#exp(x) + x∙(1 – y) -1> 0


def equations2(p):
   x, y = p
   return (y - x ** 2 + 1, np.exp(x) + x - x * y > 1)


x1, y1 = fsolve(equations2, (-1, 1))
x2, y2 = fsolve(equations2, (2, 6))

print(x1, y1)
print(x2, y2)


def equations2(p):
   x, y = p
   return (y - x ** 2 + 1, np.exp(x) + x - x * y > 1)


x1, y1 = fsolve(equations2, (-1, 1))
x2, y2 = fsolve(equations2, (2, 6))

print(x1, y1)
print(x2, y2)


















