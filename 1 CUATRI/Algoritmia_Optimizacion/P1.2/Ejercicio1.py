# Representa las siguientes funciones con Matplotlib:
import matplotlib.pyplot as plt
import math
import numpy as np

x = np.linspace(1, 5, 100)

y1 = np.sqrt(x)

#y2 = 10**x

y3 = x**1.5

y4 = 2*np.sqrt(np.log2(x))

y5 = x**2 * np.log2(x)

y6 = 2**x

y7 = x**(np.log2(x))

y8 = x**2

y9 = 2**np.log2(x)

y10 = 2**(2**np.log2(x))

y11 = x**(5/2)

y12 = x**2 * np.log2(x)

fig = plt.figure(figsize=(15,15))
ax = plt.axes()

ax.plot(x, y1, color='r')
#ax.plot(x, y2, color='g')
ax.plot(x, y3, color='b')
ax.plot(x, y4, color='orange')
ax.plot(x, y5, color='yellow')
ax.plot(x, y6, color='purple')
ax.plot(x, y7, color='pink')
ax.plot(x, y8, color='cyan')
ax.plot(x, y9, color='brown')
ax.plot(x, y10, color='black')
ax.plot(x, y11, color='darkblue')
ax.plot(x, y12, color='grey')


plt.show()