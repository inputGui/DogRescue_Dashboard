from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB 
    
    Attributes:
        client - MongoClient responsible for connection
        database - The database to connect to
    
    Methods:
        - create
        - read_all
        - read
        - update 
        - delete
    """

    def __init__(self, username, password):
        """ Initializing the MongoClient. This helps to 
        access the MongoDB databases and collections. """
        self.client = MongoClient("mongodb://%s:%s@localhost:45652/?authMechanism=DEFAULT&authSource=AAC"%(username,password))
        self.database = self.client['AAC']


    def create(self, data):
        """ Inserts a document in the animals database 
        
        Params:
            data - Dictionary containing the data to be inserted
            
        Returns:
            Boolean - True if inserted
            Exception - In case of error
         """
        
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary   
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read_all(self, data):
        """ Reads and returns a cursor from the found document(s)
        
        Params:
            data - Dictionary to be found and returned
        Returns:
            cursor - Cursor if found or None if not found
            
        """
        
        cursor = self.database.animals.find(data, {"_id": False} )
        return cursor
    
    def read(self, data):
        """ Reads and returns one document 
        
        Params:
            data - Dictionary to be found and returned
        Returns:
            cursor - List containing the found document or an empty list if not found
        """
        
        #return self.database.animals.find_one(data)
        
        result = self.database.animals.find_one(data)
        return [result] if result else []
    
    def update(self, query, new_data):
        """ Update documents based on query 
        
        Params:
            query - The filter to search for
            new_data - The new data to be added
        Returns:
            Boolean, data or error - Will return either true or false and the data or error
        """
        
        try:
            result = self.database.animals.update_many(query, {"$set": new_data})
            return True, result.raw_result
        except Exception as err:
            return False, str(err)
        
    def delete(self, query):
        """ Delete documents from animals collection 
        
        Params:
            query - The filter to be deleted
        Returns:
            Boolean, data or error - Will return either true or false and the data or error
        """
        
        try:
            result = self.database.animals.delete_many(query)
            return True, result.raw_result
        except Exception as err:
            return False, str(err)
       