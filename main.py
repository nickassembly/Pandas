import pandas as pd

df = pd.read_csv('./data/pokemon_data.csv')
# print(df.head(3)) # just see top 3 rows

# read excel
# df_xlsx = pd.read_excel('./data/pokemon_data.xlsx')
# print(df_xlsx.head(3))

# read text / needs delimiter
# df = pd.read_csv('./data/pokemon_data.txt', delimiter='\t')
# print(df.head(3))

## Read Headers
#print(df.columns)

## Read each column
#print(df[['Name', 'Type 1', 'HP']])

## Read each row
#print(df.iloc[0:4])

## Read a specific location (R,C)
#print(df.iloc[2,1])

# for index, row in df.iterrows():
#     print(index, row['Name'])

# df.loc[df['Type 1'] == "Fire"]
# print(df.describe())

# print(df.sort_values(['Type 1', 'HP'], ascending=[1, 0]))

#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

# df['Total'] = df.iloc[:, 4:10].sum(axis=1)

# cols = list(df.columns.values)
# df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

# #print(df.head(5))

# df.to_csv('modified.csv', index=False)

# Filtering Data
# new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
# new_df = new_df.reset_index(drop=True)
# print(new_df)

#print(df.loc[~df['Name'].str.contains('Mega')]) # ~ is equal to ! or NOT

# regex
# import re

# print(df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)])

#df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
#print(df)

# df = pd.read_csv('modified.csv')
# print(df)

# print(df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False))
# print(df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False))

# df['count'] = 1

# print(df.groupby(['Type 1', 'Type 2']).count()['count'])





