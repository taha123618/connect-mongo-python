import pymongo

if __name__ == "__main__":
    print("welcome to py_mango")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)

    # creatingg database with collection
    db = client['tahaahmed']
    # Add collecton
    collection = db['mysampleCollectionFortaha']
    
    
