print("TOP Level in one.py")

def func():
    print("I am func function in one.py")

def say_hello():
    print("Hello World")

def say_hi():
    print("Hi")

if __name__ == "__main__":
    print("one.py is run directly")
    func()
    say_hello()
    say_hi()
else:
    print("one.py is imported")
