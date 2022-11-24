import pandas as pd

with open('ideias/vehicles_with_price2.json', encoding='utf-8') as inputfile:
  df = pd.read_json(inputfile)

df.to_csv('csvfile.csv', encoding='utf-8', index=False)