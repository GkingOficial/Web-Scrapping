import json
from pprint import pprint
from pymongo import MongoClient

class MongoDBWeb:
  def __init__(self):
    self.password = "20deAbril%5Cn"
    self.user = "Gking"
    self.cluster = "ic-cluster"
    self.codigo = "lcpuy5t"
    
    self.client = MongoClient(
      f"mongodb+srv://{self.user}:{self.password}@{self.cluster}.{self.codigo}.mongodb.net"
    )
    self.database = self.client["veiculos"]
    self.collection = self.database["carros"]

  def add_indexes(self):
    self.collection.insert_one(
      {
        "id": 1,
        "marca": 0,
        "modelo_base": 0,
        "modelo_especifico": 0
      }
    )
    
  def update_indexes(self, marca, modelo_base, modelo_especifico):
    self.collection.update_one({"id": 1}, {'$set': {
          "marca": marca,
          "modelo_base": modelo_base,
          "modelo_especifico": modelo_especifico
        }
      }
    )

mongoWeb = MongoDBWeb()
mongoWeb.update_indexes(1, 2, 3)