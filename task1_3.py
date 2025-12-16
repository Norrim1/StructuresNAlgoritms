import matplotlib.pyplot as plt

x = [10, 20, 30]
y1 = [40, 10, 30]
y2 = [20, 40, 10]

plt.plot(x, y1, lw = 5, label = "line2-width-5-dotted", linestyle='dotted')
plt.plot(x, y2, lw = 3, label = "line1-width-3-dashed", linestyle='dashed')
plt.legend()
plt.show()