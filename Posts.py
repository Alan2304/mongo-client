from mongoConfig import *
from bson.objectid import ObjectId

class Posts():
    @staticmethod
    def insert():
        author = input("Enter the author name: ")
        text = input("Enter the text for the post: ")
        tags = []
        while 1:
            tag = input("Enter the tag: ")
            tags.append(tag)
            if (input("Add another tag to the post? y/n: ") == "n"):
                break

        #Conection to mongo
        db = connectMongo()
        testCollection = getCollection('test-collection', db)
        post = {
            "author": author,
            "text": text,
            "tags": tags
        }
        post_id = testCollection.insert_one(post).inserted_id
        print("Post saved succesfully")

    @staticmethod
    def update():
        id = input("Enter the id of the post: ")
        _id = ObjectId(id)
        text = input("Enter the new text for the post: ")
        #Conection to mongo
        db = connectMongo()
        testCollection = getCollection('test-collection', db)
        testCollection.update(
            {"_id": _id},
            {"$set": {"text": text}}
        )
        print("Post updated succesfully")

    @staticmethod
    def delete():
        author = input("Enter the name of the author: ")
        #Conection to mongo
        db = connectMongo()
        testCollection = getCollection('test-collection', db)
        testCollection.delete_many({"author": author})
        print("The post of " + author + " were deleted succesfully")
    
    @staticmethod
    def read():
        author = input("Enter the name of the author: ")
        db = connectMongo()
        testCollection = getCollection('test-collection', db)
        posts = testCollection.find({"author": author})
        for post in posts:
            print("-------------------------------")
            print("Author: " + post.get('author'))
            print("Text: " + post.get('text'))
            tags = post.get("tags")
            for tag in tags:
                print("Tag: " + tag)
            print("-------------------------------")
    
    @staticmethod
    def findByTag():
        tags = []
        while 1:
            tag = input("Enter the tag to search: ")
            tags.append(tag)
            if (input("Add another tag to search? y/n: ") == "n"):
                break
        db = connectMongo()
        testCollection = getCollection('test-collection', db)
        posts = testCollection.find({"tags": {"$all": tags}})
        for post in posts:
            print("-------------------------------")
            print("Author: " + post.get('author'))
            print("Text: " + post.get('text'))
            tags = post.get("tags")
            for tag in tags:
                print("Tag: " + tag)
            print("-------------------------------")
