import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()
men = [22, 30, 34, 30, 26]
women = [25, 32, 30, 35, 29]
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
x = np.arange(len(labels))
width = 0.4 
rects1 = ax.bar(x - width/2, men, width, label='Men', color='green')
rects2 = ax.bar(x + width/2, women, width, label='Women', color='red')
ax.set( xlabel='Scores',
    ylabel='Person',
    title='Scores by person',
)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()