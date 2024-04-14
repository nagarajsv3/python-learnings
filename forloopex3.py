my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in my_list:
    print(num)

print('*'*108)

for num in my_list:
    print("Hello")

print('*'*108)

for num in my_list:
    if (num % 2 == 0) :
        print(num)

print('*'*108)

for num in my_list:
    if num % 2 != 0 :
        print(num)

print('*'*108)

total_sum = 0

for num in my_list:
    total_sum = total_sum + num
print(total_sum)

print('*'*108)

my_string = "Hanuman"
for letter in my_string:
    print(letter)
    print(letter.upper())

print('*'*108)
my_tuples = (10, 20, 30, 40, 50)
for my_tup in my_tuples:
    print(my_tup)

print('*'*108)
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

print("*"*108)
my_dict = {'k1': 100, 'k2': 200, 'k3' : 300}
for item in my_dict:
    print(item)

for item in my_dict.items():
    print(item)

for key, value in my_dict.items():
    print(key)
    print(value)