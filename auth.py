#register
# - username, password, email
# - generae useraccount

#login
# - [username or email] and password


#bank operation
#initializing the sysstem
import random
import validation
import database
from getpass import getpass

# database = {
#     1753772826: ["fade", "rera", "email", "diyyah"]
# } #dictionary

def init():

    isvalidoptionselected = False
    print("Welcome to diyyahbank")

    while isvalidoptionselected == False:
     
         haveaccount = int(input("do you have an account with us: 1. yes 2. no \n"))
        
         if(haveaccount == 1):
            isvalidoptionselected = True
            login()

         elif(haveaccount == 2):
            isvalidoptionselected = True
           
            register()
        
         else:
            print("you have selected an invalid option")

def login():
    print("*****Login*****")
    isloginsuccessful = False

    while isloginsuccessful == False: 

        accountnumberfromuser = input("What is your account number? \n")

        is_valid_accountnumber = validation.account_number_validation(accountnumberfromuser)

        if is_valid_accountnumber:
            password = getpass("what is your password? \n" )
            user = database.authenticated_user(accountnumberfromuser, password)

            if user:
                bankoperation(user)

            # for accountnumber, userdetails in database.items():
            #     if accountnumber == int(accountnumberfromuser):
            #         if userdetails[3] == password:
            #             isloginsuccessful = True
            #             bankoperation(userdetails)

            else:
                print("Invalid account number or Password")
                login()

        else:
            print("account number invalid:check that ou have up to 10 digits and only integers")
            init()

def register():

    print('*****Register****')
    email = input("what is your email address? \n")
    first_name = input("What is your firstname? \n")
    last_name = input("What is your lastname? \n")
    password = getpass("Create your password \n" )

    accountnumber = accountnumbergeneration()
    # database[accountNumber] = [first_name, last_name, email, password, 0]
    is_user_created = database.create(accountnumber, first_name, last_name, email, password)
    
    if is_user_created:
        
        print("Your Account Has Been Created")
        print("** *** ***** ******")
        print("Your account number is: %d" % accountnumber)
        print("** *** ***** ******")

        login()
    
    else:
        print("something went wrong, please try again")
        register()

def bankoperation(user):
    print("Welcome %s %s" % (user[0], user[1] ))
    selectedoption = int(input("What would you like to do? 1. Deposite 2. Withdraw 3. Logout 4. Exit\n"))
    if(selectedoption == 1):
        depositeoperation()
    elif(selectedoption == 2):
        withdrawaloperation()
    elif(selectedoption == 3):
        logout()
    elif(selectedoption == 4):
        exit()
    else:
        print("Choose an available function")
        bankoperation(user)

def depositeoperation():
    print("This is the deposite function")
    depositeoption = int(input("what would you like to do? 1.exit 2.login\n"))
    if (depositeoption == 1):
        exit()
    elif(depositeoption == 2):
        login()
    else:
        print("Kindly choose an availlable option")
        depositeoperation()


def withdrawaloperation():
    print("This is the withdrawal function")
    withdrawaloption = int(input("what would you like to do? 1.exit 2.login\n"))
    if (withdrawaloption == 1):
        exit()
    elif(withdrawaloption == 2):
        login()
    else:
        print("Kindly choose an availlable option")
        withdrawaloperation()

def accountnumbergeneration():
    print("generating account number ")
    return random.randrange(1111111111,9999999999)
def set_current_account_balance(userdetails, balance):
    userdetails[4] = balance

def get_current_accont_balance(userdetails):
    return userdetails[4]
def logout():
    login()
###ACTUAL BANKING SYSTEM####

init()