
# import numpy as np
# import matplotlib.pyplot as plt
#
# k = 1
# k_1 = 2.5
#
# y = lambda x,a:np.cos(a*x)
#
#
# figure = plt.subplots()
#
# x = np.linspace(-10,5,150)
#
# plt.plot(x,y(x,k_1))
# plt.plot(x,y(x,k))
# plt.show()

import numpy as np

try:
   x = int(input(f"введите координату X:"))

   y = int(input(f"введите координату y:"))
   z = int(input(f"введите координату z:"))
   print(f"vect ({x},{y},{z})")
   vect = np.sqrt(x*x + y*y + z*z)
   print(round(vect,2))
except ValueError:
   print("error:enter only namber!!!!!")























