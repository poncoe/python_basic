#Matplotlib LINE & DOT

import matplotlib.pyplot as plt

x = [1,2,4,5,7]
y = [1,3,5,4,6]

plt.plot(x,y, label="")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Belajar Matplotlib")
plt.legend()
plt.show()
