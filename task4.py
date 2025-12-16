import matplotlib.pyplot as plt
import numpy
from matplotlib.ticker import AutoMinorLocator, FormatStrFormatter

x = numpy.linspace(0, 10, 100)
y = numpy.log(1+numpy.tan(1/(1+numpy.exp2(numpy.sin(x)))), (numpy.exp2(x)+1)*numpy.exp(-(numpy.abs(x)/(10))))

plt.plot(x, y)
plt.show()