
verbose = False

# NÃO PODEM MUDAR
number_of_computers = 2
number_of_years = 3

# PODEM MUDAR
computer_id = 1
mini_batch = 5

meses = [
  "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

anos_modelo = [
  2020
]

structure_columns = ['Marca', 'Modelo', 'Ano-modelo']
for index in range(number_of_years * len(meses)):
  structure_columns.append(f'Mes {index + 1}')