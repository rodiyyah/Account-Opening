#register
# - username, password, email
# - generae useraccount

#login
# - [username or email] and password


#bank operation
#initializing the sysstem

import random

database = {} #dictionary

isvalidoptionselected = False
print("Welcome to diyyahbank")

def login():
    print("This is the login function")

def register():
    print("this is the register function")

def bankoperation():
    print("some operations")

def accountnumbergeneration():
    print("generating account number")
    return random.randrange(1111111111,9999999999)

while isvalidoptionselected == False:
    haveaccount = int(input("do you have an acount with us: 1. yes 2. no \n"))
    if(haveaccount == 1):
        isvalidoptionselected = True
        login()
    elif (haveaccount == 2):
        isvalidoptionselected = True
        register()
    else:
        print("you have selected an invalid option")

###ACTUAL BANKING SYSTEM###
print(accountnumbergeneration())

 