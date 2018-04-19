import matplotlib.pyplot as plt

x = ["1", "2", "3", "4", "5", "6"]
y = [86,70,90,80,77,100]

plt.bar(x,y)
plt.xlabel("Level")
plt.ylabel("Score")
plt.title("Matplotlib Bar by Kucing Item Putih")
plt.legend()
plt.show()
