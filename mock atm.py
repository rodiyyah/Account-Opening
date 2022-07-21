allowedusers = ('diyyah', 'yussy','sammy')
allowedpassword = ('fade', 'knock', 'sis')

name = input('what is your name?\n')
if(name in allowedusers):
    password = input('what is your password?\n')
    print('These are the available options')
    print('1. Withdrawal')
    print('2. Cash deposit')
    print('3. complaint')
    
    selectedOption = int(input('please select an option'))
    print(selectedOption)
    
    if(selectedOption == 1):
        print("you selected %s" %selectedOption)

        amount = int(input('how much do you want to withdraw?\n'))
        print("withdrawal succesful")
    elif(selectedOption == 2):
        print("you selected %s"% selectedOption)
        depositamount = int(input("how much do you want to deposit?\n"))
        print("deposit succesful")

    elif(selectedOption == 3):
        print("you selected %s" % selectedOption)
    else:
        print("Invalid option selected, please try again.")
    
    if(password in allowedpassword):
        print('welcome %s' % name)
    else:
            print("password incorrect, please try again")
else:
    print('name not found please try again')
        
