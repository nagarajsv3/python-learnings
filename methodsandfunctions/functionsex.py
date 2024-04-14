'''
def say_hello():
    print("Hello")
'''
def say_hello(name="World"): #Default value
    print(f"hello {name}")

say_hello()
say_hello("Naga")

print("*"*108)

def add_numbers_positional(num1, num2, num3:int):
    return num1+num2

result = add_numbers_positional(1,2,3)
print(result)

result = add_numbers_positional(2,4,6)
print(result)

def add_numbers_keyword(*, num1, num2, num3:int):
    return num1+num2+num3
result = add_numbers_keyword(num1=1, num2=2, num3=3)
print(result)
result = add_numbers_keyword(num1=2, num2=4, num3=6)
print(result)

def even_check(number):
    return (number % 2 == 0)

print(even_check(20))
print(even_check(21))

def check_even_list(num_list):
    for num in num_list:
        if num%2 == 0:
            return True
        else:
            pass
    return False

print(check_even_list([1,1,1,1,2]))
print(check_even_list([2,1,1,1,1]))
print(check_even_list([2,4,6]))
print(check_even_list([1,3,5,7,9]))

def get_even_numbers(input_list):
    even_list = []
    for num in input_list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            pass
    return even_list

print(get_even_numbers([1,1,1,1,2]))
print(get_even_numbers([2,1,1,1,1]))
print(get_even_numbers([2,4,6]))
print(get_even_numbers([1,3,5,7,9]))

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

employee_hours = [("Ram", 1000, 21), ("Som", 200, 33), ("Shyam", 300, 44)] 
print(employee_month(employee_hours))
best_employee = employee_month(employee_hours)
print(best_employee)
print(best_employee[0])
print(best_employee[1])
print(best_employee[2])