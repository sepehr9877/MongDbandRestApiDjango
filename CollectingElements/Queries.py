from pprint import pprint

from pymongo import MongoClient
password='sepehr12345'
client=MongoClient(f'mongodb+srv://sepehr:{password}@sepehr.ypt1dzn.mongodb.net/?retryWrites=true&w=majority')
AmazonDb=client['Amazon']
HeatCollection=AmazonDb['urlHeating']

def updatecateroy():
    HeatCollection.update_many({},{"$set":{"category":"Heating"}})
updatecateroy()
items=HeatCollection.find({})
for item in items:
    pprint(item)