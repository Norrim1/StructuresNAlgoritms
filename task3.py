import matplotlib.pyplot as plt
import numpy
from matplotlib.ticker import AutoMinorLocator, FormatStrFormatter

fig, ax = plt.subplots()

x = numpy.linspace(0, 10, 100)
y = x*x-x-6

plt.plot(x, y)
ax.minorticks_on()
ax.xaxis.set_minor_locator(AutoMinorLocator(2))
ax.xaxis.set_minor_formatter(FormatStrFormatter('%.2f'))
plt.grid()
ax.xaxis.grid(which='minor')
plt.legend()
plt.show()