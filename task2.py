import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt


df = pd.read_csv('howpop_train.csv', decimal=",")

df.drop(
    filter(lambda c: c.endswith("_lognorm") or c.startswith("Unnamed"), df.columns),
    axis=1,
    inplace=True,
) 

df["published"] = pd.to_datetime(df.published, yearfirst=True)
df["year"] = [d.year for d in df.published]
df["month"] = [d.month for d in df.published]
df["dayofweek"] = [d.isoweekday() for d in df.published]
df["hour"] = [d.hour for d in df.published]

yearm = df.groupby(['year', 'month']).size().reset_index(name='count')
yearm['label'] = yearm['year'].astype(str) + ', ' + yearm['month'].astype(str)
yearm = yearm.sort_values(['year', 'month']).reset_index(drop=True)

dayofw = df.groupby('dayofweek').size().reset_index(name='count')
dayofw['day'] = dayofw['dayofweek'].astype(str)

mostwatchedh = df.groupby('hour', as_index=False)['views'].mean()
mostcommentedh = df.groupby('hour', as_index=False)['comments'].mean()

print(mostwatchedh)

sb.set_theme()
sb.lineplot(data=yearm, x='label', y='count')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

sb.set_theme()
sb.barplot(data=dayofw, x='day', y='count', hue='day')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

sb.set_theme()
sb.lineplot(data=mostwatchedh, x='hour', y='views')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
"""Больше всего просмотров набирают статьи, опубликованные в 12 часов дня = false
Больше всего просмотров набирают статьи, опубликованные в 6 часов утра = true"""

sb.set_theme()
sb.lineplot(data=mostcommentedh, x='hour', y='comments')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
"""У опубликованных в 10 утра постов больше всего комментариев = false"""
"""На хабре дневные статьи комментируют чаще, чем вечерние = false"""

authors = df.groupby('author')['votes_minus'].sum().nlargest(20).reset_index(name='count')
authors['author_name'] = authors['author'].astype(str)
sb.set_theme()
sb.lineplot(data=authors, x='author_name', y='count')
plt.show()
