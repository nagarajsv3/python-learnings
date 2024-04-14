"# python-learnings" 

Errors :
ValueError
NameError
FileNotFoundError


Static Code Analysis:
pylint myexample.py -r y


1. Tuple Unpacking
my_tuples = ( ("Naga", 35, "John Wick") , ("Ash", 30, "DDLJ") , ("Ayya", 60, "MI"))
for a, b, c in my_tuples:
    print(a)
    print(b)
    print(c)

print('*'*108)

#my_list = [[1,2,3,4,5] , [10,20,30,40,50], [100,200,300,400,500, 600]] #ValueError: too many values to unpack (expected 5)
my_list = [[1,2,3,4,5] , [10,20,30,40,50], [100,200,300,400,500]]
for a,b,c,d,e in my_list:
    print( a  )
    print( b )
    print( c )
    print( d )
    print( e )

2. While statement can have else block
while x<5 : 
    print(f'current val of x is {x}')
    x = x+1
else:
    print(f'exited while loop ; x val is {x} ; not less than 5')

3. try except finally statement can have else block
def ask_for_input():
    while True:
        try:
            num = int(input("Please input a number : "))
        except:
            print("Oh... Not a number")
            continue
        else:
            print("We got a number")
            break
        finally:
            print("End of try/except/finally")
            print("I always run")

4. Generators ex: range function
for num in range(5):
    print(num)

print('*'*108)

for num in range(0,10,3):
    print(num)

5. Enumerators ex : enumerate function
my_name = "Nagaraja"
for index, value in enumerate(my_name):
    print(index)
    print(value)
    print("\n")

print("*"*108)

my_list = ["Nagaraja", "Naveen", "Smita", "Mangala"]
for index, value in enumerate(my_list):
    print(index)
    print(value)

6. zip function
my_list1 = [1,2,3,4]
my_list2 = ["Mangala", "Naveen", "Smita", "Nagaraja"]
my_list3 = [10,20,30,40]

for item in zip(my_list1, my_list2, my_list3):
    print(item)
    print("\n")

for a,b,c in zip(my_list1, my_list2, my_list3):
    print(a)
    print(b)
    print(c)
    print("\n")

7. List Comprehension
celcius = [0,10, 20,30,40,50]
#for loop
farenheit = [ ((9/5)*temp + 32) for temp in celcius] 
print(farenheit)

#for with if
even_nums = [ num for num in range(0,11) if num %2==0]
print(even_nums) 

#for with if else
nums = [ num if num%2==0 else (num**2) for num in range(0,11) ]
print(nums) #even num ; squared odd nums

#nested for loops
my_list2 = [ x*y for x in [1,2,3] for y in [1,10,100]]

8. help(mylist.insert) # gives documentation

9. Functions - Positional
def add_numbers_positional(num1, num2, num3:int):
    return num1+num2

result = add_numbers_positional(1,2,3)
print(result)

10. Functions - Keyword (Notice * in the method arguments)
def add_numbers_keyword(*, num1, num2, num3:int):
    return num1+num2+num3
result = add_numbers_keyword(num1=1, num2=2, num3=3)
print(result)

11. Tuple unpacking with python function
def employee_month(employee_hours):
    emp_max_hours = 0
    emp_max_name = ""
    emp_max_age = 0

    for emp_name, emp_hours, emp_age in employee_hours:
        if emp_hours > emp_max_hours:
            emp_max_hours = emp_hours
            emp_max_name = emp_name
            emp_max_age = emp_age
        else:
            pass

    return (emp_max_name, emp_max_hours, emp_max_age) 

best_employee = employee_month(employee_hours)
print(best_employee)

12. *args - tuple 
pass arbitrary number of arguments. it will be stored as tuple
def myfunc(*args):
    print(args)
    return sum(args) * 0.05

print(myfunc(10 ,20 ,30 ,40 ,50))

13. **kwargs - keyword arguments - stored as dictionary
def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print(f'fruit {kwargs['fruit']} is present')
    else:
        print(f'fruit not present')

myfunc( veggie = 'Leaf', milk = 'Cow')

14. args and kwargs
def my_food(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f"I eat {args[1]} {kwargs['food']}")

my_food(3, 2, 4, 5, 6, 8, rice="White", food="eggs", fruit='Banana')

15. map function 
for item in map(square, mylist):
    print(item)

my_list_2 = list(map(square, mylist))
print(my_list_2)

16. filter function
def is_even(num):
    return num%2==0

my_nums = [1,2,3,4,5,6,7]

even_nums = list(filter(is_even , my_nums))
print(even_nums)

17. Lambda or Ananymous function
my_list = [1,2,3,4,5, 6, 7, 8]
sq_list = list(map(lambda num: num**2, my_list))
print(sq_list)

even_list = list(filter(lambda num : num%2==0, my_list))
print(even_list)