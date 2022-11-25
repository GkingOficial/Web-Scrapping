class Teste:
  def __init__(self, list_numbers=[1, 2, 3]):
    self.list_numbers = list_numbers

  def print_list_numbers(self):
    print(self.list_numbers)

Teste([10, 20, 30]).print_list_numbers()
Teste().print_list_numbers()