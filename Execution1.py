from MongoDBWeb import MongoDBWeb
import util
from settings import number_of_computers, computer_id

vehicles_to_search = util.read_json("json/vehicles_to_search.json")
length = len(vehicles_to_search)

bd = MongoDBWeb(
  vehicles_to_search_length=length,
  number_of_computers=number_of_computers
)
bd.delete_all()
bd.add_indexes()

# indices_de_busca = bd.get_indexes(computer_id=0)
# print(indices_de_busca)

# indices_de_busca["id"] = 1
# bd.update_indexes(computer_id=1, indices_de_busca=indices_de_busca)

# indices_de_busca["id"] = 2
# bd.update_indexes(computer_id=2, indices_de_busca=indices_de_busca)

# bd.persistent(util.read_json("json/vehicles_to_search.json"))

bd.print_all()