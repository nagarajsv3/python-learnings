class Dog():
    def __init__(self, name):
        self.name = name
    
    def speaks(self):
        return self.name + " ; type Dog ; says hello"

class Cat():
    def __init__(self, name):
        self.name = name
    
    def speaks(self):
        return self.name + " ; type Cat ; says hello"
    

jack = Dog("Jack")
tom = Cat("Tom")

for mypet in [jack, tom]:
    print(type(mypet))
    print(mypet.speaks())

def my_pet_speaks(my_pet):
    return my_pet.speaks()

print(my_pet_speaks(jack))
print(my_pet_speaks(tom))
