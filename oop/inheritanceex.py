class Animal():

    def __init__(self):
        print("Animal created")
    
    def eat(self):
        print("Animal is eating")
    
    def who_am_i(self):
        print("I am Animal")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def eat(self):
        print("I am dog ; I overrided Animal eat method and I am eating")

    def bark(self):
        print("I am dog ; I am barking WOOOOO")

mydog = Dog()
mydog.who_am_i()
mydog.eat() #Overrided method
mydog.bark()