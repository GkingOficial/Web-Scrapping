
verbose = True
headless = False

# NÃO PODEM MUDAR
number_of_computers = 5
number_of_years = 1

# PODEM MUDAR

# Começa em 0
computer_id = 0
mini_batch = 8

meses = [
  "janeiro", "fevereiro", "março", "abril", "maio", "junho",
  "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

anos_modelo = [
  2015, 2016, 2017, 2018, 2019, 2020
]

structure_columns = ['Marca', 'Modelo', 'Ano-modelo']
for index in range(number_of_years * len(meses)):
  structure_columns.append(f'Mes {index + 1}')