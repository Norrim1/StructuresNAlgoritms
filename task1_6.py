import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, FormatStrFormatter


fig, ax = plt.subplots()
plt.grid()
ax.minorticks_on()
ax.xaxis.grid(which='minor')
ax.yaxis.grid(which='minor')
ax.xaxis.grid(which='major', color='r')
ax.yaxis.grid(which='major', color='r')
ax.yaxis.set_minor_locator(AutoMinorLocator(4))
ax.yaxis.set_minor_formatter(FormatStrFormatter('%.2f'))

dates_ = ['2016-10-03', '2016-10-04', '2016-10-05', '2016-10-06', '2016-10-07']
values_ = [772.5, 776.4, 776.5, 776.8, 775.1]
plt.xlabel("Dates")
plt.ylabel("Closing Value")
plt.title("Closing stock value of Alphabet Inc.")
plt.plot(dates_, values_)
plt.show()