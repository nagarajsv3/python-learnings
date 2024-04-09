from io import UnsupportedOperation
num1 = input("Enter num1 : ")
try:
    result = 10 + int(num1)
except Exception as exp:
    print(f'There is an error. Error {exp=}')
    #logger.info(msg=exp, exc_info=True, stack_info=True)
else:
    print("Addition went well")
    print(result)

try:
    filea = open('test.txt',mode='r')
    filea.write('Life is beautiful')
except UnsupportedOperation as ioexp:
    print("UnsupportedOperation")
    print(ioexp)
except Exception as exp:
    print("Exception")
    print(type(exp))
    print('Oh there was an exception')
finally:
    print('I always run')


print("*"*21)

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

ask_for_input()