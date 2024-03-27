
try:
    var = 10/1
    num1 = float(input("Enter a number: "))
    print(num1)
except ZeroDivisionError as err:
    print(err)
    print(err.__class__.__name__)
except ValueError as err:
    print(err.__class__.__name__)
    print(err)
except Exception as err:
    print(err.__class__.__name__)
    print(err)
else:
    print("No error happened")
finally:
    print("I will execute no matter")
