from replit import db
key = input("Enter the username that you want to remove from the database\n")
del db[key]
print("Done!")