from matplotlib import pyplot as plt
import pandas as pd


df = pd.read_csv('la-crimes-sample.csv')

print("")

print(len(df))
print(len(df.columns))

print("")

print(df.columns)
print(df.dtypes)

print("")

for column in df.columns:
    temp = df[column]
    print(temp.nunique())

print("")

for col_index in range(len(df.columns)):
    print(df.iloc[:, col_index].isna().sum())

print("")

x = df['Victim Sex']
male_crime_victims = len(df[df['Victim Sex'] == 'M'])
female_crime_victims = len(df[df['Victim Sex'] == 'F'])
if female_crime_victims > male_crime_victims:
    print(True)
else: 
    print(False)
print(male_crime_victims, female_crime_victims)

print("")

crimes = df['Crime Code Description'].value_counts().head(10)
crimes.plot(kind='bar')
plt.show()

print("")

print('Male')
filtered_male = df[df['Victim Sex'] == 'M']
print(filtered_male['Crime Code Description'].value_counts().head(5))

print("")

print('Female')
filtered_female = df[df['Victim Sex'] == 'F']
print(filtered_female['Crime Code Description'].value_counts().head(5))

print("")

print(df['Victim Descent'].value_counts().head(1))
print("")

area_counts = df['Area Name'].value_counts()
area_counts.plot(kind='bar')
plt.show()