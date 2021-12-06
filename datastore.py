# In this project i will be using different data collection types
# A list, A tuple, A set, A dictionary.
# I will also make use of there method

# Creating a list
newlist = list()

# Appending items to the list
newlist.append("orange"); newlist.append("apple"); newlist.append("grape"); newlist.append("pineapple")
newlist.append("coconut")
print(newlist)
# finding the length of the list 
print("displaying the length of the list")
print(len(newlist))
print("\n\n")
# checking if an item is in the list
# Method 1
print("checking if apple is in the list\n")
print("apple" in newlist)
# Method 2 using the for loop
for items in newlist:
    if items == "apple":
        print(True)
        print("So yeah, apple is in the list\n")

# I am going to sort the 
print("The list when sorted") 
newlist.sort()
print(newlist)
#  Sorting in reverse order
print("\nThis is the list when sorted in the reverse order")
newlist.sort(reverse = True)
print(newlist)
# Now i am going to remove the third item in the list
newlist.pop(2)
print("After deleting the list we have ")
print(newlist)
print("\n\n")
# Here we copy the list into a new variable
newlist1 = newlist.copy()
print(newlist1)
# Let me clear the first list
print("\n\nI will clear the first list")
newlist.clear()
print("After clearing the list we have ")
print(newlist)
# Now i will delete the second list
del(newlist1)
# I am going to check if the list has been really deleted
try:
    print(newlist1)
    print("Looks like the list hasn't been deleted")
except NameError:
    print("Check completed!!!, the list has been deleted.\n\n")


# Now are going to work with tuples 
print("\n\nNow we are going to work with tuples")
# creating a tuple
newtuple = tuple()
newtuple = list(newtuple)
# Adding items to the tuple
# I had to convert the tuple to a list to add the following items
newtuple.append("football"); newtuple.append("basketball"); newtuple.append("soccer");
newtuple.append("golf")
newtuple = tuple(newtuple)
print(newtuple)
# Since a tuple is immutable we had to change them  to a list to do so
print("\nConverting a tuple to a list we get:")
newtuple1 = list(newtuple)
print(f"the tuple {newtuple}, is now a list which is {newtuple1}")
print("I will add new items to the list then convert it back to a tuple\n\n")
# Adding items to the list which was converted from a tuple
newtuple1.append("kamso"); newtuple1.append("chidalu"); newtuple1.append("neche")
# Converting from a list back to a tuple
newtuple1 = tuple(newtuple1)
print(f"The tuple {newtuple1} is now a {type(newtuple1)}")


# Now we are going to see the properties of a set
# A set is unordered, unchangable, doesn't accept duplicate terms
# Now i create a set
new_set = set(("physics", "chemistry", "math", "biology", "english"))
print(new_set)
print("\n")
# terms can be added to the set
print("Now i am going to add Religion to the set")
new_set.add("Religion")
print(new_set)
print("\n")
# we can also add another set or list to the already created list
# let me create another set
another_set = set(("houses", "airplanes", "bicycles"))
list_for_set = list(["cow", "chicken", "plantain"])
# Here i will update the new_set to incluse the another_set
print("I am going to add another set to the already displayed set\n")
new_set.update(another_set)
print("Here is the updated set")
print(new_set)
print("\n")
print("Now i am going to add a list to the set")
new_set.update(list_for_set)
print(new_set)

# Here we are going to deal with dictionaries
# creating a dictionary
new_dict_car = {"name":"Toyota", "color":"red", "model":"LX500", "year":2019 }
print("I created a dictionary, here it is:")
print(new_dict_car)
print("\n")
# I will display now only the keys of the dictionary
print("Now i will display only the keys of the dictionary")
print(new_dict_car.key())
# This time i display only the values of the dictionary
print("\nNow to display only the values of the dictionary")
print(new_dict_car.value())
print("\n this time we display the key value pair")
print(new_dict_car.items())

# creating a nested dictionary
family = {"child1":{"name":"kamso","year":2001},"child2":{"name":"dalu","year":2003}}
