allowedusers = ('diyyah', 'yussy','sammy')
allowedpassword = ('fade', 'knock', 'sis')
name = input('what is yourname?\n')
if(name in allowedusers):
    password = input('what is your password?\n')
    
    if(password in allowedpassword):
         print('welcome %s' % name)

    else:
        print("password incorrect, please try again")
        
else:
    print('name not found')

