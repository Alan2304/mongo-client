from mongoConfig import *
from bson.objectid import ObjectId

class Posts():
    @staticmethod
    def insert():
        author = input("Enter the author name")
        text = input("Enter the text for the post")
        #Conection to mongo
        db = connectMongo()
        testCollection = getCollection('test-collection', db)
        post = {
            "author": author,
            "text": text
        }
        post_id = testCollection.insert_one(post).inserted_id
        print("Post saved succesfully")

    @staticmethod
    def update():
        id = input("Enter the id of the post")
        _id = ObjectId(id)
        text = input("Enter the new text for the post")
        #Conection to mongo
        db = connectMongo()
        testCollection = getCollection('test-collection', db)
        testCollection.update(
            {"_id": _id},
            {"$set": {"text": text}}
        )
        print("Post updated succesfully")