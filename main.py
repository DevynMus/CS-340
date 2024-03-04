from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        username = 'aacuser'
        password = 'Password1'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32361
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username,password,HOST,PORT))
        self.dataBase = self.client['%s' % (DB)]
        self.collection = self.dataBase['%s' % (COL)]
    
# Complete this create method to implement the C in CRUD.
    def create(self, data):
        # Check if data paramater is not empty
        if data is not None:
            insert = self.dataBase.animals.insert(data)  # data should be dictionary

            # True if database entry creation is completed
            if insert !=0:
                return True
            else: 
                return False
         
        # Data was empty
        else:
            raise Exception("Nothing to delete, no data entered")

# Create method to implement the R in CRUD.
    def read(self, criteria=None):
        # Check if criteria paramater is not empty
        if criteria is not None:
            data = self.dataBase.animals.find(criteria,{"_id": False})
            # Print loop for each document found in the data
            #for document in data:
                #print(document)
        
        # Criteria was empty
        else:
            data = self.dataBase.animals.find({},{"_id": False})
        
        return data
    
    # Create method for the U in CRUD
    def update(self, criteria, updated):
        # Check if any data is selected
        if criteria is not None:
            if self.dataBase.animals.count_documents(criteria, limit = 1) != 0:
                update_result = self.dataBase.animals.update_many(criteria, {"$set": updated})
                result = update_result.raw_result
            else:
                # Raise if no document was found
                result = "No document found"
            return result
        # If no data was selected from initial call
        else:
            raise Exception("Nothing to update, no data entered")

# Create method for the D in CRUD
    def delete(self, remove):
        # Check if any data is selected
        if remove is not None:
            if self.dataBase.animals.count_documents(remove, limit = 1) != 0:
                delete_result = self.dataBase.animals.delete_many(remove)
                result = delete_result.raw_result
            else:
                # If data was not found, return false
                result = "No document found"
            return result
        # If no data was selected from inital call
        else:
            raise Exception("Nothing to delete, no data entered")
