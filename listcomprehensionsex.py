my_name = "Hanuman"

my_list = []
for letter in my_name:
    my_list.append(letter)

print(my_list)

my_list2 = [letter for letter in my_name]

print(my_list2)

my_num = [num for num in range(0, 10)]
print(my_num)

my_num_sq = [(num, num**2) for num in range(0,10)]
print(my_num_sq)

celcius = [0,10, 20,30,40,50]
farenheit = [ ((9/5)*temp + 32) for temp in celcius] 
print(farenheit)

farenheit_2 = []
for temp in celcius:
    farenheit_2.append((9/5)*temp + 32 )
print(farenheit_2)



even_nums = [ num for num in range(0,11) if num %2==0]
print(even_nums) 


nums = [ num if num%2==0 else (num**2) for num in range(0,11) ]
print(nums)

my_list = []
for x in [1,2,3]:
    for y in [1,10,100]:
        my_list.append(x*y)
print(my_list)

my_list2 = [ x*y for x in [1,2,3] for y in [1,10,100]]
print(my_list2)