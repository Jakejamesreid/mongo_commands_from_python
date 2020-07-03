import pymongo
import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
if os.path.exists(__location__+"\\env.py"):
    import env

MONGODB_URI = os.environ.get("MONGO_URI")
DBS_NAME = os.environ.get("DBS_NAME")
COLLECTION_NAME = os.environ.get("COLLECTION_NAME")

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

# Insert a new entry into the DB
new_doc = {'first': 'douglas', 'last': 'adams', 'dob': '11/03/1952', 'hair_colour': 'grey', 'occupation': 'writer', 'nationality': 'english'}
coll.insert(new_doc)

# Insert multiple entries into the DB
new_docs = [{'first': 'terry', 'last': 'pratchet', 'dob': '11/03/28/04/1948', 'hair_colour': 'not much', 'occupation': 'writer', 'nationality': 'english'},
{'first': 'george', 'last': 'rr martin', 'dob': '11/03/20/09/1948', 'hair_colour': 'white', 'occupation': 'writer', 'nationality': 'american'}]
coll.insert_many(new_docs)

# Find everyone whos name is Douglas
document = coll.find({'first': 'douglas'})
print(document.next())

# Delete entry from DB
coll.remove({'first': 'douglas'})

# Update one entry in DB
coll.update_one({'nationality': 'american'},{'$set':{'hair_colour': 'maroon'}})

# Update many entries in DB
coll.update_many({'nationality': 'american'},{'$set':{'hair_colour': 'orange'}})

# Find all entries in the DB
documents = coll.find()
for doc in documents:
    print(doc)

