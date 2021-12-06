cars = {"Mercedes":3300,"Honda":2500,"Toyota": 2300}
discount_rate = 0.5
import datetime as dt 
now = dt.datetime.now()
if now.hour < 12:
    print('GOOD MORNING')
elif now.hour < 17 and now.hour > 12:
    print('GOOD AFTERNOON')
else:
    print('GOOD EVENING')
print('\t\t\t\t\t\t_________AUTO DEALER__________')
print('\n\nThe available vehicle brands in stock are:\n')
print("""\tMercedes
         Toyota
         Honda
    """)


# I will define the function for providing discounts
def get_discount(choice):
    discount_amount = cars[choice] * discount_rate
    discounted_price = cars[choice] - discount_amount
    return discounted_price

# i will define the function for getting discounted price of all the cars
def car_discount():
    car_list = ['Mercedes', 'Toyota', 'Honda']
    count = len(car_list)

    for car_choice in car_list:
        discount = get_discount(car_choice)
        print('The cost of {} is ${} but with the discount the price is ${}\n'.format(car_choice, cars[car_choice], discount))
        response = input('\nDo you still want this car(yes/no): ').lower()
        if response == 'yes':
               print('Thank you for your purchase')
        elif response == 'no':
            car_list.remove(car_choice)
            count = len(car_list)
            print('You still have {} options which are {}\n'.format(count, car_list))
            if count == 1:
                ans = input('Do you want to buy the {} (yes/no)'.format(car_list[0])).lower()
                if ans == 'yes':
                    print('Thank you for the purchase')
                else:
                    print('There are no more option\n')
                    print('Thank you for choosing us')
            

try:
    car_choice = input("\nWhich car brand would you like to purchase: ").title()
    get_discount(car_choice)
    car_discount()
except:
    print('The choice you made isn\'t in the option provided')
