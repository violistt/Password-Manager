import sys
import os.path
import getpass


master_password = "abc"

login = getpass.getpass(prompt = "Enter master password: ") # Hides master password when typing.

print()


def checkExistence(): # Checks existence of 'info.txt' file.
    if os.path.exists("info.txt"):
        pass
    else:
        file = open("info.txt", 'w')
        file.close

checkExistence()


file = open("info.txt", 'r')


def saveNew(): # Saves new login data.


    file = open("info.txt", 'a')
    userName = input("Please enter the user name: ")


    while True:
        password = input("Please enter the password: ")
        password_again = input("Please retype the password: ")
        if password == password_again:
            break
        else:
            print("Passwords don't match. Please try again.")


    website = input("Please enter name of website: ")
    user_name = "UserName: " + userName + "\n"
    pass_word = "Password " + password + "\n"
    web_site = "website " + website + "\n"

    file.write("--------------------\n")
    file.write(user_name)
    file.write(pass_word)
    file.write(web_site)
    file.write("--------------------\n")
    file.write("\n")
    file.close
    print()
    print("--------------------------------------")
    print("Your login data has been saved.")
    print("--------------------------------------")


if login == master_password: # When you enter correct password.
    options = "-------------------------\nSave new password(1)\n-------------------------\nView stored passwords(2)\n-------------------------\nQuit(3)\n-------------------------"
    print(options)
    print()
    option = input("What do you want to do?: ")
    print()


    if option == "1":
        
        saveNew()    

    elif option == "2":
        view = open("info.txt", "r")
        print("Loading...\n")
        print(view.read())


    else:
        sys.exit()


else: # If you enter wrong master password
    print("Permision denied")