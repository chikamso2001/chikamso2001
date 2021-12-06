class Animal():
    def __init__(self, species):
        self.species = species
class dog(Animal):
    def __init__(self, species, name):
        self.name = name
        super. __init__(species)
sam = dog("canine","husky")
print(sam.species)
print(sam.name)