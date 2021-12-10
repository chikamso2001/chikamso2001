# I am going to create a program that converts temperature from  one unit to another

# defining a function to convert from celsius fahrenheit
def cel_fah(temp):
    fah = (1.8 * temp) + 32
    return fah 

# defining a function to convert from fahrenheit to celsius
def fah_cel(temp):
    cel = (5/9) * (temp - 32)
    return cel 

# defining a function to convert from celsius to kelvin
def cel_kelvin(temp):
    kelvin = temp + 273.15
    return kelvin 

# defining a function to convert from fahrenheit to kelvin
def fah_kelvin(temp):
    temp = fah_cel(temp)
    kelvin = temp + 273.15
    return kelvin


print("\t\t\t\tHere you will be given a list of temperature conversion options\n\n")
print("There are four options to choose from:\n")
print("""
1. Celsius --> Fahrenheit 
2. Fahrenheit --> Celsius
3. Celsius --> kelvin
4. Fahrenheit --> Kelvin\n\n""")

while True:
    choice1 = input("Please pick a number that corresponds to your choice: ")
    if choice1 == '1':
        temp = int(input("Enter the temperature in Celsius: "))
        temp_in_fah = cel_fah(temp)
        print(f"The converted value is {temp_in_fah} Fahrenheit\n")
        choice2 = input("Do you wish to continue(yes/no): ").lower()
        if choice2 == 'yes':
            continue
        else:
            break
    elif choice1 == '2':
        temp = int(input("Enter the temperature in Fahrenheit: "))
        temp_in_cel = fah_cel(temp)
        print(f"The converted value is {temp_in_cel} Celsius\n")
        choice2 = input("Do you wish to continue(yes/no): ").lower()
        if choice2 == 'yes':
            continue
        else:
            break
    elif choice1 == '3':
        temp = int(input("Enter the temperature in Celsius: "))
        temp_in_kelvin = cel_kelvin(temp)
        print(f"The converted valuse is {temp_in_kelvin} Kelvin")
        choice2 = input("Do you wish to continue(yes/no): ").lower()
        if choice2 == 'yes':
            continue
        else:
            break
    elif choice1 == '4':
        temp = int(input("Enter the temperature in Fahrenheit: "))
        temp_in_kelvin = fah_kelvin(temp)
        print(f"The converted value is {temp_in_kelvin} kelvin")
        choice2 = input("Do you wish to continue(yes/no): ").lower()
        if choice2 == 'yes':
            continue
        else:
            break