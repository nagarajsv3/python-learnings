class Animal():

    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Not Impl")
    
class Dog(Animal):
    def speak(self):
        print(self.name + " says bow")

class Cat(Animal):
    def speak(self):
        print(self.name + " says meow")

animal = Animal("ani")
#animal.speak() #NotImplementedError: Not Impl

dog = Dog("Para")
cat = Cat("Sara")
dog.speak()
cat.speak()
