import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, FormatStrFormatter
import numpy

x = numpy.linspace(0, 4, 50)
y1 = numpy.cos(x)
y2 = numpy.sin(x)
x_scatter = numpy.random.rand(30) * 4
y_scatter = numpy.random.rand(30) * 2
fig, ax = plt.subplots()

ax.plot(x, y1, color="blue", label="Синяя линия")
ax.plot(x, y2, color="red", label="Красная линия")
ax.scatter(x_scatter, y_scatter)
ax.grid(True)
ax.set( xlabel="Подпись оси OX",
    ylabel="Подпись оси OY",
    title="Элементы изображения",
)
plt.grid()
ax.minorticks_on()
ax.xaxis.grid(which='major')
ax.yaxis.grid(which='major')
ax.yaxis.set_minor_locator(AutoMinorLocator(4))
ax.yaxis.set_minor_formatter(FormatStrFormatter('%.2f'))

plt.legend()
plt.show()
