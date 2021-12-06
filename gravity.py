# using tuples and list with there methods
#create name for the list
list_name = input("Enter the name of the list: ")
list_name = list()
while True:
    item = input("Please enter an item to the list")
    list_name.append(item)
    response = input("Do you still wish to continue(Yes/No): ").lower()
    try:
        if response == "no":
            break
        else:
            continue
    except ValueError:
        print("Wrong input")
