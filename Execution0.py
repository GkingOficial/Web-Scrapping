from MongoDBWeb import MongoDBWeb
from settings import number_of_computers, computer_id

bd = MongoDBWeb()
indices_de_busca = bd.get_indexes(computer_id)
print(indices_de_busca)