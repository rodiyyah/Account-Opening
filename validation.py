def account_number_validation(accountnumber):
    if accountnumber:


        try:
            int(accountnumber)

            if len (str(accountnumber)) == 10:
                return True
        except ValueError: 
            return False

        except TypeError:
            return False
               
    else:
        print("Account number is a required field")
        return False