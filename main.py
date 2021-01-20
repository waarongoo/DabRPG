import time
from termcolor import colored
import sys
import replit
from replit import db
#Definitions | Login
loginSuccess = 0
#Ends Here
print("Note this Python script is still in beta.")
def accountCreate():
  for x in colored("Creating Account....", "white"):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.10)
    
  replit.clear()
  print("Account has been created successfully!")
username = (input("[Server] Enter an username: " ))
Numpassword = int(input("[Server] Please enter your password | Note: Characters are not allowed: "))
db[username] = Numpassword

accountCreate()
usernameLog = (input("[Server] Please enter your username: "))
value = db[username]

#login check
if usernameLog == username:
    NumpasswordLog = int(input("[Server] Please enter your password: "))
    if NumpasswordLog == Numpassword:
        print("Login successful!")
        loginSuccess = +1
    else:
        print("Your password is incorrect!")
        time.sleep(0.2)
        print("To reset your password, press the 'Run' button above to reset!")
        exit
else:
    print("Your username is incorrect!")
    time.sleep(0.2)
    exit

#start game
def Quest1():
    print("[Bailey] Howdy " + str(username) + " and welcome to DabRPG! I will train you on the basics on becoming the best warrior across all of DabRPG.")
    time.sleep(1.00)
    print("[Bailey] So lets get started shall we?")
    time.sleep(1.00)
    print("[Bailey] For your first quest, I would like you to go follow those signs there to the 'Barn' to collect me some hay!")
    time.sleep(1.00)

#Quest 1

if loginSuccess == 1:
  Quest1()
  QuestStart1 = (input("Accept Quest? "))

  if QuestStart1 == "yes" or "Yes" or "Y" or "y":
    print("[Bailey] Great!")
  else:
      exit

#Signs 1

#sign post 1

def signpost1():
    print("<- Barn")
    print("Forest ->")

def barn():
    print("Traveling to the barn!")
    time.sleep(1.00)
    print("Progress: ----------🚶")
    time.sleep(0.5)
    print("Progress: ---------🚶")
    time.sleep(0.5)
    print("Progress: --------🚶")
    time.sleep(0.5)
    print("Progress: -------🚶")
    time.sleep(0.5)
    print("Progress: ------🚶")
    time.sleep(0.5)
    print("Progress: -----🚶")
    time.sleep(0.5)
    print("Progress: ----🚶")
    time.sleep(0.5)
    print("Progress: ---🚶")
    time.sleep(0.5)
    print("Progress: --🚶")
    time.sleep(0.5)
    print("Progress: -🚶")
    time.sleep(0.5)
    print("Progress: 🚶")
    time.sleep(0.2)
    print("You have arrived at the 'Barn' !")

time.sleep(1.00)
signpost1()

signpost1 = (input("Would you like to go to the 'Barn' or the 'Forest' ? "))
#barn
if signpost1 == "Barn" or "barn":
    barn()
elif signpost1 == "Forest" or "forest":
    print("You do not have permission to go there!")
    time.sleep(0.10)
    print("Traveling to 'Barn' instead!")
    time.sleep(0.5)
    barn()
else:
  print("[Server] Sorry I did not understand your input!")
  print("[Server] Traveling to 'Barn' instead!")
  barn()

#barnarrive

reply = (input("[Farmer Joe] Welcome to the barn" + str(username) + "! What do you need today?"))
time.sleep(2)
print("Reply 1: Bailey sent me here to get some clay!")
print("Reply 2: Oh nothing thank you!")
time.sleep(1.00)
if reply == "1" or "one":
    print("[Farmer Joe] Oh! No probelmo, theres some hay laying around over there!")

elif reply == "2" or "two":
    print("die")
    
    print("pew pew pew pew pew pew pew")
    exit

else: 
    print("[Server] I did not understand your statement. Choosing option 1")

def walk():
  walkW = (input("Press 'W' to walk forward"))
if  walk == "W" or "w":
  print("You have walked one step!")


#walking2hay
walk()
walk()
walk()
walk()
walk()


pickup = (input("Pickup hay? "))
farmerBlade = 0
if pickup == "Yes" or "yes" or "y" or "Y":
    print("You have recieved 5 hay!")
    finishQuest = (input("Thank you for your help! As a reward, I will give you with a ~~Farmer's Blade~~ !"))
    farmerBlade = 1
    time.sleep(2)
else:
    exit



print("Farmer's Blade'")
print("Damage: 9")
print("Strength: 30")
print("--------------")
print("Item Ability: Crop Power!")
print("Adds 20 damage to your base damage of this blade based on how many monsters you have killed with this blade!")
time.sleep(2)
print("[Server] New Objective: Return to Bailey")

#walk to bailey 1
walk()
walk()
walk()
walk()
walk()