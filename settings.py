
verbose = True
headless = False

# NÃO PODEM MUDAR
number_of_computers = 2
number_of_years = 2

# PODEM MUDAR

# Começa em 0
computer_id = 0
mini_batch = 2

meses = [
  "janeiro", "fevereiro"
]

anos_modelo = [
  2020,
  2021
]

structure_columns = ['Marca', 'Modelo', 'Ano-modelo']
for index in range(number_of_years * len(meses)):
  structure_columns.append(f'Mes {index + 1}')