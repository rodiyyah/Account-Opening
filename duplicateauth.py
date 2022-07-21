#register
# - Firstname, Lastname, password, email
# - generae useraccount

#login
# - accountnumber and password


#bank operation
#initializing the sysstem

import random
database = {} #dictionary

def init():

    print("Welcome to diyyahbank")

    haveaccount = int(input("do you have an account with us: 1. yes 2. no \n"))
    if(haveaccount == 1):
        login()
    elif(haveaccount == 2):
        print(register())
    else:
        print("you have selected an invalid option")

def login():
    print("Log into your account")
    bankoperation()

def register():
    print('*****Register****')
    email = input("what is your email address? \n")
    first_name = input("What is your firstname? \n")
    last_name = input("What is your lastname? \n")
    password = input("create your password \n")

    accountNumber = accountnumbergeneration()
    database[accountNumber] = [first_name, last_name, email, password]
    print("Your Account Has Been Created")
    login()
    
def bankoperation():
    print("some operations")

def accountnumbergeneration():

    return random.randrange(1111111111,9999999999)


###ACTUAL BANKING SYSTEM####
init()