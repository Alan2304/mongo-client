from mongoConfig import *
def main():
    db = connectMongo()
    testCollection = getCollection('test-collection', db)
    post = {
        "author": "Alan",
        "text": "Hello I'm Alan"
    }
    post_id = testCollection.insert_one(post).inserted_id
    print (post_id)

main()
