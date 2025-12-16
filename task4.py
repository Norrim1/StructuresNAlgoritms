from matplotlib import pyplot as plt
import numpy
import pandas as pd


polit = pd.read_csv('polit.csv', decimal=",")
polit = polit.drop(columns=["Unnamed: 13"])
polit = polit.dropna()

print(polit)

polit['fh09'] = pd.to_numeric(polit['fh09'])
fh_more_than_5 = polit[polit['fh09'] > 5]

print(fh_more_than_5)

afr_fparl = polit[(polit['afri'] == 1) & (polit['fparl08'] > 30)]
print(afr_fparl)

africa_latin_dem = polit[((polit['afri'] == 1) | (polit['lati'] == 1)) & (polit['polity09'] >= 8)]
print(africa_latin_dem)

polit['corr_round'] = polit["corr0509"].round(2)

nums = [0, 2.5, 5.0, 7.0]
labels = ["Free", "Partly Free", "Not Free"]
polit['fh_status'] = pd.cut(polit['fh09'], bins=nums, labels=labels, include_lowest=True)
print(polit)

ginn = polit.groupby('fh_status')['gini'].agg(['min', 'mean', 'max'])
print(ginn)

for fhstatus, group in polit.groupby('fh_status'):
    filename = f"{fhstatus}.csv"
    group.to_csv(filename)