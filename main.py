import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

dates_ = ['2016-10-03', '2016-10-04', '2016-10-05', '2016-10-06', '2016-10-07']
values_ = [772.5, 776.4, 776.5, 776.8, 775.1]
fig, ax = plt.subplots()
ax.plot(dates_, values_)
plt.xlabel("Dates")
plt.ylabel("Closing Value")
plt.title("Closing stock value of Alphabet Inc.")
plt.minorticks_on()
plt.grid(axis='x')
plt.grid(axis='y')
plt.show()