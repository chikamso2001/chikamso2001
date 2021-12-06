class animal():
    species = ' '
    def set_species(self, species_name):
        self.species = species_name
    def get_Species(self):
        return self.species
lion = animal()
lion.set_species('feline')
print(lion.get_Species())

# Another class for the humans
class person():
    name = ' '
    age = 0
    def set_age(self):
        the_age = input('Enter your age:\n')
        self.age = the_age
    def get_age(self):
        return self.age 
kamso = person()
kamso.set_age()
print('You are {} years old'.format(kamso.get_age()))

class dog():
    def __str__(self):
        return 'This is a dog class'
husky = dog()
print(husky)

class car():
    sound = 'honk'
    def __init__(self,name, color, type):
        self.name = name
        self.color = color
        self.type = type
ford = car('LAMD', 'red', 'RX100')

nissan = car('siena', 'black', '2001')
print(nissan.type, ford.type, nissan.color, ford.color)

class subject():
    def type(self, type, level):
        print('This is {} which is {}'.format(type, level))
class math(subject):
    opinion = 'like'

school = math()
print(school.type('science', 'easy'))
room = math()
print(room.opinion)


name = input('What\'s your name: ')
print(name)
age = input('How old are you: ')
print(age)