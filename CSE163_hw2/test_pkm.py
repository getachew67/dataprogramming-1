import pandas as pd

df = pd.read_csv('pokemon_test2.csv')

print(df.groupby('name')['level'].max().max())
print(df.groupby('name')['level'].max().idxmax())

print(df['level'].max())
print(df['level'].idxmax())
print(df.loc[df['level'].idxmax(), 'name'])
