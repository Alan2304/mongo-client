from mongoConfig import *

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