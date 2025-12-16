import pandas as pd

s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s['a'])
print(s.iloc[1])
s['f'] = 6
print(s['f'])
print(s.iloc[2:5:1])
df = pd.DataFrame([[1, 2], [5, 3], [3.7, 4.8]], columns=['col1', 'col2'])
print(df.iloc[2, 0])
df.at[1, 'col2'] = 9
print(df.loc[1:2])
df['col3'] = df['col1'] * df['col2']
print(df)