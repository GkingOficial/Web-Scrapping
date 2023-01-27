import pandas

data = pandas.read_csv('./data.csv', encoding = 'utf-8', delimiter = ',')

data = data.drop_duplicates()
data.fillna(value = "NULL", axis = 1, inplace = True)

data.to_csv("data.csv", index = False, header = True)
