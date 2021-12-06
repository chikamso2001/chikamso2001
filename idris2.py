A=listOfRides={"Mercedes":3300,"Honda":2500,"Toyota": 2300}
M="Mercedes"
H="Honda"
T="Toyota"
print('''\t\t\tBAKE's RIDES''')
print('''\t\t\t____________''')
print('''---------------------'''+ M +' , '+ H +' , '+ T +'''---------------------''')
print('''\n√ What type of ride do you prefer? [''' + M + ',' + H + ' or ' + T + ']')
i = input(">>>")
if i.title() in A:
	print("The price of " +i.title() + " is ₦ " +str(A[i.title()])+" but a discount of ₦"  +str(A[i.title()]-(A[i.title()]*0.5)) + "is given")
	print("Do you want the ride?")
	a = input("\nclick 1 if you want, otherwise, click 0 :  ")
	if a == '1':
		b = str(A[i.title()]-(A[i.title()]*0.5))
		print("The price of this ride is ₦ " + b)
	elif a == 0:
		del A[i.title()]
		print()
	