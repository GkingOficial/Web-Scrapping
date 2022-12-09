
# NÃO PODEM MUDAR
number_of_computers = 2
number_of_years = 3

# PODEM MUDAR
computer_id = 0
mini_batch = 6

meses = [
  "janeiro", "fevereiro"
]

anos_modelo = [
  2015
]

structure_columns = ['Marca', 'Modelo', 'Ano-modelo']
for index in range(number_of_years * len(meses)):
  structure_columns.append(f'Mes {index + 1}')