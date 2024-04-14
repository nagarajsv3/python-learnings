class Dog():

    #CLASS OBJECT attribute
    #Same for any instance of a class
    species = "mammal"

    #Constructor
    #User defined object attribues
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    def bark(self, number):
        print(f"{self.name} is barking and the lucky number is {number}")

my_dog = Dog(breed="Lab", name='Kevin', spots=False)
print(my_dog)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)
print('*'*108)
my_dog.bark(3)
print('*'*108)
