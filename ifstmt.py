
#is_male = True
is_male = False

if is_male:
    print('You are a male')
else:
    print('You are not a male')

is_male = False
is_tall = True
#and operator

if is_male and is_tall:
    print('You are a male and tall')
elif is_male and not(is_tall):
    print('You are a male and not tall')
elif not(is_male) and is_tall:
    print('You are not male and tall')
else:
    print('You are not male and not tall')

is_male = False
is_tall = False
#or operator

if is_male or is_tall:
    print('You are either male or tall')
else:
    print('You are neither male nor tall')

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(1,2,3))
print(max_num(230,120,1))


