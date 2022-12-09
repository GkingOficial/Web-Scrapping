from MongoDBWeb import MongoDBWeb
import util
from settings import number_of_computers

vehicles_to_search = util.read_json("json/vehicles_to_search.json")
length = len(vehicles_to_search)

bd = MongoDBWeb(
  vehicles_to_search_length=length,
  number_of_computers=number_of_computers
)
bd.delete_all()
bd.add_indexes()
bd.print_all()