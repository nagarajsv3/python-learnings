try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError as te:
    print("Oh There is a Type Error")

try:
    x=5
    y=0
    z=x/y
except ZeroDivisionError as zde:
    print("Oh There is a Zero Division Error")
finally:
    print("All Done.")

def ask():
    while True:
        try:
            ip = input("Input a number : ")
            num = int(ip) 
            print(num**2)
        except:
            print("Not a number. Please re enter")
        else:
            print("Thank You")
            break

ask()