import matplotlib.pyplot as plt

x1 = [2, 3, 5, 6, 8]
y1 = [1, 5, 10, 18, 20]
x2 = [3, 4, 6, 7, 9]
y2 = [2, 6, 12, 20, 23]

plt.plot(x1, y1, lw = 5, linestyle='none', marker='o')
plt.plot(x2, y2, lw = 3, linestyle='none', marker='o')
plt.show()