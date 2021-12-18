import pymongo

if __name__ == "__main__":
    print("welcome to py_mango")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)

    # creatingg database with collection
    db = client['tahaahmed']
    # Add collecton
    collection = db['mysampleCollectionFortaha']

    # Insertion code (swith database)
    
    # How to insert document(jb tk nhi kre database ma data show nhi hoga)
    # dictionary = {'name ': 'taha' , 'marks': 47}
    # collection.insert_one(dictionary)

    # dictionary2 = {'name ': 'taha' , 'marks': 40}
    # collection.insert_one(dictionary2)

    # insert many use for muiltiple doc to magriedion 
    
    insertThis = [
        { 'id' : 1 , 'Name' : 'taha' , 'location' : 'karachi' , 'age' : 21},
        { 'id' : 2 , 'Name' : 'taha1' , 'location' : 'karachi' , 'age' : 22},
        { 'id' : 3 , 'Name' : 'taha2' , 'location' : 'karachi' , 'age' : 23},
        { 'id' : 4 , 'Name' : 'taha3' , 'location' : 'karachi' , 'age' : 24}
    ]
    collection.insert_many(insertThis)

