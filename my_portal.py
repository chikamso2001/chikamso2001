# creating an interactive web based interface 
# i'm going to create a dictionary to store users detail

# Please note that you could only login if you have been registered, every registered user is added to the dictionary
# Once registered the user can be logged in
# It's chikamso and please try every possible dynamics on my code and let me know when it crashes
# Thank you for helping me learn

import csv
from IPython.display import clear_output 

passwords = []
emails = []
user_details = dict()
# I will define a function to check if the user is logged in

def check_log():
    if emails == []:
        print('\t\t\t\t\t\t\t\tWelcome to my portal\n ')
        print('\t\t\t\t\tYou can trust me to keep your information safe and secured\n')
        print('Seems you are a new guest, well nice to have you :)')
    else:
        logout = input('Do you wish to log out from the portal(yes/no): \n').lower()
        try:
            if logout == 'yes':
                print('\t\t\t\t\tThank you for using my software')
            else:
                print('I like coffee, guess i have nothing much to say anymore')
        except:
            print('That was an invalid choice')


# Here i will define a function that would be used to log the user in
def login_user():
    while True:
        email = input('Please enter your email address:\n ')
        password2 = input('Please enter your password:\n')
        with open('register.csv', mode = 'r') as the_file:
            reader = csv.reader(the_file, delimiter = ",")
            reader.close()
            for row in reader:
                if row == [email, password2]:
                    print('You have been successfully logged in')
                    break
                else:
                    print('You entered an invalid email or password')
                    continue


# I will create a function that would be used to register 
def register():
    print('\n\t\t\t\t\tThank you for considering your registration')
    print("\nWe would like to receive some of your basic info for your registration")
    email = input('Please enter your email address:\n ')
    emails.append(email)
    password = input('Please enter your password:\n ')
    while True:
        password2 = input('please retype password:\n')
        if password == password2:
            passwords.append(password2)
            user_details[email] = password2
            print('\t\t\t\t\tYou have been successfully registered!!!!!')

            with open('register.csv', mode = 'a', newline = "") as myfile:
                writer = csv.writer(myfile, delimiter = ",")
                writer.writerow([email, password2])
            break

# Now i will have to put the whole functional parts together

check_log()

# i will define the function to add all funtions to a single function and create uniformity

def Myportal():
    user_choice = input('Would you like to login/register/quit:\n ').lower()
    try:
        if user_choice == 'login':
            login_user()
        elif user_choice == 'register':
            register()
        elif user_choice == 'quit':
            print('\t\t\t\t\t\n\nThank you for using my software')
    except:
        print('\nThat was an invalid choice')
        quit()

while True:
    Myportal()
    response = input('Are you sure you would like to exit my portal(yes/no):\n').lower()
    if response == 'no':
        continue
    else:
        print('\t\t\t\t\tI hope you come around again')
        break