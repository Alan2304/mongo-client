from Posts import *
def main():
    while 1:
        print("1.- Create Post\n2.-Update Post\n3.-Delete Post\n4.-Read Posts\n5.-Find by tag\n6.-Exit")
        option = input("Enter the option: ")
        if option == "6":
            print("Exit Program")
            exit()
        
        switcher = {
            "1": Posts.insert,
            "2": Posts.update,
            "3": Posts.delete,
            "4": Posts.read,
            "5": Posts.findByTag
        }
        print(option)
        operation = switcher.get(option, lambda: "Invalid operation")
        operation()

main()
