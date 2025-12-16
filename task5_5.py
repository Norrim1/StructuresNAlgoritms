import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator


fig, ax = plt.subplots()
ax.set( xlabel='Languages',
    ylabel='Popularity',
    title='Popularity of Programming Language Worldwide, Oct17 Compared to a year ago',
    ylim=(0, 25),
)
ax.minorticks_on()
ax.xaxis.set_minor_locator(AutoMinorLocator(4))
plt.grid()
ax.xaxis.grid(which='minor')
ax.yaxis.grid(which='minor')
ax.xaxis.grid(which='major', color='r')
ax.yaxis.grid(which='major', color='r')
colors = ['red', 'black', 'green', 'blue', 'yellow', 'cyan']

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
widths = [0.1, 0.2, 0.5, 1.1, 0.2, 0.3]
bars = plt.bar(languages, popularity, width=widths) 
plt.show()