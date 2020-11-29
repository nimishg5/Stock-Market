from pymongo import MongoClient

client = MongoClient('localhost', 27017)

def createConnectionWithDB(database, collection):
    global client
    db = client[database]
    collection = db[collection]
    return collection

def fetchNifty50AllStocks(collection):
    x = collection.find({}, {'_id': 0, 'stock': 1})
    nifty50List = []
    for data in x:
        nifty50List.append(data['stock'])
    return nifty50List

def closeConnection():
    client.close()