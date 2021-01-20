from replit import db
key = input("Enter the username for the new user\n")
value = input("Enter the password for the new user\n")
db[key] = value
print("Done!")