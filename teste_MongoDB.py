from MongoDBWeb import MongoDBWeb
import util

bd = MongoDBWeb()

vehicles_with_price = util.read_json("json/vehicles_with_price.json")
bd.persistent(vehicles_with_price)

bd.print_all()