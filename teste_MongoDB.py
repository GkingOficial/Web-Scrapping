from MongoDBWeb import MongoDBWeb

bd = MongoDBWeb(vehicles_to_search_length=99, number_of_computers=3)
bd.delete_all()
bd.add_indexes()

indices_de_busca = bd.get_indexes(computer_id=0)
print(indices_de_busca)

indices_de_busca["id"] = 1
bd.update_indexes(computer_id=1, indices_de_busca=indices_de_busca)

indices_de_busca["id"] = 2
bd.update_indexes(computer_id=2, indices_de_busca=indices_de_busca)
bd.print_all()