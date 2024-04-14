class Circle():
    #CLASS OBJECT attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = Circle.pi * radius * radius

    def get_circumference(self):
        return 2 * Circle.pi * self.radius 
    
my_circle = Circle()
my_circle_circ = my_circle.get_circumference()
print(my_circle_circ)
print(my_circle.area)
print(my_circle.radius)
print(my_circle.pi)

print('*'*108)
my_circle2 = Circle(3)
my_circle_circ = my_circle2.get_circumference()
print(my_circle_circ)
print(my_circle2.area)
print(my_circle2.radius)
print(my_circle2.pi)


