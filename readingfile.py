employee_file = open("employee.txt", "r")
print(employee_file.readable())
print(employee_file.read())
employee_file.close()

employee_file = open("employee.txt", "r")
print(employee_file.readable())
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())
employee_file.close()

employee_file = open("employee.txt", "r")
print(employee_file.readable())
print(employee_file.readlines())
employee_file.close()

print("*****for*******************")
employee_file = open("employee.txt", "r")
print(employee_file.readable())
for employee in employee_file.readlines():
    print(employee)
employee_file.close()