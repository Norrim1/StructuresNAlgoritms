import matplotlib.pyplot as plt

colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown']
explode = (0.3, 0, 0, 0, 0, 0.3)
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [31.3, 24.8, 12.4, 11.3, 10.8, 9.4]
parts, texts, smth = plt.pie(popularity, labels=languages, colors=colors, autopct='%1.1f%%', explode=explode, shadow=True, startangle=13)
for part in parts:
    part.set_edgecolor('black')
    
plt.title('PopularitY of Programming Language Worldwide, Oct17 Compared to a year ago')
plt.show()
