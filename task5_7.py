import matplotlib.pyplot as plt

colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown']
explode = (0.3, 0, 0, 0, 0, 0,)
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [31.3, 24.8, 12.4, 11.3, 10.8, 9.4]
parts, texts, smth = plt.pie(popularity, labels=languages, colors=colors, autopct='%1.1f%%', explode=explode, shadow=True)
for part in parts:
    part.set_edgecolor('black')

plt.show()
