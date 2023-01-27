import pandas

data = pandas.read_csv('./data.csv', encoding = 'utf-8', delimiter = ',')

data2 = data.drop(["Marca", "Modelo", "Ano-modelo"], axis = 1, inplace = False)

cols_to_check = data2.columns
data2['is_na'] = data2[cols_to_check].isnull().apply(lambda x: all(x), axis = 1) 

print(f"Quantidade de linhas nulas: {data2['is_na'].sum()}")

list_data = list(data2['is_na'])

for index in range(len(list_data)):
  if(list_data[index]):
    data.drop(index, axis = 0, inplace = True)

data.fillna(value = "NaN", axis = 1, inplace = True)
data.to_csv("data2.csv", index = False, header = True)