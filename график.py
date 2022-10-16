
import numpy as np
import matplotlib.pyplot as plt

k = 1
k_1 = 2.5

y = lambda x,a:np.cos(a*x)

figure = plt.subplots()

x = np.linspace(-10,5,150)

plt.plot(x,y(x,k_1))
plt.plot(x,y(x,k))
plt.show()