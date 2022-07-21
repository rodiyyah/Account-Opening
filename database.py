import os
import validation

user_db_path = "datas/user_records/"
def create(accountnumberfromuser, first_name, last_name, email, password):

    userdata = first_name + "," + last_name + "," + email + "," + password + "," + str(0)

    if does_account_number_exist(accountnumberfromuser):

        return False

    if does_email_exist(email):
        print("User alrerady exist")
        return False

    completion_state = False

    try:
        f = open(user_db_path + str(accountnumberfromuser) + ".txt" , "x")

    except FileExistsError:
        does_file_contain_data = read(user_db_path + str(accountnumberfromuser) + ".txt")
        if not does_file_contain_data:
            delete(accountnumberfromuser)

    else:
        f.write(str(userdata));
        completion_state = True
    
    finally:
        f.close();   
        return completion_state
    
    
def read(accountnumberfromuser):
    is_valid_account_number = validation.account_number_validation(accountnumberfromuser)
     
    try:
        if is_valid_account_number:
            f = open(user_db_path + str(accountnumberfromuser) + ".txt", "r")
        else:
            f = open(user_db_path + accountnumberfromuser, "r")

    except FileExistsError:
        print("user not found")

    except FileNotFoundError:
        print("File does not exist")

    except TypeError:
        print("Invalid account number format")

    else:
        return f.readline()
    return False

def update(accountnumberfromuser):
    print("Update user record")

def delete(accountnumberfromuser):

    is_delete_succesful = False

    if os.path.exists(user_db_path + str(accountnumberfromuser) + ".txt"):

        try:

            os.remove(user_db_path + str(accountnumberfromuser) + ".txt")
            is_delete_succesful = True

        except FileNotFoundError:
            print("File not found")

        finally:
            return is_delete_succesful
    
def does_email_exist(email):

    all_users = os.listdir(user_db_path)

    for user in all_users:
        user_list = str.split(read(user), ",")
        if email in user_list:
            return True
    
    return False
def does_account_number_exist(accountnumber):

    all_users = os.listdir(user_db_path)

    for user in all_users:
        
        if user == str(accountnumber) + ".txt":

            return True
    
    return False
def authenticated_user(accountnumber, password):

    if does_account_number_exist(accountnumber):

        user = str.split(read(accountnumber), ",")
        if password == user[3]:
            return user

    return False
print(does_account_number_exist(2079469291))

