def security():
    password = input('Please enter a password to secure your data: ')
    assure = False
    while assure == False:
        confirm = input('please re-enter password to confirm: ')
        if confirm == password:
            assure = True

import pandas as pd
#creating a memory storage for users who have an account
def memory():
    name = input('Enter your user name: ')
    password = input('Enter your password: ')
    the_info = {'names':name, 'passwords':password}
    the_info = pd.DataFrame(the_info)

name_of_file = input('Please enter the name of the file you want to create: ')
name_of_file = name_of_file +'.txt'
the_file = open(name_of_file,mode= 'w')
def add_info():
    quest = False
    while quest == False:
        store = input('Please make the inputs you wish to store: ')
        the_file.write(("{}\n".format(store)))
        ask = input('Do you want to make any additional info(yes/no): ').lower()
        if ask == 'yes':
            continue
        else:
            the_file.close()
            quest = True

security()
add_info()
