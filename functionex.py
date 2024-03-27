def say_hi():
    print("Hello User")

say_hi()
say_hi()

def say_hi(name, age):
    print("Hello " + name + ", you are "+ str(age))

say_hi("Dhoni", 42)
say_hi("Virat", 35)

def cube(num):
    return num * num * num
result3 = cube(3)
print(result3)

result4 = cube(4)
print(result4)