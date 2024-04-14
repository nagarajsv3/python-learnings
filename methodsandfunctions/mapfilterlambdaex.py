def square(num):
    return num**2

mylist = [1,2,3,4,5]
for item in map(square, mylist):
    print(item)

my_list_2 = list(map(square, mylist))
print(my_list_2)

def splicer(mystring):
    if len(mystring) %2==0:
        return 'EVEN'
    else:
        return mystring[0]

names_list = ["Nagaraja", "Ashwini", "Leela"]

spliced_list = list(map(splicer, names_list))
print(spliced_list)        

def is_even(num):
    return num%2==0

my_nums = [1,2,3,4,5,6,7]

even_nums = list(filter(is_even , my_nums))
print(even_nums)

print('**********Lambda function - anonymous functions')

my_list = [1,2,3,4,5, 6, 7, 8]
sq_list = list(map(lambda num: num**2, my_list))
print(sq_list)

even_list = list(filter(lambda num : num%2==0, my_list))
print(even_list)