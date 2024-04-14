#LEGB Rule
#L - Local
#E - Enclosing Function
#G - Global
#B - Built In


#Global
name = "Global Name Ganapathy"

def say_hello(name):
    
    #Enclosing function name
    #name = "Enclosing Function Name Vinayaka"
    
    def print_hello(name):
        #Local Name
        #name = "Local Name Gannu"
        print(f"Say Hello to : {name}")

    print_hello(name)

say_hello(name)

print("*"*108)

x=50

def func():
    global x #accessing global namespace x
    x=200
    print(x)

print(x)
func()
print(x)

print("*"*108)

x=50

def func(x):
    x=200
    print(x)

print(x)
func(x)
print(x)