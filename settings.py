
# NÃO PODEM MUDAR
number_of_computers = 2
number_of_years = 3

# PODEM MUDAR
computer_id = 1
mini_batch = 1

meses = [
  "janeiro", "fevereiro"
]

anos_modelo = [
  2015, 2016, 2017, 2018, 2019, 2020
]

structure_columns = ['Marca', 'Modelo', 'Ano-modelo']
for index in range(number_of_years * len(meses)):
  structure_columns.append(f'Mes {index + 1}')