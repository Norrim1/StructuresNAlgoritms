from matplotlib import pyplot as plt
import numpy
import pandas as pd

data = [["Вжик", "Zipper the Fly", "fly", "0.7"],
["Гайка", "Gadget Hackwrench", "mouse", None],
["Дейл", "Dale", "chipmunk", "1"],
["Рокфор", "Monterey Jack", "mouse", "0.8"],
["Чип", "Chip", "chipmunk", "0.2"]]

df = pd.DataFrame(data, columns=['ru_name', 'en_name', 'class', 'cheer'])
df['cheer'] = pd.to_numeric(df['cheer'])

print(df)
print(df.dtypes)
print(len(df))
print(df.iloc[:, 3].notna().sum())
print(df.iloc[2, 1])
df1 = df.iloc[1:4,0:3]

print(df1)
df['logcheer'] = numpy.log(df["cheer"])
print(df)
x = df['class']
y = x.value_counts()
x = x.unique()
print(x, y)
plt.bar(x, y)
plt.title('DataFrame class and their counts graph')
plt.xlabel('Unique class')
plt.ylabel('Counts') 
plt.show()