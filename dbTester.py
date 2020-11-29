from pymongo import MongoClient
from mongoMethods import *

def createConnection():
    client = MongoClient('localhost', 27017)
    db = client['stock-analyzer']
    return db

def getAllStocks():
    collection = createConnectionWithDB('stock-analyzer', 'Nifty50')
    fetchNifty50AllStocks(collection)

# getAllStocks()
# db = createConnection()
# collection = db['Nifty50']
# filename = 'nifty50-scripts.txt'

# with open(filename) as f:
#     content = f.readlines()
#     content = [x.strip() for x in content]


# for stock in content:
#     data = {}
#     data['stock'] = stock
#     rec_id1 = collection.insert_one(data)
#     print("Data inserted with record id",rec_id1)
