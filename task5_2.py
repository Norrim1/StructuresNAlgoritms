import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator


fig, ax = plt.subplots()
ax.set( xlabel='Languages',
    ylabel='Popularity',
    title='PopularitY of Programming Language Worldwide, Oct17 Compared to a year ago',
    ylim=(0, 25),
)
plt.grid()
ax.xaxis.grid(which='minor')
ax.yaxis.grid(which='minor')
ax.xaxis.grid(which='major', color='r')
ax.yaxis.grid(which='major', color='r')

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.barh(languages, popularity, color='green')
plt.show()
